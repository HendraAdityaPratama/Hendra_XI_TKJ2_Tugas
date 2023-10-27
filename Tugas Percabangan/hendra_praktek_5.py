# Nama     :Hendra Aditya Pratama
# Kelas    :XI-TKJ 2
# No Absen :13
# Soal     :Membuat program untuk menentukan nilai akhir siswa berdasarkan nilai tugas dan ujian.

nilai_tugas = float(input("Masukkan nilai tugas (skala 0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian (skala 0-100): "))

if nilai_tugas > 70 and nilai_ujian > 60:
    status = "Lulus"
else:
    status = "Gagal"

print("Nilai Tugas:", nilai_tugas)
print("Nilai Ujian:", nilai_ujian)
print("status:", status)
