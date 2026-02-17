"""
==========================================================
 TUGAS 1 - Manajemen Nilai Mahasiswa
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat sebuah list berisi 10 nilai ujian (integer, range 0-100)
 2. Tampilkan: nilai tertinggi, terendah, rata-rata (hitung manual)
 3. Urutkan list dari terkecil ke terbesar
 4. Gunakan list comprehension untuk filter nilai >= 70 (lulus)
 5. Hitung jumlah mahasiswa lulus dan tidak lulus
 6. Tambahkan 2 nilai baru (append), hapus nilai terkecil (remove)
==========================================================
"""

# ── Data Nilai ────────────────────────────────────────────────────────────────
nilai = [85, 60, 92, 45, 78, 55, 90, 73, 68, 88]

print("===== MANAJEMEN NILAI MAHASISWA =====")
print(f"Nilai awal   : {nilai}")


# ── Statistik Dasar (hitung manual, tanpa library) ───────────────────────────
nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)
rata_rata = sum(nilai) / len(nilai)

print(f"Tertinggi    : {nilai_tertinggi}")
print(f"Terendah     : {nilai_terendah}")
print(f"Rata-rata    : {rata_rata}")


# ── Pengurutan ────────────────────────────────────────────────────────────────
nilai_sorted = sorted(nilai)
print(f"Nilai sorted : {nilai_sorted}")


# ── List Comprehension: Filter Nilai Lulus ────────────────────────────────────
nilai_lulus = [n for n in nilai if n >= 70]
print(f"Nilai lulus  : {nilai_lulus}")


# ── Hitung Lulus & Tidak Lulus ────────────────────────────────────────────────
jumlah_lulus = len(nilai_lulus)
jumlah_tidak_lulus = len(nilai) - jumlah_lulus
print(f"Lulus: {jumlah_lulus} | Tidak lulus: {jumlah_tidak_lulus}")


# ── Manipulasi List ──────────────────────────────────────────────────────────
nilai.append(95)
nilai.append(82)
print(f"\nSetelah append 95 dan 82: {nilai}")

nilai.remove(min(nilai))
print(f"Setelah remove terkecil : {nilai}")
