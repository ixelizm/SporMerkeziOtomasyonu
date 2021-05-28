class SporMerkezi:
    def __init__(self):
        self.Kursiyerler = []
        self.Kurslar= {
        "1000": "Yüzme Kursu",
        "1010": "Fitness Kursu",
        "1020": "Yoga Kursu",
        "1030": "Tekvando Kursu",
        "1040": "Judo Kursu",
        "1050": "Boks Kursu",
        "1060": "Pilates Kursu"
        }
        self.fiyat = 0
        self.kampanya = ""
        while True:
            mesaj = """
********* SporMerkezi Otomasyonu *********
1) Kursiyer Ekle
2) Kursiyer Listele
3) Kursiyer Sorgula
4) Kursiyer Sil
5) Kursiyer Ücret Hesapla
6) Çıkış
"""
            print(mesaj)
            try:
                secim = int(input("Yapacağınız İşlem: "))
            except:
                print("Lütfen Sadece Rakam Giriniz!")
                continue
            if secim < 0 or secim > 6:
                print("Lütfen 1-6 Arasında Seçim Yapın!")
                continue
            if secim == 1:
                self.KursiyerEkle()
            elif secim == 2:
                self.KursiyerListele()
            elif secim == 3:
                self.KursiyerAra()
            elif secim == 4:
                self.KursiyerSil()
            elif secim == 5:
                self.KursiyerUcretHesapla()
            elif secim == 6:
                self.Cikis()
    def KursiyerEkle(self):
        isim = input("Kursiyer İsmi: ")
        soyisim = input("Kursiyer Soyismi: ")
        yas = int(input("Kursiyer Yaşı: "))
        tekrar = int(input("Kaç Kurs Eklenecek: "))
        kurslar = []
        for x in range(tekrar):
            kursid = input("Kurs Numarasını Girin: ")
            try:
                kurslar.append(self.Kurslar[kursid])
            except:
                print("Belirtilen Kurs Bulunamadı!")
                return
        self.Kursiyerler.append({"ID": len(self.Kursiyerler) +100, "KursiyerAD": isim, "KursiyerSOYAD": soyisim, "KursiyerYAS": yas, "Kurslar": kurslar})
        print(f"{isim} {soyisim} Adlı Kursiyer Eklendi!")
    def KursiyerListele(self):
        metin = ""
        kurs = "    -"
        for kursiyer in self.Kursiyerler:
            kurs += "\n    -".join([x for x in kursiyer["Kurslar"]])
            metin += f'{kursiyer["ID"]}) {kursiyer["KursiyerAD"]} {kursiyer["KursiyerSOYAD"]} \n{kurs}\n'
            kurs = "    -"
        print(metin)
        
    def KursiyerAra(self):
        KursiyerID= int(input("Kursiyer Numarasını Girin: "))
        status = True
        metin = ""
        kurs = "    -"
        for kursiyer in self.Kursiyerler:
            if kursiyer["ID"] == KursiyerID:
                kurs += "\n    -".join([x for x in kursiyer["Kurslar"]])
                metin += f'{kursiyer["ID"]}) {kursiyer["KursiyerAD"]} {kursiyer["KursiyerSOYAD"]} \n{kurs}\n'
                status = False
                kurs = "    -"
        if status == False:
            print(metin)
        else:
            print("Kursiyer Bulunamadı!")
    def KursiyerSil(self):
        KursiyerID = int(input("Kursiyer Numarasını Girin: "))
        status = True
        for kursiyer in self.Kursiyerler:
            if kursiyer["ID"] == KursiyerID:
                isim = kursiyer["KursiyerAD"]
                self.Kursiyerler.remove(kursiyer)
                status = False
        if status == False:
            print(f"{isim} İsimli Kursiyer Silindi!")
        else:
            print(f"{KursiyerID} Numaralı Kursiyer Bulunamadı!")
    def KursiyerUcretHesapla(self):
        KursiyerID = int(input("Kursiyer Numarasını Girin: "))
        status = True
        for kursiyer in self.Kursiyerler:
            if kursiyer["ID"] == KursiyerID:
                say = len(kursiyer["Kurslar"])
                if say == 2:
                    self.fiyat = 100+ (100-100/100*15)
                    self.kampanya = "Kampanya 1'den Faydalanıyorsunuz!"
                elif say == 3:
                    self.fiyat = 100+ 100+(100-100/100*25)
                    self.kampanya = "Kampanya 2'den Faydalanıyorsunuz!"
                elif say > 3:
                    self.fiyat = (100-100/100*10)*say
                    self.kampanya = "Kampanya 3'den Faydalanıyorsunuz!"
                else:
                    self.fiyat = 100
                    self.kampanya = "Hiçbir Kampanyadan Faydalanamıyorsunuz!"
            status = False
        if status == False:
            print(self.fiyat, self.kampanya)
        else:
            print("Kursiyer Bulunamadı!")
    def Cikis(self):
        print("Programdan Çıkılıyor...")
        exit(1)
Otomasyon = SporMerkezi()
