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
