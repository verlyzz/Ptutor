print("selamat datang di dupan")
nama = input("masukan nama : ")
umur = input("masukan umur : ")
print("halo dek", nama, "selamat datang di dupan")

daftar_wahana = ["1. roller coater RP. 15.000", "2. rumah hantu RP. 20.000", "3. bianglala RP. 10.000", "4. kora-kora RP. 10.000"]
harga = 0
for wahana in daftar_wahana :
    print(wahana)

pilihan = int(input("pilih nomor wahana : "))
if pilihan == 1 :
    print("tiket RP. 17.000")
    harga += "17.000"
elif pilihan == 2 :
    print("tiket RP. 22.000")
    harga += "24.000"
elif pilihan == 3 :
    print("tiket RP. 12.000")
    harga += "12.000"
elif pilihan == 4 :
    print("tiket RP. 12.000")
    harga += "12.000"
print("total harga wahana adalah ", harga)
print(daftar_wahana)