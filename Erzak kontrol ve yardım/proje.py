kullanicilar = [
    {"kullanici_adi": "admin", "sifre": "admin", "yetki": "admin"},
    {"kullanici_adi": "görevli1", "sifre": "123456", "yetki": "Görevli1"},
]

while True:
    print("1.Görevli Girişi")
    print("2.Depremzedeler İçin Yardım Talebi")
    print("3.Çıkış")
    
    secim=int(input("Lütfen bir işlem seçiniz: "))
    
    if secim==1:
        
         while True:
             print("1.Sisteme Üye Ol")
             print("2.Sisteme Giriş Yap")
             print("3.Şifremi Unuttum")
             print("4.Önceki Menüye Dön")
             
             secim=int(input("Lütfe Bir İşlem Seçiniz"))
             
             if secim==1:
                 #üye ol
                 kullanici_adi=input("Kullanıcı adınızı girin:")
                 sifre = input("Şifrenizi girin: ")
                 sifre2=input("Şifrenizi tekrar girin:")
                 if sifre==sifre2:
                   kullanicilar.append({"kullanici_adi": kullanici_adi, "sifre": sifre, "yetki": "Görevli1"})
                   print("Üyeliğiniz Başarıyla oluşturulmuştur.")
                 else:
                     print("Şifreler eşleşmemektedir.Tekrar deneyiniz")
                     continue
             elif secim == 2:
                 kullanici_adi = input("Kullanıcı adınızı girin: ")
                 sifre = input("Şifrenizi girin: ")
                 for kullanici in kullanicilar:
                  if kullanici["kullanici_adi"] == kullanici_adi and kullanici["sifre"] == sifre:
                   if kullanici["yetki"] == "admin":
                     print("Admin girişi başarılı.")
                     while True:
                         print("1. Depremzedeleri Listele")
                         print("2. Depremzedelere Yardım  Gönder")
                         print("3. Çıkış")
                         secim=int(input("Lütfen bir işlem seçiniz:"))
                         if secim==1:
                             print("Depremzedeler Listeleniyor...")
                         elif secim == 2:
                                  print("Depremzedelere yardım gönderiliyor...")
                                  # Yardım talepleri kabul edilip depremzedelere yardım gönderilir.
                         elif secim == 3:
                                  print("Çıkış yapılıyor...")
                                  break
                         else:
                            print("Geçersiz işlem seçimi. Lütfen tekrar deneyin.")
                  elif kullanici["yetki"] == "Görevli1":
                   print("Kullanıcı girişi başarılı.")
                   # Kullanıcıya özel işlemler yapılabilir
                  break
                 else:
                  print("Hatalı kullanıcı adı veya şifre. Lütfen tekrar deneyin.")
             elif secim == 3:
                 kullanici_adi = input("Kullanıcı adınızı girin: ")
                 for kullanici in kullanicilar:
                     if kullanici["kullanici_adi"] == kullanici_adi:
                     # Veritabanından kullanıcı bilgileri kontrol edilir
                      print("yeni şifreniz 123")
                      break
                      # Kullanıcının şifresi yenilenebilir
             elif secim == 4:
                 break
             else:
                 print("Geçersiz işlem seçimi. Lütfen tekrar deneyin.")
    elif secim ==2:
        ad_soyad=input("Adınız Soyadınız:")
        konum= input("Bulunduğunuz yerin adı ve adresi:")
        
    elif secim ==3:
        print("Çıkış yapılıyor...")
        break
    
    else:
        print("Geçersiz işlem seçimi.Lütfen tekrar deneyin.")
        
