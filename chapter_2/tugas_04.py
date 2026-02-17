"""
==========================================================
 TUGAS 4 - Tuple untuk Data Koordinat
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat list berisi 5 tuple koordinat (x, y) sebagai lokasi
 2. Gunakan tuple unpacking untuk menampilkan setiap koordinat
 3. Hitung jarak Euclidean antar dua titik:
    d = sqrt((x2-x1)^2 + (y2-y1)^2)  (gunakan ** 0.5, tanpa math)
 4. Cari pasangan titik yang paling dekat jaraknya
 5. Buat dictionary dengan tuple sebagai key, nama lokasi sebagai value
 6. Buktikan tuple bisa jadi key dict tapi list tidak (try-except)
==========================================================
"""

# ── Data Koordinat ───────────────────────────────────────────────────────────
koordinat = [
    (0, 0),
    (3, 4),
    (6, 8),
    (1, 1),
    (5, 2)
]


# ── Tuple Unpacking ──────────────────────────────────────────────────────────
print("===== DATA KOORDINAT =====")
for i, (x, y) in enumerate(koordinat, 1):
    print(f"Titik {i}: x={x}, y={y}")


# ── Fungsi Jarak Euclidean ───────────────────────────────────────────────────
def hitung_jarak(titik_1, titik_2):
    """Hitung jarak Euclidean antara dua titik.

    Args:
        titik_1 (tuple): Koordinat titik pertama (x, y).
        titik_2 (tuple): Koordinat titik kedua (x, y).

    Returns:
        float: Jarak antara kedua titik.
    """
    x1, y1 = titik_1
    x2, y2 = titik_2
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


# ── Cari Pasangan Titik Terdekat ─────────────────────────────────────────────
print("\n===== JARAK ANTAR TITIK =====")
jarak_min = float('inf')
pasangan_terdekat = (0, 0)

for i in range(len(koordinat)):
    for j in range(i + 1, len(koordinat)):
        jarak = hitung_jarak(koordinat[i], koordinat[j])
        print(f"Titik {i+1} ke Titik {j+1}: {jarak:.2f}")
        if jarak < jarak_min:
            jarak_min = jarak
            pasangan_terdekat = (i + 1, j + 1)

print(f"\n===== PASANGAN TERDEKAT =====")
print(f"Titik {pasangan_terdekat[0]} {koordinat[pasangan_terdekat[0]-1]} dan Titik {pasangan_terdekat[1]} {koordinat[pasangan_terdekat[1]-1]}")
print(f"Jarak: {jarak_min:.2f}")


# ── Tuple sebagai Key Dictionary ─────────────────────────────────────────────
lokasi = {
    (0, 0): "Kampus Unismuh",
    (3, 4): "Perpustakaan",
    (6, 8): "Kantin",
    (1, 1): "Parkiran",
    (5, 2): "Lab Komputer"
}

print(f"\n===== TUPLE SEBAGAI KEY DICTIONARY =====")
for coord, nama in lokasi.items():
    print(f"{coord} -> {nama}")


# ── Buktikan List Tidak Bisa Jadi Key ────────────────────────────────────────
print(f"\n===== BUKTI LIST TIDAK BISA JADI KEY =====")
print("Tuple sebagai key: BERHASIL (seperti contoh di atas)")

try:
    invalid_dict = {[1, 2]: "ini akan error"}
except TypeError as e:
    print(f"List sebagai key: ERROR!")
    print(f"Pesan error: {e}")
    print("Alasan: List tidak bisa menjadi key dictionary karena mutable!")
