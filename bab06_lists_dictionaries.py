# Bab 6: Lists dan Dictionaries pada Python

# 1. Operasi Dasar List
print("=== 1. Operasi List ===")
bahasa = ["Python", "JavaScript", "C++"]
print(f"List awal          : {bahasa}")

bahasa.append("Go")              # Menambah elemen di akhir
bahasa.insert(1, "Rust")         # Menyisipkan elemen pada indeks ke-1
bahasa.remove("C++")             # Menghapus elemen tertentu
print(f"Setelah modifikasi : {bahasa}")
print(f"Elemen pertama     : {bahasa[0]}")
print(f"Dua elemen terakhir: {bahasa[-2:]}")

# 2. Operasi Dasar Dictionary
print("\n=== 2. Operasi Dictionary ===")
mahasiswa = {
    "username": "MarLowBajet",
    "mata_kuliah": "Python untuk Pemula",
    "bab_selesai": 5,
    "aktif": True
}

# Mengubah & menambah pasangan key-value
mahasiswa["bab_selesai"] = 6
mahasiswa["repositori"] = "PRATIKUM-Python-untuk-PEMULA"

for kunci, nilai in mahasiswa.items():
    print(f"{kunci:<13}: {nilai}")
