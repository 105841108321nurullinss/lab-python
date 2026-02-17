"""
==========================================================
 TUGAS 1 - Klasifikasi Dataset Wine
 Chapter 6: Machine Learning & AI
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Load dataset Wine dari sklearn, tampilkan info dataset
    (jumlah sampel, fitur, nama kelas, distribusi kelas)
 2. Preprocessing: train/test split 80:20 dengan stratify,
    random_state=42, lalu StandardScaler
 3. Train 3 model klasifikasi:
    a. KNN - coba k=3, 5, 7, pilih k terbaik
    b. Decision Tree (max_depth=5)
    c. Random Forest (n_estimators=100)
 4. Evaluasi setiap model: accuracy, classification_report,
    confusion_matrix
 5. Buat tabel perbandingan accuracy ketiga model
 6. Prediksi 3 sampel baru menggunakan model terbaik
 7. Tulis komentar analisis: model mana terbaik dan mengapa

 Dataset Wine:
 - 178 sampel, 13 fitur kimia, 3 kelas wine
 - Fitur: alcohol, malic_acid, ash, alkalinity, magnesium, dll.
 - Kelas: class_0, class_1, class_2
==========================================================
"""

import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
)


# ============================================
# 1. Load & Eksplorasi Dataset
# ============================================
def load_dan_eksplorasi():
    """Load dataset Wine dan tampilkan informasi dasar.

    Returns:
        tuple: (data, target, feature_names, target_names)
    """
    wine = load_wine()

    print(f"Jumlah sampel   : {wine.data.shape[0]}")
    print(f"Jumlah fitur    : {wine.data.shape[1]}")
    print(f"Nama fitur      : {list(wine.feature_names)}")
    print(f"Nama kelas      : {list(wine.target_names)}")
    print(f"\nDistribusi kelas:")
    print(f"  - {wine.target_names[0]}: {np.sum(wine.target == 0)} sampel")
    print(f"  - {wine.target_names[1]}: {np.sum(wine.target == 1)} sampel")
    print(f"  - {wine.target_names[2]}: {np.sum(wine.target == 2)} sampel")

    print(f"\nContoh data (5 pertama):")
    for i in range(5):
        print(f"  Sampel {i+1}: {wine.data[i][:4]}... -> {wine.target_names[wine.target[i]]}")

    return wine.data, wine.target, wine.feature_names, wine.target_names


# ============================================
# 2. Preprocessing
# ============================================
def preprocessing(X, y):
    """Split data dan lakukan standardisasi.

    Args:
        X (ndarray): Feature matrix.
        y (ndarray): Target array.

    Returns:
        tuple: (X_train, X_test, y_train, y_test,
                X_train_scaled, X_test_scaled, scaler)
    """
    # Split data 80:20 dengan stratify dan random_state=42
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print(f"Total data    : {len(X)}")
    print(f"Training data : {len(X_train)} ({len(X_train)/len(X)*100:.0f}%)")
    print(f"Testing data  : {len(X_test)} ({len(X_test)/len(X)*100:.0f}%)")

    # Standardisasi dengan StandardScaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print(f"\nSebelum scaling - Mean: {X_train[:, 0].mean():.2f}, Std: {X_train[:, 0].std():.2f}")
    print(f"Setelah scaling - Mean: {X_train_scaled[:, 0].mean():.2f}, Std: {X_train_scaled[:, 0].std():.2f}")

    return X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler


# ============================================
# 3. Model 1: KNN (K-Nearest Neighbors)
# ============================================
def train_knn(X_train_scaled, X_test_scaled, y_train, y_test, target_names):
    """Train KNN dengan k=3, 5, 7 dan pilih k terbaik.

    Args:
        X_train_scaled (ndarray): Training features (scaled).
        X_test_scaled (ndarray): Testing features (scaled).
        y_train (ndarray): Training labels.
        y_test (ndarray): Testing labels.
        target_names (list): Nama kelas.

    Returns:
        tuple: (best_model, best_k, best_accuracy, y_pred)
    """
    k_values = [3, 5, 7]
    best_acc = 0
    best_k = 0
    best_model = None

    print("Mencari K terbaik:")
    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train_scaled, y_train)
        y_pred = knn.predict(X_test_scaled)
        acc = accuracy_score(y_test, y_pred)
        print(f"  K={k}: Accuracy = {acc:.4f} ({acc*100:.1f}%)")
        if acc > best_acc:
            best_acc = acc
            best_k = k
            best_model = knn

    print(f"\nK terbaik: {best_k} dengan accuracy {best_acc:.4f}")

    # Evaluasi model terbaik
    y_pred_best = best_model.predict(X_test_scaled)
    print(f"\nClassification Report (KNN k={best_k}):")
    print(classification_report(y_test, y_pred_best, target_names=target_names))
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred_best)}")

    return best_model, best_k, best_acc, y_pred_best


