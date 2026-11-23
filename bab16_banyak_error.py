def hitung(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Pembagi tidak boleh nol")
    except TypeError:
        print("Nilai harus berupa angka")

print(hitung(36000, 3))
hitung(10, 0)
hitung("seblak", 2)