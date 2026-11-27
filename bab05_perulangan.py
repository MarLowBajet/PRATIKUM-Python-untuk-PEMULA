# Bab 5: Perulangan pada Python (For dan While)

# 1. Perulangan For dengan range()
print("=== 1. Perulangan For dengan range() ===")
for i in range(1, 6):
    print(f"Iterasi ke-{i}")

# 2. Perulangan For pada daftar item
print("\n=== 2. Perulangan For pada Daftar Materi ===")
daftar_materi = ["Instalasi", "Variabel", "Operator", "If-Else", "Perulangan"]
for indeks, materi in enumerate(daftar_materi, start=1):
    print(f"{indeks}. {materi}")

# 3. Perulangan While dengan break dan continue
print("\n=== 3. Perulangan While (break & continue) ===")
angka = 0
while angka < 10:
    angka += 1
    if angka % 2 == 0:
        continue  # Lewati bilangan genap
    if angka > 7:
        break     # Hentikan perulangan jika lebih dari 7
    print(f"Bilangan ganjil ditemukan: {angka}")
