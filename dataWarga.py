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