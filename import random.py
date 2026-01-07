import random

# 1. Temel Sınıf: Cihaz (Device)
class Cihaz:
    """Akıllı ortamdaki genel bir cihazı temsil eder."""
    def __init__(self, cihaz_id, isim, durum="Kapalı"):
        self.cihaz_id = cihaz_id
        self.isim = isim
        self.durum = durum  # "Açık" veya "Kapalı"

    def durumu_goster(self):
        """Cihazın mevcut durumunu yazdırır."""
        print(f"Cihaz ID: {self.cihaz_id}, İsim: {self.isim}, Durum: **{self.durum}**")

    def ac(self):
        """Cihazı açar."""
        if self.durum == "Kapalı":
            self.durum = "Açık"
            print(f"-> {self.isim} açıldı.")

    def kapat(self):
        """Cihazı kapatır."""
        if self.durum == "Açık":
            self.durum = "Kapalı"
            print(f"-> {self.isim} kapatıldı.")

# 2. Türetilmiş Sınıf: Sensör (Sensor)
class Sensor(Cihaz):
    """Ortam verilerini okuyan bir sensörü temsil eder."""
    def __init__(self, cihaz_id, isim, birim):
        super().__init__(cihaz_id, isim, durum="Açık") # Sensörler genellikle hep açıktır
        self.birim = birim
        self.son_okuma = None

    def veri_oku(self):
        """Rastgele bir simüle edilmiş veri okuması yapar."""
        if self.isim == "Sıcaklık Sensörü":
            self.son_okuma = random.uniform(20.0, 30.0) # 20.0 ile 30.0 arası sıcaklık
        elif self.isim == "Işık Sensörü":
            self.son_okuma = random.randint(0, 1000) # Lüks birimi
        else:
            self.son_okuma = None
            
        print(f"**{self.isim}** okuması: {self.son_okuma:.2f} {self.birim}")
        return self.son_okuma

# 3. Ortam Sınıfı: Ortam (Environment)
class Ortam:
    """Akıllı ortamı ve içerdiği cihazları yönetir."""
    def __init__(self, ad):
        self.ad = ad
        self.cihazlar = {} # Cihaz ID'si anahtar, Cihaz nesnesi değer

    def cihaz_ekle(self, cihaz):
        """Ortama yeni bir cihaz ekler."""
        self.cihazlar[cihaz.cihaz_id] = cihaz
        print(f"\n[Ortam] {cihaz.isim} ({cihaz.cihaz_id}) ortama eklendi.")

    def tum_durumlari_goster(self):
        """Tüm cihazların durumlarını listeler."""
        print(f"\n--- {self.ad} Ortam Durumu ---")
        for cihaz in self.cihazlar.values():
            cihaz.durumu_goster()
        print("---------------------------------")
        
    def kural_calistir(self):
        """Sensör verilerine göre cihazları kontrol eden bir kuralı simüle eder."""
        print("\n--- KURAL YÜRÜTÜLÜYOR: Otomatik Sıcaklık Kontrolü ---")
        
        sicaklik_sensoru = self.cihazlar.get("S1")
        klima = self.cihazlar.get("A1")

        if isinstance(sicaklik_sensoru, Sensor) and isinstance(klima, Cihaz):
            okuma = sicaklik_sensoru.veri_oku()

            if okuma > 25.0:
                print(f"[KURAL] Sıcaklık ({okuma:.2f}C) 25C'nin üzerinde. Klimayı açıyorum.")
                klima.ac()
            elif okuma < 22.0:
                print(f"[KURAL] Sıcaklık ({okuma:.2f}C) 22C'nin altında. Klimayı kapatıyorum.")
                klima.kapat()
            else:
                print(f"[KURAL] Sıcaklık ({okuma:.2f}C) ideal aralıkta (22C-25C). Klima durumu korunuyor.")
        else:
            print("[KURAL HATASI] Gerekli sensörler veya cihazlar bulunamadı (S1 veya A1).")

# 4. Uygulama: Simülasyonu Başlatma
if __name__ == "__main__":
    
    # 1. Ortam oluşturma
    akilli_ev = Ortam("Akıllı Çalışma Odası")

    # 2. Cihazları oluşturma
    sicaklik_sensoru = Sensor("S1", "Sıcaklık Sensörü", "C")
    isik_sensoru = Sensor("S2", "Işık Sensörü", "Lüks")
    akilli_lamba = Cihaz("L1", "Akıllı Lamba")
    klima = Cihaz("A1", "Klima")

    # 3. Cihazları ortama ekleme
    akilli_ev.cihaz_ekle(sicaklik_sensoru)
    akilli_ev.cihaz_ekle(isik_sensoru)
    akilli_ev.cihaz_ekle(akilli_lamba)
    akilli_ev.cihaz_ekle(klima)

    # 4. Başlangıç durumu
    akilli_ev.tum_durumlari_goster()

    # 5. Kuralı bir kez çalıştır (Sıcaklık kontrolü)
    akilli_ev.kural_calistir()

    # 6. Son durumu göster
    akilli_ev.tum_durumlari_goster()
    
    # 7. Bir ışık sensörü okuması yapalım
    print("\n--- Manuel İşlem: Işık Sensörü Okuma ---")
    isik_sensoru.veri_oku()
    
    # 8. Lambayı manuel açalım
    print("\n--- Manuel İşlem: Lambayı Açma ---")
    akilli_lamba.ac()
    akilli_ev.tum_durumlari_goster()