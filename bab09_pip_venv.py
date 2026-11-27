# Bab 9: PIP dan Virtual Environments
import sys
import requests

print("=== Verifikasi Virtual Environment & PIP ===")
print(f"Path Python Aktif : {sys.executable}")
print(f"Versi Requests    : {requests.__version__}")

respons = requests.get("https://api.github.com", timeout=10)
print(f"Status HTTP GitHub: {respons.status_code} (OK)")
