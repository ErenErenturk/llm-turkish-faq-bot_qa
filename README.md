# 🇹🇷 LLM Turkish FAQ Bot

LLM tabanlı bu soru-cevap (FAQ) chatbot, Türkçe dokümanları kullanarak sorulara akıllı cevaplar verebilen bir sistemdir. Proje, yerel çalıştırılabilen RAG (Retrieval-Augmented Generation) mimarisi ile geliştirilmiştir.

## 🚀 Özellikler

- 🔍 Türkçe PDF belgelerden bilgi çıkarımı
- 🧠 LLM + RAG mimarisi
- 📦 Lokal çalışma — gizlilik dostu
- 🧾 Kolay veri güncelleme (PDF klasörü ile)
- 🖥️ Basit bir arayüz üzerinden kullanım (Streamlit)

## 📁 Proje Yapısı

```
.
├── data/
│   └── pdfs/            # Cevaplanacak içerikleri barındıran PDF dosyaları
├── src/
│   ├── ingest.py        # PDF'leri vektörleştiren ve veri tabanına kaydeden script
│   ├── qa.py            # Soru-cevap işlemlerini yöneten script
│   └── app.py           # Streamlit arayüzü
├── requirements.txt     # Gerekli Python paketleri
└── README.md
```

## 🛠️ Kurulum

### 1. Ortamı Hazırla

```bash
git clone https://github.com/ErenErenturk/llm-turkish-faq-bot.git
cd llm-turkish-faq-bot
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. PDF'leri Yükle

`data/pdfs/` klasörüne Türkçe PDF dosyalarını koyun.

### 3. Vektörleri Oluştur

```bash
python src/ingest.py
```

### 4. Chatbot'u Başlat

```bash
streamlit run src/app.py
```

## 🧠 Kullanılan Teknolojiler

- **LangChain**: RAG yapısı ve LLM entegrasyonu
- **FAISS / Chroma**: Vektör veritabanı
- **Streamlit**: Web arayüzü
- **PyMuPDF**: PDF işleme

## 💡 Geliştirme Fikirleri

- 🔄 Daha iyi sonuçlar için model kalibrasyonu
- 🤖 Farklı Türkçe LLM modellerinin karşılaştırılması
- 🌐 Belge dışında (örneğin websitesi veya veri tabanı) bilgi çekme özelliği
- 📊 Arayüzde kullanıcı analitikleri

## 🧑‍💻 Katkıda Bulun

Pull request’ler ve issue’lar her zaman memnuniyetle karşılanır.

---
