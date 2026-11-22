profil = {"nama": "Rahmayanti", "panggilan": "Rahma", "kelas": "XI RPL B", "umur": 16}

print(profil)
print(profil["nama"])
print(profil.get("hobi"))

profil["hobi"] = "memasak"
profil["umur"] = 17
print(profil)

del profil["panggilan"]
print(profil)
print(len(profil))