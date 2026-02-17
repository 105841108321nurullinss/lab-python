"""
==========================================================
 TUGAS 1 - Sistem Perpustakaan
 Chapter 4: Object-Oriented Programming
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat class Buku dengan atribut: judul, penulis, tahun, isbn, tersedia
 2. Implementasikan __str__ dan __repr__ pada class Buku
 3. Buat class Perpustakaan dengan atribut: nama, daftar_buku
 4. Implementasikan method: tambah_buku, cari_buku (pencarian parsial),
    pinjam_buku (by isbn), kembalikan_buku (by isbn), tampilkan_semua
 5. Buat minimal 5 objek Buku dan demonstrasikan semua method

 Konsep yang dipelajari:
 - Membuat class dan __init__
 - Method __str__ dan __repr__
 - Atribut instance dan default value
 - Interaksi antar objek (Perpustakaan memiliki list Buku)
==========================================================
"""


class Buku:
    """Representasi sebuah buku di perpustakaan.

    Attributes:
        judul (str): Judul buku.
        penulis (str): Nama penulis buku.
        tahun (int): Tahun terbit buku.
        isbn (str): Nomor ISBN buku (unik).
        tersedia (bool): Status ketersediaan buku (default True).
    """

    def __init__(self, judul, penulis, tahun, isbn):
        """Inisialisasi objek Buku.

        Args:
            judul (str): Judul buku.
            penulis (str): Nama penulis.
            tahun (int): Tahun terbit.
            isbn (str): Nomor ISBN.
        """
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.isbn = isbn
        self.tersedia = True

    def __str__(self):
        """Representasi string yang mudah dibaca.

        Returns:
            str: Contoh -> "Python Dasar oleh John (2023) [Tersedia]"
        """
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.judul} oleh {self.penulis} ({self.tahun}) [{status}]"

    def __repr__(self):
        """Representasi resmi untuk debugging.

        Returns:
            str: Contoh -> "Buku('Python Dasar', 'John', 2023, '978-123')"
        """
        return f"Buku('{self.judul}', '{self.penulis}', {self.tahun}, '{self.isbn}')"


