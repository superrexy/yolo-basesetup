# YOLO Object Detection

Aplikasi deteksi objek menggunakan YOLO (You Only Look Once) dengan input dari webcam atau kamera.

## Instalasi

Pasang semua dependensi yang diperlukan:

```bash
pip install -r requirements.txt
```

## Menjalankan Program

```bash
python main.py
```

## Konfigurasi Variabel

Berikut adalah variabel yang dapat dikonfigurasi di `main.py`:

| Variabel      | Default        | Deskripsi                                                                                                    |
| ------------- | -------------- | ------------------------------------------------------------------------------------------------------------ |
| `VIDEO_INDEX` | `0`            | Indeks kamera yang digunakan. `0` untuk kamera utama, ganti jika menggunakan kamera lain.                    |
| `MODEL_PATH`  | `"yolo26n.pt"` | Path ke file model YOLO. Pastikan file model tersedia di direktori project.                                  |
| `MODEL_CONF`  | `0.70`         | Threshold confidence untuk deteksi objek (0.0 - 1.0). Semakin tinggi nilainya, semakin ketat filter deteksi. |

## Menghentikan Program

Tekan tombol `q` pada keyboard untuk menutup jendela dan menghentikan program.

## Catatan

Program akan otomatis mendeteksi dan menggunakan device terbaik yang tersedia (CUDA, MPS, atau CPU).
