# Nama     :Hendra Aditya Pratama
# Kelas    :XI-TKJ 2
# No Absen :13
# Soal     :Membuat program yang mengambil total belanjaan dan status anggota (biasa atau premium).

total_belanjaan = float(input("Masukkan total harga belanjaan :"))
status_anggota = input("Apa status anggota anda (premium/biasa) :")

if status_anggota == "premium":
    if total_belanjaan > 500000:
        diskon = 0.15
    else:
        diskon = 0.10
elif status_anggota == "biasa":
    if total_belanjaan > 300000:
        diskon = 0.07
    else:
        diskon = 0

total_diskon = total_belanjaan - (total_belanjaan * diskon)

print('Total belanjaan setelah diskon :', total_diskon)