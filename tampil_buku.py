import csv
import os
from models import Buku


def muat_data():
    daftar_buku = []

    if not os.path.exists("buku.csv"):
        print("File buku.csv tidak ditemukan.")
        return daftar_buku

    with open("buku.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # Lewati header

        for row in reader:
            buku = Buku(
                judul=row[0],
                penulis=row[1],
                isbn=row[2],
                status=row[3]
            )
            daftar_buku.append(buku)

    return daftar_buku


def tampilkan_buku():
    daftar_buku = muat_data()

    if not daftar_buku:
        print("Tidak ada data buku.")
        return

    print("\n=== DAFTAR BUKU PERPUSTAKAAN ===\n")

    print(f"{'Judul':25}{'Penulis':20}{'ISBN':20}{'Status'}")
    print("-" * 75)

    for buku in daftar_buku:
        print(
            f"{buku.judul:25}"
            f"{buku.penulis:20}"
            f"{buku.isbn:20}"
            f"{buku.status}"
        )

    print("-" * 75)
    print(f"Total Buku: {len(daftar_buku)}")


def main():
    while True:
        print("\n=== MENU ===")
        print("1. Tampilkan Buku")
        print("2. Refresh Data")
        print("0. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            tampilkan_buku()

        elif pilihan == "2":
            print("Data dimuat ulang...")
            tampilkan_buku()

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()