# Nama     :Hendra Aditya Pratama
# Kelas    :XI-TKJ 2
# No Absen :13
# Soal     :Membuat program yang mengambil mengambil data penjualan bulanan produk dan menentukan kategori produk berdasarkan penjualan.

data_penjualan = float(input("Masukkan data penjualan bulanan produk :"))

if data_penjualan > 1000:
    print("Produk Terlaris")
elif  500 <= data_penjualan <= 1000:
    print("Produk Populer")
else:
    print("Produk Biasa")