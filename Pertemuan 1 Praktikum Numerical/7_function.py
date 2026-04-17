def luas_segi3(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

#input user
alas = float(input("Masukkan alas: "))
tinggi = float(input("Masukkan tinggi: "))

#panggil fungsi
luas = luas_segi3(alas, tinggi)
print("Luas segitiga: %.3f" %(luas))