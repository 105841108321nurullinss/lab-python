"""
==========================================================
 TUGAS 2 - Sistem Data Mahasiswa
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat dictionary berisi data 5 mahasiswa, setiap mahasiswa
    memiliki: nama, nim, jurusan, dan nilai (dict mata kuliah)
 2. Tampilkan seluruh data mahasiswa dalam format tabel rapi
 3. Hitung rata-rata nilai setiap mahasiswa
 4. Cari mahasiswa dengan rata-rata tertinggi
 5. Tambahkan 1 mahasiswa baru ke dictionary
 6. Gunakan dict comprehension untuk {nama: rata_rata_nilai}

 Contoh Struktur:
 mahasiswa = {
     "MHS001": {
         "nama": "Ahmad",
         "jurusan": "Informatika",
         "nilai": {"Algoritma": 85, "Basis Data": 90, "Jaringan": 78}
     },
     ...
 }
==========================================================
"""

# ── Data Mahasiswa ────────────────────────────────────────────────────────────
mahasiswa = {
    "MHS001": {
        "nama": "Ahmad",
        "jurusan": "Informatika",
        "nilai": {"Algoritma": 85, "Basis Data": 90, "Jaringan": 78}
    },
    "MHS002": {
        "nama": "Budi",
        "jurusan": "Sistem Informasi",
        "nilai": {"Algoritma": 75, "Basis Data": 82, "Jaringan": 88}
    },
    "MHS003": {
        "nama": "Citra",
        "jurusan": "Informatika",
        "nilai": {"Algoritma": 92, "Basis Data": 95, "Jaringan": 90}
    },
    "MHS004": {
        "nama": "Dewi",
        "jurusan": "Teknik Komputer",
        "nilai": {"Algoritma": 70, "Basis Data": 75, "Jaringan": 72}
    },
    "MHS005": {
        "nama": "Eko",
        "jurusan": "Informatika",
        "nilai": {"Algoritma": 88, "Basis Data": 85, "Jaringan": 80}
    }
}


# ── Tampilkan Data dalam Format Tabel ─────────────────────────────────────────
print("=" * 80)
print("                         DATA MAHASISWA                         ")
print("=" * 80)
print(f"{'NIM':<10} | {'Nama':<15} | {'Jurusan':<20} | {'Nilai'}")
print("-" * 80)
for nim, data in mahasiswa.items():
    nilai_str = ", ".join([f"{mk}: {n}" for mk, n in data["nilai"].items()])
    print(f"{nim:<10} | {data['nama']:<15} | {data['jurusan']:<20} | {nilai_str}")
print("-" * 80)


# ── Hitung Rata-rata Nilai Setiap Mahasiswa ──────────────────────────────────
print("\n===== RATA-RATA NILAI MAHASISWA =====")
for nim, data in mahasiswa.items():
    rata_rata = sum(data["nilai"].values()) / len(data["nilai"])
    print(f"{data['nama']:<15} : {rata_rata:.2f}")


# ── Cari Mahasiswa dengan Rata-rata Tertinggi ────────────────────────────────
rata_rata_tertinggi = 0
mahasiswa_terbaik = ""
nim_terbaik = ""

for nim, data in mahasiswa.items():
    rata_rata = sum(data["nilai"].values()) / len(data["nilai"])
    if rata_rata > rata_rata_tertinggi:
        rata_rata_tertinggi = rata_rata
        mahasiswa_terbaik = data["nama"]
        nim_terbaik = nim

print(f"\n===== MAHASISWA DENGAN RATA-RATA TERTINGGI =====")
print(f"NIM     : {nim_terbaik}")
print(f"Nama    : {mahasiswa_terbaik}")
print(f"Rata-rata: {rata_rata_tertinggi:.2f}")


# ── Tambahkan Mahasiswa Baru ─────────────────────────────────────────────────
mahasiswa["MHS006"] = {
    "nama": "Fajar",
    "jurusan": "Sistem Informasi",
    "nilai": {"Algoritma": 80, "Basis Data": 78, "Jaringan": 85}
}
print(f"\n===== MAHASISWA BARU DITAMBAHKAN =====")
print(f"NIM     : MHS006")
print(f"Nama    : {mahasiswa['MHS006']['nama']}")
print(f"Jurusan : {mahasiswa['MHS006']['jurusan']}")


# ── Dictionary Comprehension ─────────────────────────────────────────────────
ringkasan = {
    data["nama"]: sum(data["nilai"].values()) / len(data["nilai"])
    for nim, data in mahasiswa.items()
}

print(f"\n===== RINGKASAN (Dict Comprehension) =====")
print(f"{'Nama':<15} | {'Rata-rata':>10}")
print("-" * 28)
for nama, rata in ringkasan.items():
    print(f"{nama:<15} | {rata:>10.2f}")
