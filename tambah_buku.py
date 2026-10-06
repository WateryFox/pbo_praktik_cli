import csv
import os
from models import Buku


def simpan_buku():
    print("\n=== TAMBAH DATA BUKU ===")

    judul = input("Judul   : ").strip()
    penulis = input("Penulis : ").strip()
    isbn = input("ISBN    : ").strip()

    if not judul or not penulis or not isbn:
        print("\n[PERINGATAN] Semua kolom harus diisi!\n")
        return

    buku = Buku(judul, penulis, isbn)

    file_exists = os.path.exists("buku.csv")

    with open("buku.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Judul", "Penulis", "ISBN", "Status"])

        writer.writerow(buku.to_list())

    print("\n[BERHASIL] Buku berhasil ditambahkan.\n")


def main():
    while True:
        print("=== MENU TAMBAH BUKU ===")
        print("1. Tambah Buku")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            simpan_buku()

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.\n")


if __name__ == "__main__":
    main()