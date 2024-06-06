# -*- coding: utf-8 -*-
"""pemvis pt6

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z49kKxTYe_C5dJ80UuU1dOyV0githL-s

Pemrograman dengan Melibatkan Operator Aritmatika, Operator
Logika, Operator Komparasi, Kondisi dan Perulangan

latihan set
"""

def tampilkan_menu():
    print("Menu:")
    print("1. Tambah makanan")
    print("2. Update makanan")
    print("3. Hapus makanan")
    print("4. Tampilkan makanan")
    print("5. Keluar")

makanan = set()

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        makanan_baru = input("Masukkan nama makanan baru: ")
        makanan.add(makanan_baru)
        print(f"Makanan {makanan_baru} telah ditambahkan.")

    elif pilihan == "2":
        makanan_lama = input("Masukkan nama makanan yang ingin diupdate: ")
        makanan_baru = input("Masukkan nama makanan baru: ")
        if makanan_lama in makanan:
            makanan.remove(makanan_lama)
            makanan.add(makanan_baru)
            print(f"Makanan {makanan_lama} telah diupdate menjadi {makanan_baru}.")
        else:
            print(f"Makanan {makanan_lama} tidak ditemukan.")

    elif pilihan == "3":
        makanan_hapus = input("Masukkan nama makanan yang ingin dihapus: ")
        if makanan_hapus in makanan:
            makanan.remove(makanan_hapus)
            print(f"Makanan {makanan_hapus} telah dihapus.")
        else:
            print(f"Makanan {makanan_hapus} tidak ditemukan.")

    elif pilihan == "4":
        print("Daftar makanan:")
        for m in makanan:
            print(m)

    elif pilihan == "5":
        print("Terima kasih")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")

"""latihan boolean"""

print("A dan B")
t = bool(True)
f = bool(False)
print("apakah A lebih besar dari B?")
print(t)
print("----------------------------------------------------")

print("Apakah B lebih besar dari A?")
t = bool(True)
f = bool(False)
print(f)
print("----------------------------------------------------")

print("Apakah A sama dengan B?")
t = bool(True)
f = bool(False)
print(f)
print("----------------------------------------------------")

ppn_a = 0
ppn_b = 0

harga = 15000

if harga > 10000:
    ppn_a = harga * 0.12

if harga > 50000:
    ppn_b = harga * 0.12

ppn_total = ppn_a + ppn_b

print("Hitung PPN A dan B:")
print("PPN A:", ppn_a)
print("PPN B:", ppn_b)
print("Total PPN:", ppn_total)
print("----------------------------------------------------")

print("Cek PPN:")
print(ppn_total > 0)  # True jika ada PPN, False jika tidak
print("----------------------------------------------------")

del ppn_a, ppn_b

# Setelah variabel a dan b dihapus, cek apakah mereka benar-benar tidak ada
try:
    print("Cek A dan B setelah dihapus:")
    print(a, b)
except NameError:
    print("Variabel a dan b sudah dihapus.")
print("----------------------------------------------------")

"""P1 kondisi dan komparasi
p1.1 tentukan sub judul
"""

#case: menentukan warna pixel berdasarkan posisi pixel dengan kondisi dan komparasi

#masukkan posisi pixel pada layar (nomor baris)
pixel_row = 100

rowmax = int(1079)
batas1 = int(0.5*rowmax)

print("batas1: ", batas1)
print("Posisi pixel berada pada baris ke-", pixel_row)

if pixel_row < batas1:
  print("warnai pixel merah.")
if pixel_row == batas1:
  print("warnai pixel hitam.")
if pixel_row > batas1:
  print("warnai pixel putih.")
if pixel_row <= batas1:
  print("warnai pixel kuning.")
if pixel_row > batas1:
  print("warnai pixel ungu.")

"""pt1.2. tentukan sub judul"""

#masukkan posisi pixel pada layar (nomor baris)
pixel_row = 300

rowmax = int(1079)
batas1 = int(0.2*rowmax)
batas2 = int(0.4*rowmax)
batas3 = int(0.6*rowmax)
batas4 = int(0.8*rowmax)

print("batas1:",batas1)
print("batas2:",batas2)
print("batas3:",batas1)
print("batas4:",batas4)
print("rowmax:",rowmax)

print("posisi pixel berada pada baris ke-", pixel_row)

if (pixel_row >= 0 and pixel_row < batas1):
  print("warnai pixel merah.")
if (pixel_row >= batas1 and pixel_row < batas2):
  print("warnai pixel hijau.")
if (pixel_row >= batas2 and pixel_row < batas3):
  print("warnai pixel biru.")
if (pixel_row >= batas3 and pixel_row < batas4):
  print("warnai pixel kuning.")
if (pixel_row >= batas4 and pixel_row < rowmax):
  print("warnai pixel ungu.")

"""P2 kondisi, loop, komparasi dan logika"""

print("\833c")
import numpy as np
import matplotlib.pyplot as plt

rowmax = int(1879)
colmax = int(1919)

radius_max = int(1000)
batas1 = int(0.2*radius_max)
batas2 = int(0.4*radius_max)
batas3 = int(0.6*radius_max)
batas4 = int(0.8*radius_max)

Gambar = np.zeros(shape=(rowmax+1, colmax+1, 3), dtype=np.int16)
for i in range(0, rowmax+1):
  for j in range(0, colmax+1):
    if (i**2+j**2) >= 0 and (i**2+j**2) < batas1**2:
      Gambar[i, j, 0] = 255
    if (i**2+j**2) >= batas1**2 and (i**2+j**2) < batas2**2:
      Gambar[i, j, 1] = 255
    if (i**2+j**2) >= batas2**2 and (i**2+j**2) < batas3**2:
      Gambar[i, j, 2] = 255
    if (i**2+j**2) >= batas3**2 and (i**2+j**2) < batas4**2:
      Gambar[i, j, 0] = 255
      Gambar[i, j, 1] = 255
    if (i**2+j**2) >= batas4**2 and (i**2+j**2) < radius_max**2:
      Gambar[i, j, 0] = 255
      Gambar[i, j, 2] = 255

plt.figure()
plt.imshow(Gambar)
plt.show()

"""P3 Latihan"""
