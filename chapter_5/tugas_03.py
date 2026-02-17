"""
==========================================================
 TUGAS 3 - Handling Missing Data
 Chapter 5: NumPy & Pandas
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat DataFrame dengan data yang sengaja memiliki NaN
    (minimal 3 kolom, 10-15 baris)
 2. Deteksi missing values: isnull().sum() per kolom
 3. Hitung persentase missing per kolom
 4. Buat 3 versi penanganan:
    - Versi 1: dropna() — hapus baris yang memiliki NaN
    - Versi 2: fillna() — isi numerik dengan mean,
               kategorikal dengan mode
    - Versi 3: fillna(method="ffill") — forward fill
 5. Bandingkan jumlah baris ketiga versi
 6. Berikan komentar kapan metode mana yang tepat digunakan

 Catatan:
 - Gunakan np.nan untuk membuat missing values
 - Buat data yang realistis (misal: data survei/kuesioner)
==========================================================
"""

import pandas as pd
import numpy as np


def buat_data_dengan_missing():
    """Membuat DataFrame dengan data yang memiliki missing values.

    Buat data realistis (misal: survei mahasiswa) dengan 10-15 baris
    dan minimal 3 kolom. Sisipkan np.nan di beberapa posisi.

    Returns:
        pd.DataFrame: DataFrame dengan missing values.
    """
    data = {
        "Nama": ["Ahmad", "Budi", "Citra", "Dewi", "Eko",
                 "Fitri", "Gilang", "Hana", "Irfan", "Jasmine",
                 "Kamal", "Lina"],
        "Usia": [20, 21, np.nan, 22, 20, np.nan, 23, 21, 20, np.nan, 22, 21],
        "IPK": [3.5, np.nan, 3.2, 3.8, np.nan, 3.1, 3.6, np.nan, 3.4, 3.7, np.nan, 3.3],
        "Jurusan": ["Informatika", "SI", np.nan, "Informatika", "Elektro",
                    "SI", np.nan, "Informatika", "Elektro", np.nan,
                    "SI", "Informatika"],
        "Skor_Survei": [85, 90, 78, np.nan, 88, 92, np.nan, 75, np.nan, 80, 95, np.nan],
    }

    return pd.DataFrame(data)


def deteksi_missing(df):
    """Mendeteksi dan menampilkan informasi missing values.

    Args:
        df (pd.DataFrame): DataFrame yang mungkin memiliki NaN.

    Returns:
        tuple: (jumlah_missing_per_kolom, persen_missing_per_kolom)
    """
    jumlah = df.isnull().sum()
    persen = (df.isnull().sum() / len(df)) * 100
    return jumlah, persen


def versi_dropna(df):
    """Versi 1: Menghapus baris yang mengandung NaN.

    Args:
        df (pd.DataFrame): DataFrame asli.

    Returns:
        pd.DataFrame: DataFrame tanpa baris yang memiliki NaN.
    """
    return df.dropna()


def versi_fillna_statistik(df):
    """Versi 2: Mengisi NaN — numerik dengan mean, kategorikal dengan mode.

    Args:
        df (pd.DataFrame): DataFrame asli.

    Returns:
        pd.DataFrame: DataFrame dengan NaN terisi.
    """
    df_filled = df.copy()

    # Untuk setiap kolom numerik, isi NaN dengan mean
    for col in df_filled.select_dtypes(include=["number"]).columns:
        df_filled[col] = df_filled[col].fillna(df_filled[col].mean())

    # Untuk setiap kolom kategorikal/object, isi NaN dengan mode
    for col in df_filled.select_dtypes(include=["object"]).columns:
        df_filled[col] = df_filled[col].fillna(df_filled[col].mode()[0])

    return df_filled


def versi_fillna_ffill(df):
    """Versi 3: Mengisi NaN dengan forward fill (nilai sebelumnya).

    Args:
        df (pd.DataFrame): DataFrame asli.

    Returns:
        pd.DataFrame: DataFrame dengan NaN terisi (ffill).
    """
    return df.ffill()


