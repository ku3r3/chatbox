# 🧠 Chatbot GUI dengan Python + TensorFlow

Chatbot sederhana berbasis **GUI Tkinter** yang menggunakan **Natural Language Processing (NLP)** dan **TensorFlow** untuk memprediksi intent dari user.

## ⚠️ Catatan Penting

> **Gunakan Python versi 3.10 atau lebih rendah.**
>
> TensorFlow saat ini **tidak kompatibel dengan Python versi terbaru** (seperti 3.12 atau 3.13). Disarankan menggunakan Python **3.10.x** untuk menghindari masalah instalasi.

---

## 🛠️ Setup Awal

1. **Clone repositori ini** atau download sebagai ZIP

   ```bash
   git clone https://github.com/riskiputraalamzah/chatbox.git
   cd chatbox
   ```

2. **Buat dan aktifkan virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate    # Windows
   # source venv/bin/activate  # Linux/macOS
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## 🚀 Menjalankan Chatbot

1. **Training data** (hanya dilakukan jika `chatbot_model.h5` belum ada)

   ```bash
   python train_chatbot.py
   ```

2. **Jalankan GUI chatbot**
   ```bash
   python gui_chatbot.py
   ```

---

## 📁 Struktur Proyek

```
chatbot-project/
├── intents.json # Data intent dan response
├── train_chatbot.py # File training model chatbot
├── gui_chatbot.py # Aplikasi GUI dengan Tkinter
├── words.pkl # Pickle kata-kata hasil training
├── classes.pkl # Pickle classes hasil training
├── chatbot_model.h5 # Model hasil training
├── requirements.txt # Daftar dependencies
└── .gitignore
```