# ============================================
# 4. Model 2: Decision Tree
# ============================================
def train_decision_tree(X_train, X_test, y_train, y_test, target_names, feature_names):
    """Train Decision Tree dengan max_depth=5.

    Args:
        X_train (ndarray): Training features (tanpa scaling).
        X_test (ndarray): Testing features (tanpa scaling).
        y_train (ndarray): Training labels.
        y_test (ndarray): Testing labels.
        target_names (list): Nama kelas.
        feature_names (list): Nama fitur.

    Returns:
        tuple: (model, accuracy, y_pred)
    """
    dt = DecisionTreeClassifier(max_depth=5, random_state=42)
    dt.fit(X_train, y_train)

    y_pred_dt = dt.predict(X_test)
    acc_dt = accuracy_score(y_test, y_pred_dt)
    print(f"Accuracy: {acc_dt:.4f} ({acc_dt*100:.1f}%)")

    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred_dt, target_names=target_names))
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred_dt)}")

    print("\nFeature Importance (Top 5):")
    importances = sorted(
        zip(feature_names, dt.feature_importances_),
        key=lambda x: x[1], reverse=True
    )
    for name, imp in importances[:5]:
        bar = "#" * int(imp * 40)
        print(f"  {name:30s}: {imp:.4f} {bar}")

    return dt, acc_dt, y_pred_dt


# ============================================
# 5. Model 3: Random Forest
# ============================================
def train_random_forest(X_train, X_test, y_train, y_test, target_names, feature_names):
    """Train Random Forest dengan n_estimators=100.

    Args:
        X_train (ndarray): Training features (tanpa scaling).
        X_test (ndarray): Testing features (tanpa scaling).
        y_train (ndarray): Training labels.
        y_test (ndarray): Testing labels.
        target_names (list): Nama kelas.
        feature_names (list): Nama fitur.

    Returns:
        tuple: (model, accuracy, y_pred)
    """
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    y_pred_rf = rf.predict(X_test)
    acc_rf = accuracy_score(y_test, y_pred_rf)
    print(f"Accuracy: {acc_rf:.4f} ({acc_rf*100:.1f}%)")

    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred_rf, target_names=target_names))
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred_rf)}")

    print("\nFeature Importance (Top 5):")
    importances = sorted(
        zip(feature_names, rf.feature_importances_),
        key=lambda x: x[1], reverse=True
    )
    for name, imp in importances[:5]:
        bar = "#" * int(imp * 40)
        print(f"  {name:30s}: {imp:.4f} {bar}")

    return rf, acc_rf, y_pred_rf


# ============================================
# 6. Perbandingan Model
# ============================================
def perbandingan_model(hasil_knn, hasil_dt, hasil_rf, y_test):
    """Buat tabel perbandingan accuracy ketiga model.

    Args:
        hasil_knn (tuple): (nama, accuracy, y_pred) dari KNN.
        hasil_dt (tuple): (nama, accuracy, y_pred) dari Decision Tree.
        hasil_rf (tuple): (nama, accuracy, y_pred) dari Random Forest.
        y_test: Target sebenarnya untuk menghitung metrik.

    Returns:
        str: Nama model terbaik.
    """
    models = [hasil_knn, hasil_dt, hasil_rf]

    print(f"{'Model':<20} | {'Accuracy':>10} | {'Precision':>10} | {'Recall':>10} | {'F1-Score':>10}")
    print("-" * 70)

    sorted_models = sorted(models, key=lambda x: x[1], reverse=True)
    for name, acc, y_pred in sorted_models:
        prec = precision_score(y_test, y_pred, average='weighted')
        rec = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        marker = " <- TERBAIK" if name == sorted_models[0][0] else ""
        print(f"{name:<20} | {acc:>10.4f} | {prec:>10.4f} | {rec:>10.4f} | {f1:>10.4f}{marker}")

    print("=" * 70)
    best_model_name = sorted_models[0][0]
    best_acc = sorted_models[0][1]
    print(f"Model Terbaik: {best_model_name} (Accuracy: {best_acc*100:.1f}%)")

    return best_model_name


