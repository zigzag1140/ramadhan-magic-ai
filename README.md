# 🌙 Ramadan Magic AI

Aplikasi Web interaktif bertenaga AI yang dirancang khusus untuk memeriahkan suasana Ramadan. Aplikasi ini mengubah "curhatan" pengguna menjadi karya visual estetik dan caption puitis menggunakan perpaduan model AI mutakhir dari Alibaba Cloud.

---

## ✨ Fitur Utama
- **AI Visual Generation (wan2.6-t2i)**: Menggunakan model **wan2.6-t2i** terbaru untuk menghasilkan ilustrasi visual Ramadan yang berkualitas tinggi dan artistik.
- **Smart NLP Captioning (Qwen-Max)**: Didukung oleh **Qwen-Max**, model bahasa (LLM) tercanggih untuk memahami konteks curhatan pengguna dan mengubahnya menjadi caption yang menyentuh hati.
- **Modern Glassmorphism UI**: Antarmuka elegan dengan efek kaca yang responsif di berbagai perangkat.
- **Download Ready**: Simpan hasil kreasi gambar langsung ke galeri dengan satu klik.

## 🛠️ Tech Stack (Teknologi yang Digunakan)

### **Backend (The Engine):**
- **Python**: Digunakan sebagai bahasa utama di sisi server untuk menangani logika bisnis dan integrasi API.
- **Alibaba Cloud AI Services**: 
    - **Qwen-Max**: Untuk pemrosesan bahasa alami dan pembuatan caption puitis.
    - **Wan2.1**: Untuk pembuatan gambar/visual berbasis teks (Text-to-Image).

### **Frontend (The Interface):**
- **HTML5 & Vanilla JavaScript**: Menangani struktur dan interaksi pengguna secara ringan tanpa dependensi berat.
- **Tailwind CSS**: Framework CSS untuk styling modern yang cepat dan efisien.
- **Google Fonts**: Menggunakan *Poppins* dan *Montserrat* untuk tipografi yang elegan.

## 📂 Struktur Proyek
```text
/ramadhan-magic-ai
├── index.html       # Struktur halaman utama
├── style.css        # Desain kustom & efek visual magis
├── script.js        # Logika frontend & komunikasi API
├── main.py          # Backend server (Python)
├── requirements.txt # Dependensi Python
└── README.md        # Dokumentasi proyek
