
from  BankSampah import BankSampah
from dataWarga import Warga

def menu():
    bank = BankSampah()

    while True:
        print("\n=== BANK SAMPAH ===")
        print("1. Tambah Warga")
        print("2. Tampilkan Warga")
        print("3. Cari Warga")
        print("4. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            id_warga = input("ID: ")
            nama = input("Nama: ")
            telepon = input("Telepon: ")
            

            warga = Warga(id_warga, nama, telepon)
            bank.tambah_warga(warga)

        elif pilihan == "2":
            bank.tampilkan_warga()

        elif pilihan == "3":
            id_warga = input("Masukkan ID: ")
            bank.cari_warga(id_warga)

        elif pilihan == "4":
            break

if __name__ == "__main__":
    menu()