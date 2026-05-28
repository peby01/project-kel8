#nyicil progress
#bikin class warga
class Warga:
    def __init__(self, id_warga, nama, telepon):
        self.id = id_warga
        self.nama = nama
        self.telepon = telepon
        self.poin = 0

    def tampilkan(self):
        print(f"ID      : {self.id}")
        print(f"Nama    : {self.nama}")
        print(f"Telepon : {self.telepon}")
        print(f"Poin    : {self.poin}")

#bikin class bank sampah
class BankSampah:
    def __init__(self):
        self.data_warga = {}

    def tambah_warga(self, warga):
        self.data_warga[warga.id] = warga

    def tampilkan_warga(self):
        for warga in self.data_warga.values():
            warga.tampilkan()
            print("-" * 20)
    
    def cari_warga(self, id_warga):
        if id_warga in self.data_warga:
            self.data_warga[id_warga].tampilkan()
        else:
            print("Warga tidak ditemukan")

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