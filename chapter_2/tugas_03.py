"""
==========================================================
 TUGAS 3 - Analisis Teks dengan Set
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Definisikan 2 string kalimat (minimal 10 kata per kalimat)
 2. Konversi setiap kalimat menjadi set kata unik (lowercase)
 3. Tampilkan intersection (kata di kedua kalimat)
 4. Tampilkan difference (kata hanya di kalimat 1 / kalimat 2)
 5. Tampilkan union (semua kata unik)
 6. Tampilkan symmetric difference (kata di salah satu saja)
 7. Hitung jumlah kata unik total
==========================================================
"""

# ── Data Kalimat ─────────────────────────────────────────────────────────────
kalimat_1 = "Python adalah bahasa pemrograman yang sangat populer untuk data science dan machine learning"
kalimat_2 = "Machine learning adalah cabang dari artificial intelligence yang sangat berkembang pesat saat ini"


# ── Konversi ke Set ──────────────────────────────────────────────────────────
kata_set_1 = set(kalimat_1.lower().split())
kata_set_2 = set(kalimat_2.lower().split())

print("===== ANALISIS TEKS DENGAN SET =====")
print(f"\nKalimat 1: {kalimat_1}")
print(f"Kalimat 2: {kalimat_2}")
print(f"\nSet kata kalimat 1: {kata_set_1}")
print(f"Set kata kalimat 2: {kata_set_2}")


# ── Intersection (kata yang muncul di KEDUA kalimat) ─────────────────────────
kata_sama = kata_set_1 & kata_set_2
print(f"\n===== INTERSECTION (kata di kedua kalimat) =====")
print(f"{kata_sama}")


# ── Difference (kata HANYA di kalimat 1) ─────────────────────────────────────
hanya_kalimat_1 = kata_set_1 - kata_set_2
print(f"\n===== DIFFERENCE (kata hanya di kalimat 1) =====")
print(f"{hanya_kalimat_1}")


# ── Difference (kata HANYA di kalimat 2) ─────────────────────────────────────
hanya_kalimat_2 = kata_set_2 - kata_set_1
print(f"\n===== DIFFERENCE (kata hanya di kalimat 2) =====")
print(f"{hanya_kalimat_2}")


# ── Union (SEMUA kata unik dari kedua kalimat) ──────────────────────────────
semua_kata = kata_set_1 | kata_set_2
print(f"\n===== UNION (semua kata unik) =====")
print(f"{semua_kata}")


# ── Symmetric Difference (kata di SALAH SATU saja) ──────────────────────────
kata_unik_masing = kata_set_1 ^ kata_set_2
print(f"\n===== SYMMETRIC DIFFERENCE (kata di salah satu saja) =====")
print(f"{kata_unik_masing}")


# ── Tampilkan Hasil ──────────────────────────────────────────────────────────
print(f"\n===== RINGKASAN =====")
print(f"Jumlah kata unik kalimat 1 : {len(kata_set_1)}")
print(f"Jumlah kata unik kalimat 2 : {len(kata_set_2)}")
print(f"Jumlah kata sama           : {len(kata_sama)}")
print(f"Jumlah kata unik total     : {len(semua_kata)}")
