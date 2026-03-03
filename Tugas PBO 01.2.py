class Buku:
    def __init__(self, id_buku, judul, penulis):
        self.id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.status = "Tersedia"

    def ubah_status(self, status):
        self.status = status

    def info_buku(self):
        print(f"ID: {self.id_buku}")
        print(f"judul {self.judul}")
        print(f"penulis {self.penulis}")
        print(f"status {self.status}")

class Anggota:
    def __init__(self, id_anggota, nama, alamat, no_hp):
        self.id_anggota = id_anggota
        self.nama = nama
        self.alamat = alamat
        self.no_hp = no_hp

    def info_anggota(self):
        print(f"ID: {self.id_anggota}")
        print(f"Nama {self.nama}")
        print(f"Alamat {self.alamat}")
        print(f"No_hp {self.no_hp}")
    
class Peminjaman:
    def __init__(self, id_peminjaman, anggota, buku, tanggal_pinjam):
        self.id_peminjaman = id_peminjaman
        self.anggota = anggota
        self.buku = buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = None

    def pinjam_buku(self):
        if self.buku.status == "Tersedia":
            self.buku.ubah_status("Dipinjam")
            print(f"\nBuku berhasil dipinjam.")
        else:
            print(f"\nBuku sedang tidak tersedia/dipinjam.")
    
    def kembalikan_buku(self, tanggal_kembali):
        if self.buku.status == "Dipinjam":
            self.tanggal_kembali = tanggal_kembali
            self.buku.ubah_status ("Tersedia")
            print(f"\nBuku berhasil dikembalikan.")
        else:
            print(f"\nBuku sudah tersedia.")

buku1 = Buku("B001", "Pemrograman Python", "Andi")
anggota1 = Anggota("A001", "Zura", "Jl.Soebrantas", "081189093742")

peminjaman1 = Peminjaman("P001", anggota1, buku1, "04-03-2026")

peminjaman1.pinjam_buku()
buku1.info_buku()

peminjaman1.kembalikan_buku("10-03-2026")
buku1.info_buku()