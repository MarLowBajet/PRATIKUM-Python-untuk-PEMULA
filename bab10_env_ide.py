# Bab 10: Konfigurasi Environment dan IDE
import os
import sys

print("=== Verifikasi Konfigurasi Environment & IDE ===")
print(f"Direktori Kerja : {os.getcwd()}")
print(f"Interpreter     : {sys.executable}")
print(f"Mode Lingkungan : {os.getenv('APP_ENV', 'development')}")
print(f"Nama Sistem     : {os.name}")
