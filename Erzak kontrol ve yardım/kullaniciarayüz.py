import sqlite3
import pandas as pd
conn = sqlite3.connect('veritabaný.db')
conn.execute('''CREATE TABLE IF NOT EXISTS depremzedeler
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                ad_soyad TEXT NOT NULL,
                konum TEXT NOT NULL,
                ihtiyaç TEXT NOT NULL,
                ihtadet TEXT NOT NULL)''')

def yardým_oku():
    dt = pd.read_csv("Erzakyardým.csv", sep=';')
    df_filtered = dt[dt['adet'] > 0]
    print(df_filtered)
class kayit:
   def __init__(self, ad_soyad, konum, ihtiyaç, ihtadet):

       self.ad_soyad = ad_soyad

       self.konum = konum

       self.ihtiyaç = ihtiyaç

       self.ihtadet = ihtadet
   def depremzedeleri_kaydet(self):
        conn.execute("INSERT INTO depremzedeler(ad_soyad, konum, ihtiyaç, ihtadet) VALUES (?, ?, ?, ?)",
                     (self.ad_soyad, self.konum, self.ihtiyaç, self.ihtadet))
        conn.commit()
        conn.close()
def menü():
    ad_soyad = input("Adýnýz Soyadýnýz:")
    konum = input("Bulunduðunuz yerin adý ve adresi:")
    yardým_oku()
    sorgu="e"
    while sorgu.lower()=="e":
        ihtiyaç=input("Ýhtiyaçlarýnýzý sýrasýyla virgülle(,) ayýrarak yazýnýz: \n")
        ihtadet=input("Kaç adet:\n")
        sorgu=input("Baþka ihtiyacýnýz varmý? EVET[E]/HAYIR[H]")
        deprem=kayit(ad_soyad, konum, ihtiyaç , ihtadet)
        deprem.ihtiyaç += ", " + ihtiyaç
        deprem.ihtadet += ", " + ihtadet
    deprem.depremzedeleri_kaydet()

# SQLite veritabanýna baðlan
con = sqlite3.connect('gorev_yonetim.db')
cursor = con.cursor()
# Görevliler tablosunu oluþtur
cursor.execute('''CREATE TABLE IF NOT EXISTS gorevliler (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tc_kimlik TEXT,
                    kullanici_adi TEXT,
                    sifre TEXT
                )''')
