print("LATIHAN 3")
total = int(input("Total belanja : "))
if total >= 100000:
    print("acik dapet diskon 10%")
    diskon = total * 0.10
    hargasetelahdiskon = total - diskon
    print("Harga potongan diskon adalah", hargasetelahdiskon)
else:
    print("p pinjem seratus")



print("LATIHAN 4")
i_nilai = int(input('nilai anda: '))

if i_nilai >= 100:
    print("boonk y lu")
elif i_nilai >= 90:
    print("grade A")
elif i_nilai >= 80:
    print("grade B")
elif i_nilai >= 70:
    print("grade C")
elif i_nilai >= 60:
    print("grade D")
elif i_nilai < 0:
    print("bjir diluar nunung")
else :
    print("grade E")
