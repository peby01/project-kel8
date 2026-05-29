import json
from dataWarga import Warga


def import_data_warga(bank):
    try:
        with open("dokumen_data_warga.json", "r", encoding="utf-8") as file:
            data_warga = json.load(file)

        
        for data in data_warga:
            id_warga = data["id"]
            nama = data["nama"]
            telepon = data["telepon"]

            warga = Warga(id_warga, nama, telepon)

            if "poin" in data:
                warga.poin = data["poin"]

            bank.data_warga[id_warga] = warga

            if id_warga not in bank.urutan_tambah:
                bank.urutan_tambah.append(id_warga)

            print(f"ID      : {warga.id}")
            print(f"Nama    : {warga.nama}")
            print(f"Telepon : {warga.telepon}")
            print(f"Poin    : {warga.poin}")
            print("-" * 30)

        print("Data warga berhasil diimport dan sudah bisa diakses dari program.")

    except FileNotFoundError:
        print("File dokumen_data_warga.json tidak ditemukan.")

    except json.JSONDecodeError:
        print("Format file JSON salah.")

    except KeyError:
        print("Data JSON harus memiliki id, nama, dan telepon.")