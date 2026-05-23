# 🧠 GLCM Object Recognition App

### Object Classification Application Using GLCM & Decision Tree

Aplikasi berbasis **Computer Vision** yang dibuat menggunakan **Python**, **Streamlit**, dan **Machine Learning** untuk melakukan klasifikasi objek berdasarkan tekstur gambar menggunakan metode **GLCM (Gray Level Co-occurrence Matrix)** dan algoritma **Decision Tree**.

Project ini dikembangkan sebagai **Project Akhir / UAS Mata Kuliah Computer Vision**.

---

# 🚀 Demo Fitur

Aplikasi mampu melakukan:

* ✅ Klasifikasi objek otomatis dari gambar
* ✅ Ekstraksi fitur tekstur menggunakan GLCM
* ✅ Klasifikasi menggunakan Decision Tree
* ✅ Menampilkan confidence score
* ✅ Visualisasi grafik fitur
* ✅ Compare 2 Images
* ✅ Riwayat prediksi
* ✅ Export hasil ke CSV/Excel
* ✅ Interface modern berbasis Streamlit

---

# 📸 Preview Aplikasi

## 🏠 Halaman Utama

Menampilkan:

* Akurasi model
* Total dataset
* Algoritma yang digunakan

```md
Tambahkan screenshot:
screenshots/home.png
```

---

## 🖼️ Upload & Prediksi Gambar

User dapat mengunggah gambar JPG/PNG/JPEG untuk diklasifikasikan.

```md
Tambahkan screenshot:
screenshots/upload.png
```

---

## 📊 Hasil Klasifikasi

Aplikasi akan menampilkan:

* Nama objek
* Confidence score
* Progress bar

```md
Tambahkan screenshot:
screenshots/result.png
```

---

## 🔍 Detail Fitur GLCM

Menampilkan hasil ekstraksi fitur:

* Contrast
* Correlation
* Energy
* Homogeneity

```md
Tambahkan screenshot:
screenshots/features.png
```

---

## 📈 Grafik Fitur

Visualisasi fitur menggunakan grafik batang.

```md
Tambahkan screenshot:
screenshots/chart.png
```

---

## ⚖️ Compare 2 Images

Membandingkan hasil klasifikasi dua gambar sekaligus.

```md
Tambahkan screenshot:
screenshots/compare.png
```

---

# 🧠 Metode yang Digunakan

## 1️⃣ Gray Level Co-occurrence Matrix (GLCM)

GLCM digunakan untuk mengekstraksi informasi tekstur dari gambar grayscale.

Pada project ini digunakan 4 fitur utama:

| Fitur       | Fungsi                               |
| ----------- | ------------------------------------ |
| Contrast    | Mengukur perbedaan intensitas piksel |
| Correlation | Mengukur hubungan antar piksel       |
| Energy      | Mengukur keseragaman tekstur         |
| Homogeneity | Mengukur kemiripan distribusi piksel |

GLCM dihitung menggunakan:

* Distance = 1
* Angle = 0°, 45°, 90°, 135°

---

## 2️⃣ Decision Tree

Algoritma Decision Tree digunakan sebagai model klasifikasi berdasarkan fitur hasil ekstraksi GLCM.

Model dilatih menggunakan:

* `max_depth = 5`
* `train_test_split = 70:30`
* `random_state = 42`

---

# 🛠️ Teknologi yang Digunakan

| Teknologi    | Fungsi                   |
| ------------ | ------------------------ |
| Python       | Bahasa pemrograman utama |
| Streamlit    | Framework web aplikasi   |
| OpenCV       | Pengolahan citra         |
| Scikit-Learn | Machine Learning         |
| NumPy        | Operasi numerik          |
| Pandas       | Manipulasi data          |
| Matplotlib   | Visualisasi grafik       |
| PIL          | Membaca gambar           |

---

# 📂 Struktur Project

```bash
GLCM_Object_Recognition/
│
├── app.py
├── glcm_feature.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── dataset/
│   ├── Buah/
│   ├── Sayur/
│   ├── Kain/
│   ├── Logam/
│   └── Bambu/
│
├── screenshots/
│
└── hasil_klasifikasi.csv
```

