menu = {"seblak": 12000, "bakso": 10000, "es teh": 4000}

for nama, harga in menu.items():
    print(nama, ":", harga)

for nama in menu:
    print("Menu:", nama)

print(list(menu.keys()))
print(sum(menu.values()))