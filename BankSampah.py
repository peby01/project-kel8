class BankSampah:
    def __init__(self):
        self.data_warga = {}
        self.urutan_tambah = []

    # kode fungsi tambah warga:   
    def tambah_warga(self, warga):
        
        for data in self.data_warga.values():
            
            #apakah nama sama?
            if data.nama.lower() == warga.nama.lower():

                print("Nama warga sudah terdaftar")
                print("Silahkan gunakan nama yang berbeda.")

                return
        
        self.data_warga[warga.id] = warga
        self.urutan_tambah.append(warga.id)

        print("Warga berhasil ditambahkan!")

    def tampilkan_warga(self):

        if len(self.data_warga) == 0:
            print("Belum ada warga yang terdaftar.")
            return 
        
        for data in self.data_warga.values():


            data.tampilkan()
            print("-" * 20)
    
    #cari nama warga lewat ketikan
    def cari_nama_warga(self, name):
        
        if len(self.data_warga) == 0:
            print("Belum ada warga yang terdaftar.")
            return 
    
        ketemu = False

        for warga in self.data_warga.values():

            if warga.nama.lower() == name.lower():

                warga.tampilkan()
                print("-" * 20)

                ketemu = True
            
        if not ketemu:
            print("Warga tidak ditemukan.")

    
    #Cari warga berdasarkan terbaru ke terlama
    def tampil_terbaru(self):


        if len(self.data_warga) == 0:
            print("Belum ada warga yang terdaftar.")
            return 
        
        for id_warga in reversed(self.urutan_tambah):

            self.data_warga[id_warga].tampilkan()

            print("-"* 20)
    
    #Cari warga berdasarkan huruf abjad A-Z

    def tampil_abjad(self):

        if len(self.data_warga) == 0:
            print("Belum ada warga.")
            return

        daftar_warga = list(
            self.data_warga.values()
        )

        for i in range(
            len(daftar_warga)
        ):

            for j in range(
                0,
                len(daftar_warga)-i-1
            ):

                if (
                    daftar_warga[j].nama.lower()
                    >
                    daftar_warga[j+1].nama.lower()
                ):

                    sementara = daftar_warga[j]

                    daftar_warga[j] = (
                        daftar_warga[j+1]
                    )

                    daftar_warga[j+1] = sementara

        for warga in daftar_warga:
            warga.tampilkan()
            print("-" * 20)

    def tampil_poin(self):

        if len(self.data_warga) == 0:
            print("Belum ada warga yang terdaftar.")
            return 
    
        # ambil semua data dari dictionary
        daftar_warga = list(
            self.data_warga.values()
        )

        # Bubble Sort manual
        for i in range(
            len(daftar_warga)
        ):

            for j in range(
                0,
                len(daftar_warga) - i - 1
            ):

                # kalau poin kiri lebih kecil,
                # tukar posisi
                if (
                    daftar_warga[j].poin < daftar_warga[j + 1].poin
                ):

                    sementara = daftar_warga[j]

                    daftar_warga[j] = (
                        daftar_warga[j + 1]
                    )

                    daftar_warga[j + 1] = sementara

        # tampilkan hasil
        for warga in daftar_warga:

            warga.tampilkan()
            print("-" * 20)
