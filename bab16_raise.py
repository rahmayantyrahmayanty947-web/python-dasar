def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif")
    return umur

print(cek_umur(16))

try:
    cek_umur(-1)
except ValueError as e:
    print("Error:", e)