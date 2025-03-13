# Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data peminjaman sepeda berdasarkan musim dan pola penggunaan dalam sehari. Selain itu, dilakukan analisis lanjutan dengan teknik manual grouping dan binning untuk memahami pola peminjaman lebih dalam. 

## Pertanyaan Bisnis
1. Bagaimana pengaruh musim terhadap jumlah peminjaman sepeda?
2. Bagaimana tren penggunaan sepeda berdasarkan waktu dalam sehari?
3. Apakah terdapat pola peminjaman sepeda berdasarkan kategori waktu (pagi, siang, sore, malam)?
4. Bagaimana distribusi jumlah peminjaman sepeda berdasarkan kategori (rendah, sedang, tinggi)?

## Struktur Direktori
```
submission/
├── dashboard/
│   ├── main_data.csv        # Dataset utama untuk dashboard
│   └── dashboard.py         # Aplikasi Streamlit untuk visualisasi
├── data/
│   ├── day.csv              # Dataset penyewaan harian
│   ├── hour.csv             # Dataset penyewaan per jam
├── notebook.ipynb           # Notebook untuk analisis eksplorasi data (EDA)
├── README.md                # Dokumentasi proyek
├── requirements.txt         # Daftar dependensi yang dibutuhkan
└── url.txt                  # URL dashboard 

```

## Instalasi dan Menjalankan Proyek
### Menjalankan Analisis Data
1. Pastikan Anda memiliki Jupyter Notebook atau Google Colab.
2. Buka `notebook.ipynb` dan jalankan semua sel untuk melihat hasil analisis.

### Menjalankan Dashboard (Streamlit)  
1. Instal library yang diperlukan dengan menjalankan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```
# Library utama yang digunakan dalam proyek ini:
streamlit==1.27.0
pandas==2.1.0
numpy==1.24.3
matplotlib==3.7.2
seaborn==0.12.2

2. Jalankan dashboard dengan perintah:
   ```bash
   streamlit run dashboard/Dashboard.py
   ```
3. Dashboard akan terbuka di browser web default Anda.

## Fitur Dashboard
Dashboard ini menyediakan beberapa fitur utama:
- Filter Data berdasarkan waktu & Musim:
   * Pengguna dapat memilih rentang tanggal, dan dashboard akan secara otomatis menampilkan musim yang terdeteksi.
- Visualisasi interaktif:
   * Menampilkan total penyewaan harian dan tren peminjaman berdasarkan waktu yang dipilih. 
   *  Melihat bagaimana musim mempengaruhi jumlah peminjaman sepeda.
   *  Menganalisis jam-jam sibuk dan sepi dalam sehari.
- Analisis Manual Grouping & Binning:
   * Mengelompokkan peminjaman berdasarkan waktu dalam sehari.
   * Menggunakan teknik binning untuk memahami distribusi peminjaman.

## Kesimpulan Utama
1. Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?
Musim gugur memiliki jumlah penyewaan tertinggi, kemungkinan karena suhu yang nyaman.
Musim dingin memiliki jumlah penyewaan terendah, karena cuaca dingin dan bersalju.
2. Bagaimana pola penyewaan sepeda berdasarkan waktu dalam sehari?
Jam sibuk peminjaman terjadi pada 07:00-09:00 dan 17:00-19:00, sesuai dengan jam kerja/sekolah.
Jumlah peminjaman rendah pada malam hari (setelah pukul 22:00), karena aktivitas luar ruangan menurun.
3. Bagaimana distribusi peminjaman berdasarkan kategori waktu?
Sore hari memiliki jumlah penyewaan tertinggi, terutama setelah jam kerja/sekolah.
Malam hari memiliki jumlah penyewaan paling sedikit, kemungkinan karena faktor keamanan.
4. Bagaimana distribusi jumlah peminjaman berdasarkan kategori (rendah, sedang, tinggi)?
Sebagian besar peminjaman masuk dalam kategori "rendah", terutama di luar jam sibuk.
Kategori "tinggi" hanya terjadi di jam sibuk pagi dan sore.

## Rekomendasi Bisnis
1. Tambahkan lebih banyak sepeda di musim gugur dan jam sibuk untuk menghindari kekurangan unit.
2. Terapkan strategi promosi pada musim dingin untuk meningkatkan peminjaman.
3. Perkuat keamanan dan pencahayaan di malam hari untuk menarik lebih banyak pengguna.

## Sumber Data
Dataset yang digunakan dalam proyek ini adalah Bike Sharing Dataset dari [sumber data](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset).

## Penulis
**Hanna Tashya Portuna**  
Email: mc185d5x0288@student.devacademy.id  
ID Dicoding: MC185D5X0288

---
© 2025 Bike Sharing Analysis Project  
Proyek ini dikembangkan sebagai bagian dari submission Dicoding "Belajar Analisis Data dengan Python".
