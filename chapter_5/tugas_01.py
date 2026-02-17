"""
==========================================================
 TUGAS 1 - Analisis Statistik dengan NumPy
 Chapter 5: NumPy & Pandas
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat array 30 nilai mahasiswa (acak 40-100, seed=42)
 2. Hitung statistik dasar: mean, median, std, max/min
 3. Temukan indeks nilai tertinggi dan terendah (argmax/argmin)
 4. Hitung jumlah mahasiswa yang lulus (nilai >= 70)
 5. Lakukan normalisasi Min-Max (skala 0-1)
 6. Lakukan normalisasi Z-Score
 7. Reshape array menjadi 6x5, hitung rata-rata per baris & kolom
 8. Tampilkan semua hasil dalam format terstruktur

 Referensi:
 - Min-Max: (x - min) / (max - min)
 - Z-Score: (x - mean) / std
==========================================================
"""

import numpy as np


def buat_data_nilai(seed=42, jumlah=30, batas_bawah=40, batas_atas=100):
    """Membuat array nilai mahasiswa secara acak.

    Args:
        seed (int): Random seed untuk reprodusibilitas.
        jumlah (int): Jumlah mahasiswa.
        batas_bawah (int): Nilai minimum yang mungkin.
        batas_atas (int): Nilai maksimum yang mungkin (eksklusif di randint).

    Returns:
        np.ndarray: Array 1D berisi nilai mahasiswa.
    """
    np.random.seed(seed)
    return np.random.randint(batas_bawah, batas_atas, jumlah)


def statistik_dasar(nilai):
    """Menghitung statistik dasar dari array nilai.

    Args:
        nilai (np.ndarray): Array nilai mahasiswa.

    Returns:
        dict: Dictionary berisi mean, median, std, max, min,
              idx_max (argmax), idx_min (argmin), jumlah_lulus.
    """
    mean = np.mean(nilai)
    median = np.median(nilai)
    std = np.std(nilai)
    maks = np.max(nilai)
    mins = np.min(nilai)
    idx_max = np.argmax(nilai)
    idx_min = np.argmin(nilai)
    lulus = np.sum(nilai >= 70)

    return {
        "mean": mean, "median": median, "std": std,
        "max": maks, "min": mins,
        "idx_max": idx_max, "idx_min": idx_min,
        "jumlah_lulus": lulus,
    }


def normalisasi_minmax(nilai):
    """Normalisasi Min-Max: mengubah skala ke rentang 0-1.

    Rumus: (x - min) / (max - min)

    Args:
        nilai (np.ndarray): Array nilai asli.

    Returns:
        np.ndarray: Array nilai yang sudah dinormalisasi (0-1).
    """
    min_val = np.min(nilai)
    max_val = np.max(nilai)
    return (nilai - min_val) / (max_val - min_val)


def normalisasi_zscore(nilai):
    """Normalisasi Z-Score: mengubah ke distribusi mean=0, std=1.

    Rumus: (x - mean) / std

    Args:
        nilai (np.ndarray): Array nilai asli.

    Returns:
        np.ndarray: Array z-score.
    """
    mean = np.mean(nilai)
    std = np.std(nilai)
    return (nilai - mean) / std


def analisis_reshape(nilai, baris=6, kolom=5):
    """Reshape array dan hitung rata-rata per baris & kolom.

    Args:
        nilai (np.ndarray): Array 1D (harus berjumlah baris*kolom).
        baris (int): Jumlah baris.
        kolom (int): Jumlah kolom.

    Returns:
        tuple: (matriks, rata_per_baris, rata_per_kolom)
    """
    matriks = nilai.reshape(baris, kolom)
    rata_per_baris = np.mean(matriks, axis=1)
    rata_per_kolom = np.mean(matriks, axis=0)
    return matriks, rata_per_baris, rata_per_kolom


def tampilkan_hasil(nilai, stats, norm_mm, norm_zs, matriks, avg_baris, avg_kolom):
    """Menampilkan semua hasil analisis dalam format terstruktur.

    Args:
        nilai (np.ndarray): Array nilai asli.
        stats (dict): Hasil statistik dasar.
        norm_mm (np.ndarray): Hasil normalisasi Min-Max.
        norm_zs (np.ndarray): Hasil normalisasi Z-Score.
        matriks (np.ndarray): Matriks hasil reshape.
        avg_baris (np.ndarray): Rata-rata per baris.
        avg_kolom (np.ndarray): Rata-rata per kolom.
    """
    print("=" * 55)
    print(" ANALISIS STATISTIK NILAI MAHASISWA (NumPy)")
    print("=" * 55)

    print(f"\nData Nilai ({len(nilai)} mahasiswa):")
    print(nilai)

    print("\n── Statistik Deskriptif ──")
    print(f"  Mean    : {stats['mean']:.2f}")
    print(f"  Median  : {stats['median']:.2f}")
    print(f"  Std Dev : {stats['std']:.2f}")
    print(f"  Min     : {stats['min']} (index: {stats['idx_min']})")
    print(f"  Max     : {stats['max']} (index: {stats['idx_max']})")
    persen_lulus = (stats['jumlah_lulus'] / len(nilai)) * 100
    print(f"  Lulus   : {stats['jumlah_lulus']} dari {len(nilai)} ({persen_lulus:.1f}%)")

    print("\n── Normalisasi ──")
    print(f"  Min-Max (5 pertama) : {np.round(norm_mm[:5], 3)}")
    print(f"  Z-Score (5 pertama) : {np.round(norm_zs[:5], 3)}")

    print(f"\n── Reshape {matriks.shape[0]}x{matriks.shape[1]} (setiap baris = 1 kelas) ──")
    print(matriks)

    print("\n── Rata-rata per Kelas (per baris) ──")
    for i, avg in enumerate(avg_baris, 1):
        print(f"  Kelas {i} : {avg:.2f}")

    print("\n── Rata-rata per Mata Ujian (per kolom) ──")
    for i, avg in enumerate(avg_kolom, 1):
        print(f"  Ujian {i} : {avg:.2f}")

    print(f"\n  Rata-rata per baris  : {np.round(avg_baris, 2)}")
    print(f"  Rata-rata per kolom  : {np.round(avg_kolom, 2)}")


# ── Main Program ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Jalankan semua fungsi
    nilai = buat_data_nilai()
    stats = statistik_dasar(nilai)
    norm_mm = normalisasi_minmax(nilai)
    norm_zs = normalisasi_zscore(nilai)
    matriks, avg_baris, avg_kolom = analisis_reshape(nilai)
    tampilkan_hasil(nilai, stats, norm_mm, norm_zs, matriks, avg_baris, avg_kolom)