# ============================================
# 7. Prediksi Data Baru
# ============================================
def prediksi_data_baru(model, scaler, feature_names, target_names, use_scaling=True):
    """Prediksi kelas untuk 3 sampel wine baru.

    Args:
        model: Model terbaik yang sudah di-train.
        scaler: StandardScaler (jika model butuh scaling).
        feature_names (list): Nama fitur.
        target_names (list): Nama kelas.
        use_scaling (bool): Apakah data perlu di-scale.
    """
    # Data baru (13 fitur sesuai dataset Wine)
    data_baru = np.array([
        [13.5, 2.0, 2.5, 18.0, 105.0, 2.8, 2.5, 0.3, 1.8, 5.0, 1.0, 3.0, 1200],  # mirip class_0
        [12.0, 1.5, 2.3, 20.0, 90.0, 2.0, 1.8, 0.4, 1.5, 4.0, 0.9, 2.5, 700],    # mirip class_1
        [13.0, 3.5, 2.4, 22.0, 120.0, 1.5, 0.8, 0.5, 1.2, 7.0, 0.7, 1.8, 500],   # mirip class_2
    ])

    # Scaling jika diperlukan
    if use_scaling:
        data_prediksi = scaler.transform(data_baru)
    else:
        data_prediksi = data_baru

    # Prediksi
    prediksi = model.predict(data_prediksi)

    print("Prediksi untuk wine baru:")
    print(f"{'No':>3} | {'Alcohol':>8} | {'Malic Acid':>11} | {'Ash':>5} | {'Prediksi':<15}")
    print("-" * 55)
    for i, (d, p) in enumerate(zip(data_baru, prediksi), 1):
        nama_kelas = target_names[p]
        print(f"{i:>3} | {d[0]:>8.1f} | {d[1]:>11.1f} | {d[2]:>5.1f} | {nama_kelas:<15}")

    if hasattr(model, 'predict_proba'):
        print("\nProbabilitas per kelas:")
        probabilitas = model.predict_proba(data_prediksi)
        for i, prob in enumerate(probabilitas, 1):
            prob_str = ", ".join([f"{target_names[j]}={p:.1%}" for j, p in enumerate(prob)])
            print(f"  Wine {i}: {prob_str}")


# ============================================
# 8. Analisis
# ============================================
def analisis():
    """Tulis komentar analisis tentang hasil klasifikasi."""
    print("=" * 60)
    print("ANALISIS HASIL KLASIFIKASI")
    print("=" * 60)
    print("""
1. Model terbaik: Random Forest
   Alasan: Random Forest memberikan accuracy tertinggi karena
   menggunakan ensemble dari banyak decision tree yang mengurangi
   overfitting dan meningkatkan generalisasi.

2. Kelas yang sulit diprediksi: class_1 (kadang tertukar dengan class_0/2)
   Karena: Fitur-fitur kimia class_1 memiliki nilai yang berada
   di antara class_0 dan class_2 sehingga batasannya kurang tegas.

3. Fitur terpenting:
   - flavanoids: Senyawa antioksidan yang berbeda signifikan antar kelas
   - color_intensity: Intensitas warna wine yang berbeda per jenis
   - proline: Asam amino yang berkorelasi dengan kualitas wine

4. Pengaruh scaling:
   - KNN sangat membutuhkan scaling karena menggunakan jarak Euclidean
   - Decision Tree dan Random Forest tidak memerlukan scaling karena
     berbasis split berdasarkan threshold

5. Rekomendasi:
   - Gunakan Random Forest untuk produksi karena robust dan akurat
   - Pertimbangkan KNN sebagai alternatif karena lebih cepat untuk
     dataset kecil dan mudah di-interpretasi
""")


# ── Main Program ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("TUGAS 1 - KLASIFIKASI DATASET WINE")
    print("=" * 60)

    # 1. Load dataset
    print("\n=== 1. Load & Eksplorasi Dataset ===")
    X, y, feature_names, target_names = load_dan_eksplorasi()

    # 2. Preprocessing
    print("\n=== 2. Preprocessing ===")
    X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler = preprocessing(X, y)

    # 3. Train KNN
    print("\n=== 3. K-Nearest Neighbors ===")
    knn_model, best_k, acc_knn, y_pred_knn = train_knn(
        X_train_scaled, X_test_scaled, y_train, y_test, target_names
    )

    # 4. Train Decision Tree
    print("\n=== 4. Decision Tree ===")
    dt_model, acc_dt, y_pred_dt = train_decision_tree(
        X_train, X_test, y_train, y_test, target_names, feature_names
    )

    # 5. Train Random Forest
    print("\n=== 5. Random Forest ===")
    rf_model, acc_rf, y_pred_rf = train_random_forest(
        X_train, X_test, y_train, y_test, target_names, feature_names
    )

    # 6. Perbandingan
    print("\n=== 6. Perbandingan Model ===")
    best = perbandingan_model(
        (f"KNN (k={best_k})", acc_knn, y_pred_knn),
        ("Decision Tree", acc_dt, y_pred_dt),
        ("Random Forest", acc_rf, y_pred_rf),
        y_test
    )

    # 7. Prediksi data baru (gunakan model terbaik - Random Forest)
    print("\n=== 7. Prediksi Data Baru ===")
    prediksi_data_baru(rf_model, scaler, feature_names, target_names, use_scaling=False)

    # 8. Analisis
    print("\n=== 8. Analisis ===")
    analisis()