---

# ⚙️ Cara Instalasi

## 1️⃣ Clone Repository

```bash
git clone https://github.com/username/repository-name.git
```

---

## 2️⃣ Masuk ke Folder Project

```bash
cd repository-name
```

---

## 3️⃣ Install Dependency

```bash
pip install -r requirements.txt
```

---

# ▶️ Cara Menjalankan Aplikasi

```bash
streamlit run app.py
```

Jika berhasil, aplikasi akan berjalan di browser:

```bash
http://localhost:8501
```

---

# 📄 Penjelasan Source Code

## 📌 app.py

File utama aplikasi Streamlit.

Berfungsi untuk:

* Menampilkan UI aplikasi
* Upload gambar
* Menampilkan hasil klasifikasi
* Menampilkan grafik fitur
* Menampilkan riwayat prediksi

---

## 📌 glcm_feature.py

File untuk ekstraksi fitur tekstur menggunakan metode GLCM.

Fitur yang diekstraksi:

* Contrast
* Correlation
* Energy
* Homogeneity

---

## 📌 train_model.py

File untuk:

* Membaca dataset
* Training model
* Split data train-test
* Menghitung akurasi model

---

# 🗂️ Dataset

Dataset terdiri dari beberapa kelas objek:

| Kelas | Deskripsi              |
| ----- | ---------------------- |
| Buah  | Apel, jeruk, dll       |
| Sayur | Wortel, tomat, dll     |
| Kain  | Denim, kain polos, dll |
| Logam | Emas, besi, dll        |
| Bambu | Tekstur bambu          |

Total dataset digunakan untuk proses training dan testing model.

---

# 📊 Alur Sistem

```text
Input Gambar
      ↓
Preprocessing
(Grayscale + Resize)
      ↓
Ekstraksi Fitur GLCM
      ↓
Decision Tree Classification
      ↓
Hasil Prediksi
```

---

# 📈 Hasil Pengujian

Hasil pengujian menunjukkan bahwa model mampu melakukan klasifikasi objek dengan baik berdasarkan tekstur gambar.

Contoh hasil klasifikasi:

| File       | Hasil Prediksi | Confidence |
| ---------- | -------------- | ---------- |
| apel.jpg   | Buah           | 100%       |
| wortel.jpg | Sayur          | 96%        |
| denim.jpg  | Kain           | 98%        |
| emas.jpg   | Logam          | 95%        |

---

# 📥 Export Hasil

Aplikasi menyediakan fitur export hasil klasifikasi ke file CSV sehingga dapat dibuka menggunakan:

* Microsoft Excel
* Google Spreadsheet
* WPS Spreadsheet

---

# 💡 Kelebihan Project

* Interface sederhana dan modern
* Mudah digunakan
* Proses klasifikasi cepat
* Menampilkan detail fitur
* Support multiple mode
* Cocok untuk pembelajaran Computer Vision

---

# ⚠️ Kekurangan Project

* Dataset masih terbatas
* Belum menggunakan Deep Learning
* Sensitif terhadap kualitas gambar
* Belum support realtime webcam

---

# 🔮 Pengembangan Selanjutnya

Project ini dapat dikembangkan menggunakan:

* CNN / Deep Learning
* Realtime Camera Detection
* Mobile App
* Dataset lebih besar
* Random Forest / SVM

---

# 👨‍💻 Author

## Apdan Arifin

Mahasiswa Teknik Informatika
Project UAS Computer Vision

---

# 📚 Referensi

* Gonzalez & Woods — Digital Image Processing
* Haralick Texture Features Paper
* OpenCV Documentation
* Streamlit Documentation
* Scikit-Learn Documentation

---

# ⭐ Support

Jika project ini bermanfaat:

⭐ Star repository ini
🍴 Fork repository
📢 Share project ini

---

# 🏁 Penutup

Project ini dibuat sebagai implementasi dasar Computer Vision menggunakan ekstraksi fitur tekstur dan machine learning untuk klasifikasi objek gambar. Diharapkan project ini dapat membantu pembelajaran dan pengembangan sistem pengolahan citra digital di masa depan.
