# Bab 4: Kondisi If, Elif, dan Else pada Python

nilai_ujian = 84
kehadiran = 90

print("=== Evaluasi Kelulusan Mata Kuliah ===")
print(f"Nilai Ujian : {nilai_ujian}")
print(f"Kehadiran   : {kehadiran}%\n")

# 1. Percabangan if - elif - else untuk menentukan grade
if nilai_ujian >= 85:
    grade = "A"
elif nilai_ujian >= 75:
    grade = "B"
elif nilai_ujian >= 65:
    grade = "C"
elif nilai_ujian >= 50:
    grade = "D"
else:
    grade = "E"

print(f"Predikat Nilai : {grade}")

# 2. Nested If (Kondisi Bersarang) untuk status kelulusan
if kehadiran >= 75:
    if grade in ["A", "B", "C"]:
        print("Status         : LULUS")
    else:
        print("Status         : TIDAK LULUS (Nilai di bawah standar)")
else:
    print("Status         : TIDAK LULUS (Kehadiran kurang dari 75%)")