class Perpustakaan:
    """Sistem manajemen perpustakaan sederhana.

    Attributes:
        nama (str): Nama perpustakaan.
        daftar_buku (list): Koleksi objek Buku.
    """

    def __init__(self, nama):
        """Inisialisasi perpustakaan.

        Args:
            nama (str): Nama perpustakaan.
        """
        self.nama = nama
        self.daftar_buku = []

    def tambah_buku(self, buku):
        """Menambahkan buku ke koleksi perpustakaan.

        Args:
            buku (Buku): Objek Buku yang akan ditambahkan.
        """
        # Cek apakah ISBN sudah ada
        for b in self.daftar_buku:
            if b.isbn == buku.isbn:
                print(f"Buku dengan ISBN {buku.isbn} sudah ada!")
                return
        self.daftar_buku.append(buku)
        print(f"Buku '{buku.judul}' berhasil ditambahkan.")

    def cari_buku(self, kata_kunci):
        """Mencari buku berdasarkan kata kunci (pencarian parsial).

        Pencarian dilakukan pada judul dan penulis (case-insensitive).

        Args:
            kata_kunci (str): Kata kunci pencarian.

        Returns:
            list: Daftar objek Buku yang cocok.
        """
        hasil = [b for b in self.daftar_buku 
                 if kata_kunci.lower() in b.judul.lower() 
                 or kata_kunci.lower() in b.penulis.lower()]
        return hasil

    def pinjam_buku(self, isbn):
        """Meminjam buku berdasarkan ISBN.

        Args:
            isbn (str): Nomor ISBN buku yang akan dipinjam.

        Returns:
            str: Pesan berhasil/gagal meminjam.
        """
        for buku in self.daftar_buku:
            if buku.isbn == isbn:
                if buku.tersedia:
                    buku.tersedia = False
                    return f"Buku '{buku.judul}' berhasil dipinjam."
                else:
                    return f"Buku '{buku.judul}' sedang dipinjam."
        return f"Buku dengan ISBN {isbn} tidak ditemukan."

    def kembalikan_buku(self, isbn):
        """Mengembalikan buku berdasarkan ISBN.

        Args:
            isbn (str): Nomor ISBN buku yang akan dikembalikan.

        Returns:
            str: Pesan berhasil/gagal mengembalikan.
        """
        for buku in self.daftar_buku:
            if buku.isbn == isbn:
                if not buku.tersedia:
                    buku.tersedia = True
                    return f"Buku '{buku.judul}' berhasil dikembalikan."
                else:
                    return f"Buku '{buku.judul}' tidak sedang dipinjam."
        return f"Buku dengan ISBN {isbn} tidak ditemukan."

    def tampilkan_semua(self):
        """Menampilkan semua buku dalam format tabel.

        Contoh output:
        ============================================================
        No | Judul               | Penulis        | Tahun | Status
        ------------------------------------------------------------
         1 | Python Dasar        | John Doe       |  2023 | Tersedia
         2 | Data Science        | Jane Smith     |  2022 | Dipinjam
        ============================================================
        """
        print(f"\n{'=' * 75}")
        print(f"{'PERPUSTAKAAN ' + self.nama.upper():^75}")
        print(f"{'=' * 75}")
        print(f"{'No':>2} | {'Judul':<25} | {'Penulis':<18} | {'Tahun':>5} | {'Status'}")
        print("-" * 75)
        
        tersedia_count = 0
        dipinjam_count = 0
        
        for i, b in enumerate(self.daftar_buku, 1):
            status = "Tersedia" if b.tersedia else "Dipinjam"
            print(f"{i:>2} | {b.judul:<25} | {b.penulis:<18} | {b.tahun:>5} | {status}")
            if b.tersedia:
                tersedia_count += 1
            else:
                dipinjam_count += 1
        
        print("=" * 75)
        print(f"Total: {len(self.daftar_buku)} buku | Tersedia: {tersedia_count} | Dipinjam: {dipinjam_count}")


# ── Demonstrasi ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Buat minimal 5 objek Buku
    buku1 = Buku("Algoritma & Pemrograman", "Rinaldi Munir", 2016, "978-001")
    buku2 = Buku("Basis Data", "Fathansyah", 2018, "978-002")
    buku3 = Buku("Machine Learning", "Tom Mitchell", 2020, "978-003")
    buku4 = Buku("Python untuk Data Science", "Jake VanderPlas", 2019, "978-004")
    buku5 = Buku("Artificial Intelligence", "Stuart Russell", 2021, "978-005")

    # Buat objek Perpustakaan
    perpus = Perpustakaan("Unismuh Makassar")

    # Tambahkan semua buku ke perpustakaan
    print("=== TAMBAH BUKU ===")
    for buku in [buku1, buku2, buku3, buku4, buku5]:
        perpus.tambah_buku(buku)

    # Tampilkan semua buku
    perpus.tampilkan_semua()

    # Cari buku
    print("\n=== CARI BUKU: 'python' ===")
    hasil = perpus.cari_buku("python")
    for buku in hasil:
        print(f"  - {buku}")

    # Pinjam buku
    print("\n=== PINJAM BUKU ===")
    print(perpus.pinjam_buku("978-001"))
    print(perpus.pinjam_buku("978-002"))
    print(perpus.pinjam_buku("978-001"))  # coba pinjam lagi (sudah dipinjam)

    # Tampilkan setelah peminjaman
    perpus.tampilkan_semua()

    # Kembalikan buku
    print("\n=== KEMBALIKAN BUKU ===")
    print(perpus.kembalikan_buku("978-001"))

    # Tampilkan setelah pengembalian
    perpus.tampilkan_semua()

    # Test __repr__
    print("\n=== REPR ===")
    print(repr(buku1))