def main_menu():
    while True:
      print("1.Görevli Giriþi")
      print("2.Depremzedeler Ýçin Yardým Talebi")
      print("3.Çýkýþ")
      secim1=int(input("Lütfen bir iþlem seçiniz: "))  
      if secim1==1:
        secim = input("Seçiminizi yapýn (1-5):\n"
                      "1. Kullanýcý Kaydet\n"
                      "2. Kullanýcý Giriþi\n"
                      "3. Þifre Sýfýrlama\n"
                      "4. Admin Giriþi\n"
                      "5.Çýkýþ\n")
    
        if secim == "1":
            kullanici_adi = input("Kullanýcý adý: ")
            sifre = input("Þifre: ")
            sifre2 = input("Þifreyi tekrar giriniz: ")
            if sifre == sifre2:
                tc_kimlik = input("TC Kimlik Numarasý: ")
                kullanici_kaydet(kullanici_adi, sifre, tc_kimlik)
                
            else:
                print("Þifreler uyuþmuyor. Lütfen tekrar deneyin.")
        elif secim == "2":
            tc_kimlik = input("TC Kimlik Numarasý: ")
            if len(tc_kimlik) != 11:
                print("Geçersiz TC kimlik numarasý. TC kimlik numarasý 11 haneli olmalýdýr.")
            else:
                sifre=input("sifre: ")
                cursor.execute("SELECT * FROM gorevliler WHERE tc_kimlik = ? AND sifre= ?", (tc_kimlik,sifre))
                user = cursor.fetchone()
                if user:
                    print("Kullanýcý giriþi baþarýlý.")
                    depremzede_yardim_gönder()
                else:
                    print("Geçersiz TC kimlik numarasý. Lütfen tekrar deneyin.") 
        elif secim == "3":
            tc_kimlik = input("TC Kimlik Numarasý: ")
            sifre_sifirla(tc_kimlik)
        elif secim == "4":
             admin()
        elif secim == "5":
            print("çýkýlýyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
      elif secim1==2:
          
           break
      elif secim1==3:
           print("çýkýlýyor...")
           break
      else:
           print("Hatalý deðer girdiniz!")
           continue
    con.close()
# Kullanýcý kaydetme fonksiyonu
def kullanici_kaydet(kullanici_adi, sifre,tc_kimlik):
    if len(tc_kimlik) != 11:
        print("Geçersiz TC kimlik numarasý. TC kimlik numarasý 11 haneli olmalýdýr.")
        return

    cursor.execute("SELECT * FROM gorevliler WHERE tc_kimlik = ?", (tc_kimlik,))
    user = cursor.fetchone()
    if user:
        print("Bu TC kimlik numarasý zaten kayýtlý. Lütfen farklý bir TC kimlik numarasý deneyin.")
        return

    cursor.execute("INSERT INTO gorevliler (kullanici_adi, sifre, tc_kimlik) VALUES (?, ?, ?)",
                   (kullanici_adi, sifre, tc_kimlik))
    
    print("KUllanýcý Bilgileri Baþarýyla kaydedildi")
    con.commit()
    
# Kullanýcý giriþi kontrol fonksiyonu
def kullanici_giris(tc_kimlik, sifre):
    if len(tc_kimlik) != 11:
        print("Geçersiz TC kimlik numarasý. TC kimlik numarasý 11 haneli olmalýdýr.")
        return

    cursor.execute("SELECT * FROM gorevliler WHERE tc_kimlik = ?", (tc_kimlik))
    user = cursor.fetchone()
    if user:
        print("Kullanýcý giriþi baþarýlý.")
    else:
        print("Geçersiz TC kimlik numarasý. Lütfen tekrar deneyin.")
def kullanici_listele():
    cursor.execute("SELECT * FROM gorevliler")
    users = cursor.fetchall()
    for user in users:
        print("Kullanýcý Adý:", user[2])
        print("TC Kimlik Numarasý:", user[1])
        print("----------------------")
# Þifre sýfýrlama fonksiyonu
def sifre_sifirla(tc_kimlik):
    if len(tc_kimlik) != 11:
        print("Geçersiz TC kimlik numarasý. TC kimlik numarasý 11 haneli olmalýdýr.")
        return
    cursor.execute("SELECT * FROM gorevliler WHERE tc_kimlik = ?", (tc_kimlik,))
    user = cursor.fetchone()
    if user:
        yeni_sifre = input("Yeni þifreyi girin: ")
        cursor.execute("UPDATE gorevliler SET sifre = ? WHERE tc_kimlik = ?", (yeni_sifre, tc_kimlik,))
        con.commit()
        print("Þifre baþarýyla sýfýrlandý.")
    else:
        print("Geçersiz TC kimlik numarasý veya þifre. Lütfen tekrar deneyin.")
def kullanici_sil(tc_kimlik):
    cursor.execute("SELECT * FROM gorevliler WHERE tc_kimlik = ?", (tc_kimlik,))
    user = cursor.fetchone()
    if user:
        cursor.execute("DELETE FROM gorevliler WHERE tc_kimlik = ?", (tc_kimlik,))
        con.commit()
        print("Kullanýcý baþarýyla silindi.")
    else:
        print("Geçersiz TC kimlik numarasý. Lütfen tekrar deneyin.")
        
kullanicilar = [
    {"kullanici_adi": "admin", "sifre": "admin", "yetki": "admin"},
]
def admin():
    kullanici_adi = input("Kullanýcý adýnýzý girin: ")
    sifre = input("Þifrenizi girin: ")
    for kullanici in kullanicilar:
     if kullanici["kullanici_adi"] == kullanici_adi and kullanici["sifre"] == sifre:
      if kullanici["yetki"] == "admin":
        print("Admin giriþi baþarýlý.")
        while True:
            print("\nAdmin Paneli:")
            print("1. Kullanýcýlarý Listele")
            print("2. Kullanýcý Sil")
            print("3.Yardým Gönderilen bilgileri")
            print("4.Çýkýþ")
        
            secim = input("Seçiminizi yapýn (1-4): ")
        
            if secim == "1":
                kullanici_listele()
            elif secim == "2":
                tc_kimlik = input("TC Kimlik Numarasý: ")
                kullanici_sil(tc_kimlik)
            elif secim == "3":
                 conn = sqlite3.connect('veritabaný.db')
                 cursor = conn.cursor()
                 cursor.execute("SELECT * FROM gönderilen_depremzedeler")
                 # Listelenen depremzedeleri ekrana yazdýr
                 rows = cursor.fetchall()
                 for row in rows:
                      print(row)
            elif secim == "4":
                print("Admin panelinden çýkýlýyor...")
                break
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
def depremzede_yardim_gönder():
    conn = sqlite3.connect('veritabaný.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gönderilen_depremzedeler (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       ad_soyad TEXT NOT NULL,
       konum TEXT NOT NULL,
       ihtiyaç TEXT NOT NULL,
       ihtadet TEXT NOT NULL
    )
    """)
    # Depremzedeleri listele
    cursor.execute("SELECT * FROM depremzedeler")
    # Listelenen depremzedeleri ekrana yazdýr
    rows = cursor.fetchall()
    for row in rows:
         print(row)
    depremzede_id = int(input("Silmek istediðiniz depremzede kaydýnýn ID'sini girin: "))

    # Silme iþlemi
    cursor.execute("SELECT * FROM depremzedeler WHERE id = ?", (depremzede_id,))
    kayit = cursor.fetchone()
    if kayit:
        cursor.execute("DELETE FROM depremzedeler WHERE id = ?", (depremzede_id,))
        # Silinen kaydý baþka bir tabloya aktarma iþlemi
        cursor.execute("INSERT INTO gönderilen_depremzedeler VALUES (?, ?, ?, ?, ?)", kayit)
        print("Depremzede kaydý silindi ve gönderilen_depremzedeler tablosuna aktarýldý.")
    else:
        print("Girilen ID'ye sahip bir depremzede kaydý bulunamadý.")
    # Ýþlemleri kaydet ve baðlantýyý kapat
    conn.commit()
    conn.close()

# Ana döngü

while True:
  print("1.Görevli Giriþi")
  print("2.Depremzedeler Ýçin Yardým Talebi")
  print("3.Çýkýþ")
  secim1=int(input("Lütfen bir iþlem seçiniz: "))  
  if secim1==1:
    secim = input("Seçiminizi yapýn (1-5):\n"
                  "1. Kullanýcý Kaydet\n"
                  "2. Kullanýcý Giriþi\n"
                  "3. Þifre Sýfýrlama\n"
                  "4. Admin Giriþi\n"
                  "5.Çýkýþ\n")

    if secim == "1":
        kullanici_adi = input("Kullanýcý adý: ")
        sifre = input("Þifre: ")
        sifre2 = input("Þifreyi tekrar giriniz: ")
        if sifre == sifre2:
            tc_kimlik = input("TC Kimlik Numarasý: ")
            kullanici_kaydet(kullanici_adi, sifre, tc_kimlik)
            
        else:
            print("Þifreler uyuþmuyor. Lütfen tekrar deneyin.")
    elif secim == "2":
        tc_kimlik = input("TC Kimlik Numarasý: ")
        if len(tc_kimlik) != 11:
            print("Geçersiz TC kimlik numarasý. TC kimlik numarasý 11 haneli olmalýdýr.")
        else:
            sifre=input("sifre: ")
            cursor.execute("SELECT * FROM gorevliler WHERE tc_kimlik = ? AND sifre= ?", (tc_kimlik,sifre))
            user = cursor.fetchone()
            if user:
                print("Kullanýcý giriþi baþarýlý.")
                depremzede_yardim_gönder()
            else:
                print("Geçersiz TC kimlik numarasý. Lütfen tekrar deneyin.") 
    elif secim == "3":
        tc_kimlik = input("TC Kimlik Numarasý: ")
        sifre_sifirla(tc_kimlik)
    elif secim == "4":
         admin()
    elif secim == "5":
        print("çýkýlýyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
  elif secim1==2:
       menü()
  elif secim1==3:
       print("çýkýlýyor...")
       break
  else:
       print("Hatalý deðer girdiniz!")
       continue


