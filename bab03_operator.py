# Bab 3: Operator pada Python

a = 15
b = 4

# 1. Operator Aritmatika
print("=== 1. Operator Aritmatika ===")
print(f"{a} + {b}  = {a + b}")    # Penjumlahan
print(f"{a} - {b}  = {a - b}")    # Pengurangan
print(f"{a} * {b}  = {a * b}")    # Perkalian
print(f"{a} / {b}  = {a / b}")    # Pembagian float
print(f"{a} // {b} = {a // b}")   # Pembagian bulat (floor division)
print(f"{a} % {b}  = {a % b}")    # Modulus (sisa bagi)
print(f"{a} ** {b} = {a ** b}")   # Pemangkatan

# 2. Operator Penugasan (Assignment)
print("\n=== 2. Operator Penugasan ===")
nilai = 10
nilai += 5
print(f"Setelah nilai += 5 : {nilai}")
nilai *= 2
print(f"Setelah nilai *= 2 : {nilai}")

# 3. Operator Perbandingan
print("\n=== 3. Operator Perbandingan ===")
print(f"{a} == {b} : {a == b}")
print(f"{a} != {b} : {a != b}")
print(f"{a} > {b}  : {a > b}")
print(f"{a} <= {b} : {a <= b}")

# 4. Operator Logika
print("\n=== 4. Operator Logika ===")
lulus_teori = True
lulus_praktik = False
print(f"and (keduanya wajib True) : {lulus_teori and lulus_praktik}")
print(f"or  (salah satu True)     : {lulus_teori or lulus_praktik}")
print(f"not (kebalikan nilai)     : {not lulus_praktik}")
