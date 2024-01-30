def tambah_absensi(nama, status):
    with open('absensi.txt', 'a') as file:
        file.write(f'{nama},{status}\n')

def tampilkan_absensi():
    with open('absensi.txt', 'r') as file:
        print("Daftar Absensi:")
        print("Nama\t\tStatus")
        print("----------------------")
        for line in file:
            nama, status = line.strip().split(';')
            print(f'{nama}\t\t{status}')

# Contoh penggunaan
while True:
    print("\nAction:")
    print("1. Tambah Absensi")
    print("2. Tampilkan Daftar Absensi")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == '1':
        nama = input("Masukkan nama: ")
        status = input("Masukkan status (Hadir/Absen): ")
        tambah_absensi(nama, status)
    elif pilihan == '2':
        tampilkan_absensi()
    elif pilihan == '3':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")