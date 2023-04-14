while True:
    print("1.Görevli Girişi")
    print("2.Depremzedeler İçin Yardım Talebi")
    print("3.Çıkış")
    
    secim=int(input("Lütfen bir işlem seçiniz: "))
    
    if secim==1:
        dogru_bilgi=True
        if dogru_bilgi:
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
                     print("Üyeliğiniz Başarıyla oluşturulmuştur.")
                     
                 else:
                     print("Şifreler eşleşmemektedir.Tekrar deneyiniz")
                     continue
             elif secim == 2:
                 kullanici_adi = input("Kullanıcı adınızı girin: ")
                 sifre = input("Şifrenizi girin: ")
                 if dogru_bilgi:
                     print("giriş başarılı")
                     # Veritabanından kullanıcı bilgileri kontrol edilir
             elif secim == 3:
                 kullanici_adi = input("Kullanıcı adınızı girin: ")
                     # Veritabanından kullanıcı bilgileri kontrol edilir
                 if dogru_bilgi:
                     print("yeni şifreniz 123")
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
        