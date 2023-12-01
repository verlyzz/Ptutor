print("SOAL 2")
umur = int(input("Masukan umur anda : "))
keanggotaan_aktif = input("apakah anda aktif berolahraga ( yes / no ) : ")

aktif = "yes"
tidak_aktif = "no"

if(umur >= 18) :
     if (keanggotaan_aktif == aktif) :
        print("selamat datang di klub olahraga kami")
     if (keanggotaan_aktif == tidak_aktif) :
        print("anda belum bisa masuk ke klub olahraga kami")
else :
    print("anda belum bisa masuk ke klub olahraga kami")