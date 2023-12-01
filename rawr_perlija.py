tahun_lahir = int(input("masukan tahun lahir anda :"))
tahun_sekarang = 2023
umur = tahun_sekarang - tahun_lahir
print("umur anda", umur)
if umur < 18:
    print("kamu masih dibawah umur")
else :
    print("anda sudah bisa membuat KTP")