def bandingkan_hasil(df_asli, df_dropna, df_fillna_stat, df_fillna_ffill):
    """Membandingkan jumlah baris dan sisa NaN dari ketiga versi.

    Args:
        df_asli (pd.DataFrame): DataFrame asli.
        df_dropna (pd.DataFrame): Hasil dropna.
        df_fillna_stat (pd.DataFrame): Hasil fillna statistik.
        df_fillna_ffill (pd.DataFrame): Hasil fillna ffill.
    """
    print(f"{'Metode':<25} | {'Baris':>5} | {'NaN Tersisa':>11}")
    print("-" * 48)
    print(f"{'Data Asli':<25} | {len(df_asli):>5} | {df_asli.isnull().sum().sum():>11}")
    print(f"{'dropna()':<25} | {len(df_dropna):>5} | {df_dropna.isnull().sum().sum():>11}")
    print(f"{'fillna (mean/mode)':<25} | {len(df_fillna_stat):>5} | {df_fillna_stat.isnull().sum().sum():>11}")
    print(f"{'fillna (ffill)':<25} | {len(df_fillna_ffill):>5} | {df_fillna_ffill.isnull().sum().sum():>11}")


# ── Kapan Menggunakan Metode Mana? ──────────────────────────────────────────
#
# dropna():
#   - Gunakan ketika: Data yang hilang hanya sebagian kecil dari total data
#     (biasanya < 5%), dan kehilangan baris tersebut tidak mempengaruhi
#     representasi data secara signifikan.
#   - Risiko: Kehilangan data yang banyak jika NaN tersebar di banyak baris,
#     dapat menyebabkan bias jika data yang hilang tidak acak (MNAR).
#   - Contoh kasus: Menghapus responden yang tidak mengisi seluruh survei,
#     atau menghapus transaksi dengan data tidak lengkap.
#
# fillna(mean/mode):
#   - Gunakan ketika: Ingin mempertahankan semua baris data, dan data yang
#     hilang diasumsikan mengikuti distribusi data yang ada (MAR/MCAR).
#   - Risiko: Mengurangi variasi data (variance), dapat menyebabkan
#     underestimate dari standar deviasi, tidak cocok jika distribusi
#     data sangat tidak normal (skewed).
#   - Contoh kasus: Mengisi nilai yang hilang pada data sensor, mengisi
#     data demografis yang terlewat dengan nilai rata-rata.
#
# fillna(ffill):
#   - Gunakan ketika: Data memiliki urutan waktu (time series) atau urutan
#     logis, dimana nilai sebelumnya adalah perkiraan terbaik untuk nilai
#     yang hilang.
#   - Risiko: Tidak cocok jika data tidak memiliki urutan bermakna, dapat
#     menyebabkan nilai yang "basi" jika ada banyak NaN berturut-turut.
#   - Contoh kasus: Data harga saham (harga terakhir digunakan jika tidak
#     ada transaksi), data inventaris (stok terakhir jika tidak ada update).


# ── Main Program ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Jalankan semua fungsi
    df = buat_data_dengan_missing()

    print("=" * 55)
    print(" HANDLING MISSING DATA")
    print("=" * 55)

    print("\n── Data Asli ──")
    print(df.to_string())

    print("\n── Deteksi Missing Values ──")
    jumlah, persen = deteksi_missing(df)
    print(f"Jumlah NaN per kolom:\n{jumlah}")
    print(f"\nPersentase NaN per kolom:\n{persen.round(1)}")

    print("\n── Versi 1: dropna() ──")
    df_v1 = versi_dropna(df)
    print(df_v1.to_string())

    print("\n── Versi 2: fillna (mean/mode) ──")
    df_v2 = versi_fillna_statistik(df)
    print(df_v2.to_string())

    print("\n── Versi 3: fillna (ffill) ──")
    df_v3 = versi_fillna_ffill(df)
    print(df_v3.to_string())

    print("\n── Perbandingan Hasil ──")
    bandingkan_hasil(df, df_v1, df_v2, df_v3)
