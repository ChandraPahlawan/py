print("Chandra Adha Rezki Pahlawan")
print("NIM:2309106011")
print("Izin BPOM")
print()

# Dictionary untuk menyimpan data pengguna
users = {
    "admin": "admin11",
    "nabilsaragih": "sepuh"
}

# Dictionary untuk menyimpan izin BPOM
izin_bpom = {}

# registrasi
def register():
    username = input("Masukkan nama pengguna: ")
    password = input("Masukkan kata sandi: ")
    users[username] = password
    print("Registrasi berhasil!")

# login
def login():
    username = input("Nama pengguna: ")
    password = input("Kata sandi: ")
    if username in users and users[username] == password:
        return True
    return False

# nampilin produk yang telah berizin
def display_izin():
    print("\nDaftar Izin BPOM:")
    for i, (nama, nomor_izin) in enumerate(izin_bpom.items(), 1):
        print(f"{i}. Nama: {nama}, Nomor Izin: {nomor_izin}")

# Fungsi untuk menambahkan izin BPOM
def create_izin():
    nama = input("Nama Produk: ")
    nomor_izin = input("Nomor Izin: ")
    izin_bpom[nama] = nomor_izin
    print("Izin BPOM telah ditambahkan.")

# memperbarui izin BPOM
def update_izin():
    display_izin()
    try:
        choice = int(input("Pilih nomor izin yang ingin diperbarui: "))
        izin_list = list(izin_bpom.items())
        if 1 <= choice <= len(izin_list):
            nama, nomor_izin = izin_list[choice - 1]
            print("Data Izin BPOM yang akan diperbarui:")
            print(f"Nama: {nama}, Nomor Izin: {nomor_izin}")
            new_nama = input("Nama baru (kosongkan jika tidak ingin mengubah): ")
            new_nomor_izin = input("Nomor izin produk: ")

            if new_nama:
                del izin_bpom[nama]
                izin_bpom[new_nama] = nomor_izin
            if new_nomor_izin:
                izin_bpom[nama] = new_nomor_izin
            print("Izin BPOM telah diperbarui.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Masukan harus berupa nomor.")

# menghapus izin BPOM
def delete_izin():
    display_izin()
    try:
        choice = int(input("Pilih nomor izin yang ingin dihapus: "))
        izin_list = list(izin_bpom.items())
        if 1 <= choice <= len(izin_list):
            nama, _ = izin_list[choice - 1]
            del izin_bpom[nama]
            print("Izin BPOM telah dihapus.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Masukan harus berupa nomor.")

while True:
    print("\nSelamat datang di Aplikasi Izin BPOM")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")
    choice = input("Pilih opsi: ")

    if choice == "1":
        if login():
            while True:
                print("\nMenu:")
                print("1. Tampilkan Izin BPOM")
                print("2. Tambah Izin BPOM")
                print("3. Perbarui Izin BPOM")
                print("4. Hapus Izin BPOM")
                print("5. Logout")
                sub_choice = input("Pilih opsi: ")

                if sub_choice == "1":
                    display_izin()
                elif sub_choice == "2":
                    create_izin()
                elif sub_choice == "3":
                    update_izin()
                elif sub_choice == "4":
                    delete_izin()
                elif sub_choice == "5":
                    break
                else:
                    print("Salah, pilihan tidak ada.")
        else:
            print("Login gagal. Coba lagi atau registrasi.")
    elif choice == "2":
        register()
    elif choice == "3":
        print("Terima kasih.")
        break
    else:
        print("Opsi tidak valid. Silakan pilih 1, 2, atau 3.")
