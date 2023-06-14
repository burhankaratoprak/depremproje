import sqlite3
import pandas as pd
conn = sqlite3.connect('veritaban�.db')
conn.execute('''CREATE TABLE IF NOT EXISTS depremzedeler
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                ad_soyad TEXT NOT NULL,
                konum TEXT NOT NULL,
                ihtiya� TEXT NOT NULL,
                ihtadet TEXT NOT NULL)''')

def yard�m_oku():
    dt = pd.read_csv("Erzakyard�m.csv", sep=';')
    df_filtered = dt[dt['adet'] > 0]
    print(df_filtered)
class kayit:
   def __init__(self, ad_soyad, konum, ihtiya�, ihtadet):

       self.ad_soyad = ad_soyad

       self.konum = konum

       self.ihtiya� = ihtiya�

       self.ihtadet = ihtadet
   def depremzedeleri_kaydet(self):
        conn.execute("INSERT INTO depremzedeler(ad_soyad, konum, ihtiya�, ihtadet) VALUES (?, ?, ?, ?)",
                     (self.ad_soyad, self.konum, self.ihtiya�, self.ihtadet))
        conn.commit()
        conn.close()
def men�():
    ad_soyad = input("Ad�n�z Soyad�n�z:")
    konum = input("Bulundu�unuz yerin ad� ve adresi:")
    yard�m_oku()
    sorgu="e"
    while sorgu.lower()=="e":
        ihtiya�=input("�htiya�lar�n�z� s�ras�yla virg�lle(,) ay�rarak yaz�n�z: \n")
        ihtadet=input("Ka� adet:\n")
        sorgu=input("Ba�ka ihtiyac�n�z varm�? EVET[E]/HAYIR[H]")
        deprem=kayit(ad_soyad, konum, ihtiya� , ihtadet)
        deprem.ihtiya� += ", " + ihtiya�
        deprem.ihtadet += ", " + ihtadet
    deprem.depremzedeleri_kaydet()

# SQLite veritaban�na ba�lan
con = sqlite3.connect('gorev_yonetim.db')
cursor = con.cursor()
# G�revliler tablosunu olu�tur
cursor.execute('''CREATE TABLE IF NOT EXISTS gorevliler (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tc_kimlik TEXT,
                    kullanici_adi TEXT,
                    sifre TEXT
                )''')
def main_menu():
    while True:
      print("1.G�revli Giri�i")
      print("2.Depremzedeler ��in Yard�m Talebi")
      print("3.��k��")
      secim1=int(input("L�tfen bir i�lem se�iniz: "))  
      if secim1==1:
        secim = input("Se�iminizi yap�n (1-5):\n"
                      "1. Kullan�c� Kaydet\n"
                      "2. Kullan�c� Giri�i\n"
                      "3. �ifre S�f�rlama\n"
                      "4. Admin Giri�i\n"
                      "5.��k��\n")
    
        if secim == "1":
            kullanici_adi = input("Kullan�c� ad�: ")
            sifre = input("�ifre: ")
            sifre2 = input("�ifreyi tekrar giriniz: ")
            if sifre == sifre2:
                tc_kimlik = input("TC Kimlik Numaras�: ")
                kullanici_kaydet(kullanici_adi, sifre, tc_kimlik)
                
            else:
                print("�ifreler uyu�muyor. L�tfen tekrar deneyin.")
        elif secim == "2":
            tc_kimlik = input("TC Kimlik Numaras�: ")
            if len(tc_kimlik) != 11:
                print("Ge�ersiz TC kimlik numaras�. TC kimlik numaras� 11 haneli olmal�d�r.")
            else:
                sifre=input("sifre: ")
                cursor.execute("SELECT * FROM gorevliler WHERE tc_kimlik = ? AND sifre= ?", (tc_kimlik,sifre))
                user = cursor.fetchone()
                if user:
                    print("Kullan�c� giri�i ba�ar�l�.")
                    depremzede_yardim_g�nder()
                else:
                    print("Ge�ersiz TC kimlik numaras�. L�tfen tekrar deneyin.") 
        elif secim == "3":
            tc_kimlik = input("TC Kimlik Numaras�: ")
            sifre_sifirla(tc_kimlik)
        elif secim == "4":
             admin()
        elif secim == "5":
            print("��k�l�yor...")
            break
        else:
            print("Ge�ersiz se�im. L�tfen tekrar deneyin.")
      elif secim1==2:
          
           break
      elif secim1==3:
           print("��k�l�yor...")
           break
      else:
           print("Hatal� de�er girdiniz!")
           continue
    con.close()
