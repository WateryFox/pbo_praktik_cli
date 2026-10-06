class Buku:

    def __init__(self, judul, penulis, isbn, status="Tersedia"):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn
        self.status = status

    def to_list(self):
        return [self.judul, self.penulis, self.isbn, self.status]

    def __str__(self):
        return f"{self.judul} oleh {self.penulis} (ISBN: {self.isbn}) - {self.status}"


class Anggota:

    def __init__(self, id_anggota, nama, kelas, no_hp):
        self.id = id_anggota
        self.nama = nama
        self.kelas = kelas
        self.no_hp = no_hp

    def to_list(self):
        return [self.id, self.nama, self.kelas, self.no_hp]

    def __str__(self):
        return f"{self.nama} ({self.id}) - Kelas {self.kelas}"