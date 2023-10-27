# Nama     :Hendra Aditya Pratama
# Kelas    :XI-TKJ 2
# No Absen :13
# Soal     :Buat program yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis pinjaman.

durasi_peminjaman = int (input("Masukkan durasi peminjaman buku (dalam hari): "))


if durasi_peminjaman <= 7:
    print("Peminjaman Pendek")
elif durasi_peminjaman <= 30:
    print("Peminjaman Menengah")
else:
    print("Peminjaman Panjang")

