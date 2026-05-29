class Transaksi:
    def __init__(self, id_transaksi, id_warga, nama_warga, jenis_sampah, berat, poin):
        self.id_transaksi = id_transaksi
        self.id_warga = id_warga
        self.nama_warga = nama_warga
        self.jenis_sampah = jenis_sampah
        self.berat = berat
        self.poin = poin

    def tampilkan(self):
        print(f"ID Transaksi : {self.id_transaksi}")
        print(f"ID Warga     : {self.id_warga}")
        print(f"Nama Warga   : {self.nama_warga}")
        print(f"Jenis Sampah : {self.jenis_sampah}")
        print(f"Berat        : {self.berat} kg")
        print(f"Poin         : {self.poin}")



class BankSampah:
    def __init__(self):
        self.data_warga = {}
        self.urutan_tambah = []
        self.data_transaksi = []
        self.jenis_sampah = ("Plastik", "Kertas", "Logam", "Kaca", "Organik")
        self.nomor_transaksi = 1
       
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
    

    # fungsi tambah transaksi sampah
    def tambah_transaksi_sampah(self):
        if len(self.data_warga) == 0:
            print("Belum ada data warga. Silakan import atau tambah warga dulu.")
            return

        id_warga = input("Masukkan ID warga: ")

        if id_warga not in self.data_warga:
            print("ID warga tidak ditemukan.")
            return

        print("\n=== Pilih Jenis Sampah ===")

        for i in range(len(self.jenis_sampah)):
            print(f"{i + 1}. {self.jenis_sampah[i]}")

        try:
            pilihan = int(input("Pilih jenis sampah: "))

            if pilihan < 1 or pilihan > len(self.jenis_sampah):
                print("Pilihan jenis sampah tidak valid.")
                return

            jenis = self.jenis_sampah[pilihan - 1]

            berat = float(input("Masukkan berat sampah kg: "))

            if berat <= 0:
                print("Berat sampah harus lebih dari 0.")
                return

        except ValueError:
            print("Input harus berupa angka.")
            return

        poin = int(berat * 10)
        warga = self.data_warga[id_warga]

        id_transaksi = "T" + str(self.nomor_transaksi).zfill(3)

        transaksi = Transaksi(
            id_transaksi,
            id_warga,
            warga.nama,
            jenis,
            berat,
            poin
        )

        self.data_transaksi.append(transaksi)
        self.nomor_transaksi += 1

        warga.poin += poin

        print("\nTransaksi sampah berhasil ditambahkan.")
        print(f"Nama warga   : {warga.nama}")
        print(f"Jenis sampah : {jenis}")
        print(f"Berat        : {berat} kg")
        print(f"Poin tambah  : {poin}")
        print(f"Total poin   : {warga.poin}")

        return

    def tampilkan_transaksi_sampah(self):
        if len(self.data_transaksi) == 0:
            print("Belum ada transaksi sampah.")
            return

        print("\n=== Riwayat Transaksi Sampah ===")

        for transaksi in self.data_transaksi:
            transaksi.tampilkan()
            print("-" * 30)