# Nama     :Hendra Aditya Pratama
# Kelas    :XI-TKJ 2
# No Absen :13
# Soal     :Membuat pemeriksaan apakah file sudah ada di direktory server.

nama_file = 'data.txt'
daftar_file_di_server = ['file1.txt', 'file2.txt', 'data.txt', 'file3.txt']

if nama_file in daftar_file_di_server:
    print('File sudah ada')
else:
    print('File belum ada')

