class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.status = "Tersedia"
    def info(self):
        print(f"judul : {self.judul}")
        print(f"penulis : {self.penulis}")
        print(f"status : {self.status}")

class Anggota:
    def __init__(self, nama):
        self.nama = nama
        self.buku_dipinjam = None
    def info(self):
        pinjam = self.buku_dipinjam.judul if self.buku_dipinjam else "-"
        print(f"Nama = {self.nama}")
        print(f"Dipinjam = {pinjam}")

class Peminjaman:
    def __init__(self, buku, anggota, tgl_kembali):
        self.buku = buku
        self.anggota = anggota
        self.tgl_kembali = tgl_kembali
        self.status = "Aktif"

    def info(self):
        print(f"Buku = {self.buku.judul}")
        print(f"Peminjam = {self.anggota.nama}")
        print(f"Kembali = {self.tgl_kembali}")
        print(f"Status = {self.status}")

    def selesaikan(self):
        self.status = "Selesai"

class Perpustakaan:
    def __init__(self,nama):
        self.nama = nama
        self.buku = []
        self.anggota = []
        self.pinjaman = []
        
    def tambah_buku(self, buku):
        self.buku.append(buku)
        print(f"[+] Buku '{buku.judul}' ditambahkan.")
    
    def daftar_anggota(self, anggota):
        self.anggota.append(anggota)
        print(f"[+] Anggota '{anggota.nama}' didaftarkan.")

    def pinjam_buku(self, anggota, buku, tgl_kembali):
        if buku.status == "Dipinjam":
            print(f"[!] '{buku.judul}' sedang dipinjam orang lain")
            return
        buku_status = "Dipinjam"
        anggota.buku_dipinjam = buku
        p = Peminjaman(buku, anggota, tgl_kembali)
        self.pinjaman.append(p)
        print(f"'{anggota.nama}' meminjam '{buku.judul}'.")

    def kembalikan_buku(self, anggota):
        if anggota.buku_dipinjam is None:
            print(f" '{anggota.nama}' tidak sedang meminjam.")
            return
        judul = anggota.buku_dipinjam.judul
        anggota.buku_dipinjam.status = "Tersedia"
        anggota.buku_dipinjam = None
        print(f" '{judul}' berhasil dikembalikan.")

    def tampilkan_buku(self):
        print(f"\n=== Daftar Buku {self.nama} ====")
        for b in self.buku:
            b.info()

# program utama
perpus = Perpustakaan ("Perpustakaan Kampus")

# buat buku
buku1 = Buku ("Pemrograman Python Dasar", "Budi Santoso")
buku2 = Buku ("Sistem Operasi", "Rahayu Ningsih")

# tambah buku
print("\nTambah Buku")
perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)

# buat anggota
anggota1 = Anggota ("Fulan")
anggota2 = Anggota ("Fulani")

# tambah anggota
print("\nDaftar Anggota")
perpus.daftar_anggota(anggota1)
perpus.daftar_anggota(anggota2)

#pinjam buku
perpus.pinjam_buku(anggota1, buku1, "18 Februari 2026")
perpus.pinjam_buku(anggota2, buku2, "19 Februari 2026")

#jika meminjam buku yang sama
print("\nJika meminjam buku yang sama")
perpus.pinjam_buku(anggota2, buku1, "18 Februari 2026")

# tampilkan buku
perpus.pinjam_buku(anggota2, buku2, "19 Februari 2026")

# kembalikan buku
print("\nKembalikan Buku")
perpus.kembalikan_buku(anggota1)

# cek buku setelah dikembalikan
perpus.tampilkan_buku()