# Kullan�c� kaydetme fonksiyonu
def kullanici_kaydet(kullanici_adi, sifre,tc_kimlik):
    if len(tc_kimlik) != 11:
        print("Ge�ersiz TC kimlik numaras�. TC kimlik numaras� 11 haneli olmal�d�r.")
        return

    cursor.execute("SELECT * FROM gorevliler WHERE tc_kimlik = ?", (tc_kimlik,))
    user = cursor.fetchone()
    if user:
        print("Bu TC kimlik numaras� zaten kay�tl�. L�tfen farkl� bir TC kimlik numaras� deneyin.")
        return

    cursor.execute("INSERT INTO gorevliler (kullanici_adi, sifre, tc_kimlik) VALUES (?, ?, ?)",
                   (kullanici_adi, sifre, tc_kimlik))
    
    print("KUllan�c� Bilgileri Ba�ar�yla kaydedildi")
    con.commit()
    
# Kullan�c� giri�i kontrol fonksiyonu
def kullanici_giris(tc_kimlik, sifre):
    if len(tc_kimlik) != 11:
        print("Ge�ersiz TC kimlik numaras�. TC kimlik numaras� 11 haneli olmal�d�r.")
        return

    cursor.execute("SELECT * FROM gorevliler WHERE tc_kimlik = ?", (tc_kimlik))
    user = cursor.fetchone()
    if user:
        print("Kullan�c� giri�i ba�ar�l�.")
    else:
        print("Ge�ersiz TC kimlik numaras�. L�tfen tekrar deneyin.")
def kullanici_listele():
    cursor.execute("SELECT * FROM gorevliler")
    users = cursor.fetchall()
    for user in users:
        print("Kullan�c� Ad�:", user[2])
        print("TC Kimlik Numaras�:", user[1])
        print("----------------------")
# �ifre s�f�rlama fonksiyonu
def sifre_sifirla(tc_kimlik):
    if len(tc_kimlik) != 11:
        print("Ge�ersiz TC kimlik numaras�. TC kimlik numaras� 11 haneli olmal�d�r.")
        return
    cursor.execute("SELECT * FROM gorevliler WHERE tc_kimlik = ?", (tc_kimlik,))
    user = cursor.fetchone()
    if user:
        yeni_sifre = input("Yeni �ifreyi girin: ")
        cursor.execute("UPDATE gorevliler SET sifre = ? WHERE tc_kimlik = ?", (yeni_sifre, tc_kimlik,))
        con.commit()
        print("�ifre ba�ar�yla s�f�rland�.")
    else:
        print("Ge�ersiz TC kimlik numaras� veya �ifre. L�tfen tekrar deneyin.")
def kullanici_sil(tc_kimlik):
    cursor.execute("SELECT * FROM gorevliler WHERE tc_kimlik = ?", (tc_kimlik,))
    user = cursor.fetchone()
    if user:
        cursor.execute("DELETE FROM gorevliler WHERE tc_kimlik = ?", (tc_kimlik,))
        con.commit()
        print("Kullan�c� ba�ar�yla silindi.")
    else:
        print("Ge�ersiz TC kimlik numaras�. L�tfen tekrar deneyin.")
        
kullanicilar = [
    {"kullanici_adi": "admin", "sifre": "admin", "yetki": "admin"},
]
def admin():
    kullanici_adi = input("Kullan�c� ad�n�z� girin: ")
    sifre = input("�ifrenizi girin: ")
    for kullanici in kullanicilar:
     if kullanici["kullanici_adi"] == kullanici_adi and kullanici["sifre"] == sifre:
      if kullanici["yetki"] == "admin":
        print("Admin giri�i ba�ar�l�.")
        while True:
            print("\nAdmin Paneli:")
            print("1. Kullan�c�lar� Listele")
            print("2. Kullan�c� Sil")
            print("3.Yard�m G�nderilen bilgileri")
            print("4.��k��")
        
            secim = input("Se�iminizi yap�n (1-4): ")
        
            if secim == "1":
                kullanici_listele()
            elif secim == "2":
                tc_kimlik = input("TC Kimlik Numaras�: ")
                kullanici_sil(tc_kimlik)
            elif secim == "3":
                 conn = sqlite3.connect('veritaban�.db')
                 cursor = conn.cursor()
                 cursor.execute("SELECT * FROM g�nderilen_depremzedeler")
                 # Listelenen depremzedeleri ekrana yazd�r
                 rows = cursor.fetchall()
                 for row in rows:
                      print(row)
            elif secim == "4":
                print("Admin panelinden ��k�l�yor...")
                break
            else:
                print("Ge�ersiz se�im. L�tfen tekrar deneyin.")
