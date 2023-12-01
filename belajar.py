print("LATIHAN 1")
angka = int(input("Masukan sebuah angka :"))
if angka < 10:
    print("Angka yang Anda masukkan 10 atau kurang.")
else:
    print("Angka yang Anda masukkan lebih besar dari 10.")


print("LATIHAN 2")
angka = int(input("Masukan sebuah angka :"))
if angka < 0:
    print("bilangan negatif")
elif angka > 0:
    print("bilangan positif")
else:
    print("bilangan nol")


print("LATIHAN 3")
total = int(input("Total belanja : "))
if total >= 100000:
    print("Anda mendapatkan diskon 10%")
    diskon = total * 0.10
    hargasetelahdiskon = total - diskon
    print("Anda hanya membayar", hargasetelahdiskon)
else:
    print("Anda tidak mendapatkan diskon :3")


print("LATIHAN 4")
i_nilai = int(input('nilai anda: '))

if i_nilai >= 100:
    print("Nilai tidak boleh lebih dari 100")
elif i_nilai >= 90:
    print("grade A")
elif i_nilai >= 80:
    print("grade B")
elif i_nilai >= 70:
    print("grade C")
elif i_nilai >= 60:
    print("grade D")
elif i_nilai < 0:
    print("Yang benar dong adik masukin nilainya")
else :
    print("grade E")
