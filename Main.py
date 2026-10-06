import subprocess


def buka_tambah_buku():
    subprocess.run(["python", "tambah_buku.py"])


def buka_tampil_buku():
    subprocess.run(["python", "tampil_buku.py"])


def menu_utama():
    while True:
        print("\n" + "=" * 40)
        print(" SISTEM PERPUSTAKAAN ".center(40, "="))
        print("=" * 40)
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("0. Keluar")
        print("=" * 40)

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            buka_tambah_buku()

        elif pilihan == "2":
            buka_tampil_buku()

        elif pilihan == "0":
            print("Terima kasih.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    menu_utama()