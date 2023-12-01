def menyapa (nama) :
    print("p wibu", nama)
    print("ingpokan rawr")

menyapa("jaki")

#tugas 1
def hitung (angka1, angka2, operator) :
    if(operator == "+") :
        return angka1 + angka2
    elif(operator == "-") :
        return angka1 - angka2
    elif(operator == "x") :
        return angka1 * angka2
    else :
        print("operator tidak valid")
print(hitung(5, 3, "+"))
print(hitung(5, 2, "-"))
print(hitung(5, 5, "x"))

#tugas 2
def perulangan (nama, perulangan) :
    for i in range(perulangan) :
        print(nama)
perulangan("p mabar", 1000000)