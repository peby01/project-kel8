# ============================================================
#                         BANK SAMPAH
# ============================================================
# Judul Proyek:
# Simulasi Daur Ulang Sampah Berbasis Terminal

# Deskripsi:
# Program berbasis teks yang digunakan untuk mengelola proses
# penerimaan sampah dari warga, pencatatan jenis sampah,
# antrean penimbangan, pengelompokan sampah berdasarkan kategori,
# penentuan rute pengambilan sampah, hingga riwayat transaksi
# penukaran sampah menjadi poin.

# Sistem ini juga dapat mencari data warga, mengurutkan data
# transaksi, menyimpan data ke file, serta menampilkan struktur
# kategori sampah secara hierarki.

# ============================================================
#                      PENERAPAN MATERI
# ============================================================

# 1. Sorting
#    Mengurutkan data warga berdasarkan poin, berat sampah,
#    atau tanggal transaksi.

# 2. File Handler
#    Menyimpan dan membaca data warga, transaksi, dan kategori
#    sampah dari file .txt.

# 3. Searching
#    Mencari data warga berdasarkan ID, nama, atau nomor telepon.

# 4. Rekursif
#    Menampilkan kategori sampah dalam bentuk tree secara bertingkat.

# 5. List, Tuple, Set, dan Dictionary
#    - List       : Menyimpan data transaksi.
#    - Tuple      : Menyimpan data tetap seperti jenis sampah.
#    - Set        : Menyimpan kategori unik.
#    - Dictionary : Menyimpan data warga berdasarkan ID.

# 6. Stack dan Queue
#    - Queue : Antrean warga yang ingin menimbang sampah.
#    - Stack : Fitur undo transaksi terakhir.

# 7. OOP
#    Membuat class seperti Warga, Sampah, Transaksi, dan BankSampah.

# 8. Single Linked List
#    Menyimpan riwayat transaksi warga.
    
# 9. Double Linked List
#    Navigasi maju dan mundur data transaksi.

# 10. Circular Linked List
#     Rotasi petugas penjemput sampah.

# 11. Tree
#     Struktur kategori sampah.
#     Contoh: Organik -> Sisa Makanan -> Sayuran.

# 12. Graph
#     Menentukan rute pengambilan sampah antar lokasi warga.

# 13. Hash Table
#     Menyimpan dan mencari data warga dengan cepat menggunakan ID warga.


import json
from  BankSampah import BankSampah
from dataWarga import Warga
from Importdatawarga import import_data_warga

def menu():
    bank = BankSampah()
    jalan = True

    while jalan:
        print("1. Tambah Warga")
        print("2. Tampilkan / Cari Warga")
        print("3. Import Data Warga ")
        print("4. Tambah Transaksi Sampah")
        print("5. Tampilkan Riwayat Transaksi Sampah")
        print("0. Keluar")
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
            import_data_warga(bank)

            pass
        elif pilihan == "4":
            bank.tambah_transaksi_sampah()
            
        elif pilihan == "5":
            bank.tampilkan_transaksi_sampah()


        elif pilihan == "0":
            jalan = False
            print("Terimakasih sudah memakai aplikasi layanan kami!")
        else:
            print("Pilihan tidak valid.")
    
    

if __name__ == "__main__":
    menu()