for i in range(1, 25) :
    for j in range(1, 61) :
        print("---" , j)
    print(i)

for i in range(1, 6) :
    print(i)
    for j in range (1, 4) :
        print(i , "x" , j , "=" , int(i * j))

kumpulanbarang = [ ["meja", "kursi", "tatakan"], ["monitor", "tv", "handphone"] ]
for barang in kumpulanbarang :
    for item in barang :
        print(item, end=",")
    print()