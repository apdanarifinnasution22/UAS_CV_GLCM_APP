# 🧠 GLCM Object Recognition App

Aplikasi berbasis **Computer Vision** menggunakan **Python**, **Streamlit**, metode **GLCM (Gray Level Co-occurrence Matrix)**, dan algoritma **Decision Tree** untuk melakukan klasifikasi objek berdasarkan tekstur gambar.

Project ini dibuat sebagai **Project Akhir / UAS Computer Vision**.

---

# ✨ Fitur Utama

* ✅ Klasifikasi objek otomatis
* ✅ Ekstraksi fitur GLCM
* ✅ Decision Tree Classification
* ✅ Confidence Score
* ✅ Grafik fitur GLCM
* ✅ Compare 2 Images
* ✅ Riwayat prediksi
* ✅ Export hasil ke CSV/Excel

---

# 🗂️ Kategori Dataset

* 🍎 Buah
* 🥕 Sayur
* 🧵 Kain
* 🪙 Logam
* 🎋 Bambu

---

# 🛠️ Teknologi

* Python
* Streamlit
* OpenCV
* Scikit-Learn
* NumPy
* Pandas
* Matplotlib

---

# 📂 Struktur Project

```bash
GLCM_Object_Recognition/
│
├── app.py
├── glcm_feature.py
├── train_model.py
├── requirements.txt
├── dataset/
└── hasil_klasifikasi.csv
```

---

# ⚙️ Cara Menjalankan

## Install Dependency

```bash
pip install -r requirements.txt
```

## Jalankan Aplikasi

```bash
streamlit run app.py
```

---

# 🧠 Metode yang Digunakan

## GLCM

Ekstraksi fitur tekstur:

* Contrast
* Correlation
* Energy
* Homogeneity

## Decision Tree

Digunakan untuk klasifikasi objek berdasarkan fitur GLCM.

---

# 📊 Alur Sistem

```text
Input Gambar
     ↓
Preprocessing
     ↓
Ekstraksi Fitur GLCM
     ↓
Decision Tree
     ↓
Hasil Prediksi
```

---

# 📈 Hasil

Aplikasi mampu melakukan klasifikasi objek dengan baik berdasarkan tekstur gambar dan menampilkan confidence score hasil prediksi.

---

# 👨‍💻 Author

**Apdan Arifin**
Teknik Informatika
Project UAS Computer Vision

---

# 📚 Referensi

* OpenCV Documentation
* Streamlit Documentation
* Scikit-Learn Documentation
* Gonzalez & Woods - Digital Image Processing

---

# ⭐ Support

Jika project ini bermanfaat:

* ⭐ Star repository
* 🍴 Fork repository
* 📢 Share project
