print("SOAL 3")
umur = int(input("masukan umur anda : "))
status_anda = input("masukan status anda : ")

status = "pelajar"
status2 = "anggota klub film"

if umur < 18 :
    if (status_anda == status or status2):
        print("anda memenuhi syarat untuk mendapatkan diskon pelajar")
    else :
        print("anda tidak memenuhi syarat untuk mendapatkan diskon pelajar")
else :
        print("anda tidak memenuhi syarat untuk mendapatkan diskon pelajar")