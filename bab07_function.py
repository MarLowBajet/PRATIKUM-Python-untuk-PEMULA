# Bab 7: Function pada Python

# 1. Fungsi tanpa parameter dan tanpa return
def tampilkan_header():
    print("=== Praktikum Bab 7: Function pada Python ===")

# 2. Fungsi dengan parameter wajib dan parameter default
def sapa_peserta(nama, modul="Python untuk Pemula"):
    print(f"Halo, {nama}! Selamat mengerjakan modul {modul}.")

# 3. Fungsi dengan nilai kembalian (return)
def hitung_nilai_akhir(tugas, uts, uas):
    skor = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    return round(skor, 2)

# 4. Fungsi dengan jumlah argumen dinamis (*args)
def hitung_rata_rata(*nilai_list):
    if not nilai_list:
        return 0
    return round(sum(nilai_list) / len(nilai_list), 2)

# Eksekusi fungsi
tampilkan_header()
sapa_peserta("MarLowBajet")

nilai_akhir = hitung_nilai_akhir(88, 82, 90)
print(f"Nilai Akhir Mata Kuliah : {nilai_akhir}")

rata_rata = hitung_rata_rata(85, 90, 78, 92, 88)
print(f"Rata-rata 5 Kuis        : {rata_rata}")
