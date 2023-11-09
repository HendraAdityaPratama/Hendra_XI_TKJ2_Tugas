# Nama    = Hendra Aditya Pratama
# Kelas   = XI-TKJ2
# No      = 13
# Soal    = Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga
#           batas tertentu yang ditentukan pengguna.

def hitung_bilangan_ganjil_sebelum(angka):
    jumlah_ganjil = angka // 2
    return jumlah_ganjil

angka = int(input("Masukkan angka tertentu: "))
jumlah_ganjil_sebelum = hitung_bilangan_ganjil_sebelum(angka)
print(f"Jumlah bilangan ganjil sebelum {angka} adalah {jumlah_ganjil_sebelum}")