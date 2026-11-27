# Bab 2: Variabel dan Tipe Data pada Python

# 1. Tipe Data String (teks)
nama_mahasiswa = "MarLowBajet"
mata_kuliah = 'Pemrograman Dasar Python'

# 2. Tipe Data Integer (bilangan bulat)
semester = 1
jumlah_sks = 3

# 3. Tipe Data Float (bilangan desimal)
ipk_target = 3.95

# 4. Tipe Data Boolean (True / False)
status_aktif = True

# Menampilkan nilai beserta tipe datanya menggunakan fungsi type()
print("=== Data Mahasiswa ===")
print(f"Nama        : {nama_mahasiswa} -> {type(nama_mahasiswa)}")
print(f"Mata Kuliah : {mata_kuliah} -> {type(mata_kuliah)}")
print(f"Semester    : {semester} -> {type(semester)}")
print(f"Jumlah SKS  : {jumlah_sks} -> {type(jumlah_sks)}")
print(f"Target IPK  : {ipk_target} -> {type(ipk_target)}")
print(f"Status Aktif: {status_aktif} -> {type(status_aktif)}")

# 5. Type Casting (Konversi Tipe Data)
teks_angka = "2026"
tahun = int(teks_angka)
print(f"\nHasil casting '{teks_angka}' menjadi integer: {tahun} -> {type(tahun)}")
