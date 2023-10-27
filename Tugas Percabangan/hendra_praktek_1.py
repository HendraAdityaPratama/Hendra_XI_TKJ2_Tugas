# Nama     :Hendra Aditya Pratama
# Kelas    :XI-TKJ 2
# No Absen :13
# Soal     :Ditoko online, Hitung diskon berdasarkan total belanjaan!


total_belanjaan = float(input('Masukkan total harga belanjaan: '))

if total_belanjaan > 500000:
    diskon = 0.10
elif 300000 <= total_belanjaan <= 500000:
    diskon = 0.05
else:
    diskon = 0

total_harga = total_belanjaan - (total_belanjaan * diskon)

print('Total harga belanjaan setelah diskon: ', total_harga)

