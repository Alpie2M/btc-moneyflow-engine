import hashlib

mesaj = "Orhun'un ilk Bitcoin hash testi !"

hash_sonucu = hashlib.sha256(mesaj.encode()).hexdigest()

print("Girdi:", mesaj)
print("SHA-256:", hash_sonucu)
