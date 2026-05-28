import json
from  BankSampah import BankSampah
from dataWarga import Warga

def menu():
    bank = BankSampah()
    jalan = True

    while jalan:
        print("\n=== BANK SAMPAH ===")
        print("1. Tambah Warga")
        print("2. Cari Warga")
        print("3. import data warga")
        print("4. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            id_warga = input("ID: ")
            nama = input("Nama: ")
            telepon = input("Telepon: ")
            
            warga = Warga(
                id_warga, 
                nama,
                telepon
            )

            bank.tambah_warga(warga)

        elif pilihan == "2":
            
            while jalan:
                

                print("\n=== CARI WARGA ===")
                print("1. Tampilkan semua")
                print("2. Cari nama")
                print("3. Terbaru")
                print("4. A-Z")
                print("5. Berdasarkan poin")
                print("6. Kembali")

                pilihan = input("Masukan pilihan:")

                if pilihan == "1":
                    bank.tampilkan_warga()
                elif pilihan == "2":
                    nama = input("Nama: ")
                    bank.cari_nama_warga(nama)

                elif pilihan == "3": 
                    bank.tampil_terbaru()
                
                elif pilihan == "4":
                    bank.tampil_abjad()
                
                elif pilihan == "5":
                    bank.tampil_poin()
                
                elif pilihan == "6":
                    break

        
        elif pilihan == "3":

            pass
        elif pilihan == "4":

            jalan = False
            print("Terimakasih sudah memakai aplikasi layanan kami!")

        else:
            print("Pilihan tidak valid silahkan masukan angka dari 1-3!")
            continue

if __name__ == "__main__":
    menu()