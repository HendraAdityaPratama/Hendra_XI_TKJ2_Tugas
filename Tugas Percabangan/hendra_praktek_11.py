# Nama     :Hendra Aditya Pratama
# Kelas    :XI-TKJ 2
# No Absen :13
# Soal     :Buat program Python yang mengambil nilai performa karyawandan menghitung bonus tahunan.

performa = int(input("Masukkan nilai performa karyawan (1-5): "))

gaji_tahunan = float(input("Masukkan gaji tahunan karyawan: "))

bonus = 0

if performa == 5:
    bonus = 0.20 * gaji_tahunan
elif performa == 4:
    bonus = 0.10 * gaji_tahunan
elif performa == 3:
    bonus = 0.05 * gaji_tahunan
elif performa == 2:
    bonus = 0.02 * gaji_tahunan

if bonus > 0:
    print(f"Bonus tahunan: Rp {bonus:.2f}")
else:
    print("Tidak ada bonus.")