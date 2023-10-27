# Nama     :Hendra Aditya Pratama
# Kelas    :XI-TKJ 2
# No Absen :13
# Soal     :Membuat ketentuan waktu projek akan selesai tepat waktu atau terlambat

estimasi_selesai = (input("Masukkan waktu estimasi selesai (tahun-bulan-tanggal): "))
target_selesai = (input("Masukkan waktu target selesai (tahun-bulan-tanggal) : "))

if estimasi_selesai <= target_selesai:
    print("Tepat waktu")
else:
    print("Terlambat")
