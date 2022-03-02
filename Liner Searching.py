cari = 7
a = [8,5,7,9,2]
posisi = 0
iterasi = 0
akhir = len(a) - 1
found = False
while posisi <= akhir and not found:
    iterasi+=1
    if a[posisi] == cari:
        found = True
    else: posisi = posisi + 1
if found:
    print("angka yang anda cari terletak pada indeks :",posisi)
    print("iterasi sebanyak = ",iterasi,"kali")
else:
    print("Nomor yang dicari tidak ditemukan")
    print("iterasi sebanyak = ",iterasi,"kali")