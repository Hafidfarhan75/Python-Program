cari = 5
a = [1,3,4,5,7]
posisi = 0
iterasi = 0
akhir = len(a) - 1
found = False
while posisi <= akhir and not found:
    posisi = (posisi+akhir)//2
    iterasi+=1
    if a[posisi] < cari:
        position = posisi + 1
    elif a[posisi] > cari:
        akhir = posisi - 1
    else :
        found = True

if found:
    print("ditemukan angka",iterasi,"pada indeks",posisi)
    print("Banyak iterasi : ",iterasi )
else :
    print("indeks angka",iterasi,"tidak ditemukan dalam list")
    print("iterasi : ",iterasi )