# Nama     :Hendra Aditya Pratama
# Kelas    :XI-TKJ 2
# No Absen :13
# Soal     :Membuat program yang mengambil informasi pembaruan perangkat lunak dan menentukan apakah sistem perlu direstart.


persiapan = input("Apakah proyek dapat diluncurkan? (Siap/Tunda): ").strip().lower()

if persiapan == "siap":
    print("Proyek diluncurkan.")
elif persiapan == "tunda":
    print("Proyek ditunda.")
