# Bab 8: Class dan Object pada Python (OOP Dasar)

class Praktikan:
    # Atribut kelas (berlaku untuk semua objek)
    kelas = "Python untuk Pemula"

    # Konstruktor
    def __init__(self, username, bahasa_utama):
        self.username = username
        self.bahasa_utama = bahasa_utama
        self.bab_selesai = 0

    # Method untuk memperbarui progres
    def selesaikan_bab(self, jumlah):
        self.bab_selesai += jumlah
        print(f"[INFO] {self.username} menyelesaikan {jumlah} bab baru.")

    # Method untuk menampilkan status objek
    def tampilkan_profil(self):
        print(f"Username     : {self.username}")
        print(f"Kelas        : {self.kelas}")
        print(f"Bahasa Utama : {self.bahasa_utama}")
        print(f"Total Bab    : {self.bab_selesai} bab selesai\n")


# Instansiasi objek dari class Praktikan
peserta_1 = Praktikan("MarLowBajet", "Python")
peserta_1.selesaikan_bab(8)
peserta_1.tampilkan_profil()