def depremzede_yardim_g�nder():
    conn = sqlite3.connect('veritaban�.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS g�nderilen_depremzedeler (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       ad_soyad TEXT NOT NULL,
       konum TEXT NOT NULL,
       ihtiya� TEXT NOT NULL,
       ihtadet TEXT NOT NULL
    )
    """)
    # Depremzedeleri listele
    cursor.execute("SELECT * FROM depremzedeler")
    # Listelenen depremzedeleri ekrana yazd�r
    rows = cursor.fetchall()
    for row in rows:
         print(row)
    depremzede_id = int(input("Silmek istedi�iniz depremzede kayd�n�n ID'sini girin: "))

    # Silme i�lemi
    cursor.execute("SELECT * FROM depremzedeler WHERE id = ?", (depremzede_id,))
    kayit = cursor.fetchone()
    if kayit:
        cursor.execute("DELETE FROM depremzedeler WHERE id = ?", (depremzede_id,))
        # Silinen kayd� ba�ka bir tabloya aktarma i�lemi
        cursor.execute("INSERT INTO g�nderilen_depremzedeler VALUES (?, ?, ?, ?, ?)", kayit)
        print("Depremzede kayd� silindi ve g�nderilen_depremzedeler tablosuna aktar�ld�.")
    else:
        print("Girilen ID'ye sahip bir depremzede kayd� bulunamad�.")
    # ��lemleri kaydet ve ba�lant�y� kapat
    conn.commit()
    conn.close()

# Ana d�ng�

while True:
  print("1.G�revli Giri�i")
  print("2.Depremzedeler ��in Yard�m Talebi")
  print("3.��k��")
  secim1=int(input("L�tfen bir i�lem se�iniz: "))  
  if secim1==1:
    secim = input("Se�iminizi yap�n (1-5):\n"
                  "1. Kullan�c� Kaydet\n"
                  "2. Kullan�c� Giri�i\n"
                  "3. �ifre S�f�rlama\n"
                  "4. Admin Giri�i\n"
                  "5.��k��\n")

    if secim == "1":
        kullanici_adi = input("Kullan�c� ad�: ")
        sifre = input("�ifre: ")
        sifre2 = input("�ifreyi tekrar giriniz: ")
        if sifre == sifre2:
            tc_kimlik = input("TC Kimlik Numaras�: ")
            kullanici_kaydet(kullanici_adi, sifre, tc_kimlik)
            
        else:
            print("�ifreler uyu�muyor. L�tfen tekrar deneyin.")
    elif secim == "2":
        tc_kimlik = input("TC Kimlik Numaras�: ")
        if len(tc_kimlik) != 11:
            print("Ge�ersiz TC kimlik numaras�. TC kimlik numaras� 11 haneli olmal�d�r.")
        else:
            sifre=input("sifre: ")
            cursor.execute("SELECT * FROM gorevliler WHERE tc_kimlik = ? AND sifre= ?", (tc_kimlik,sifre))
            user = cursor.fetchone()
            if user:
                print("Kullan�c� giri�i ba�ar�l�.")
                depremzede_yardim_g�nder()
            else:
                print("Ge�ersiz TC kimlik numaras�. L�tfen tekrar deneyin.") 
    elif secim == "3":
        tc_kimlik = input("TC Kimlik Numaras�: ")
        sifre_sifirla(tc_kimlik)
    elif secim == "4":
         admin()
    elif secim == "5":
        print("��k�l�yor...")
        break
    else:
        print("Ge�ersiz se�im. L�tfen tekrar deneyin.")
  elif secim1==2:
       men�()
  elif secim1==3:
       print("��k�l�yor...")
       break
  else:
       print("Hatal� de�er girdiniz!")
       continue


