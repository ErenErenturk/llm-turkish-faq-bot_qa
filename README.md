# 🇹🇷 Türkçe PDF Soru-Cevap Botu (Qwen 7B Chat + Streamlit)

Bu proje, yüklenen PDF dosyaları üzerinden Türkçe doğal dilde soru-cevap yapılmasına olanak tanır.  
Backend'de `Qwen 7B Chat` modeli kullanılarak belge içeriği analiz edilir, türü tespit edilir ve bağlama uygun cevaplar üretilir.

## 🚀 Özellikler

- 📄 **PDF'den metin çıkarma** (`PyMuPDF`)
- 🤖 **LLM destekli Soru-Cevap** (`Qwen 7B Chat` - Ollama üzerinden)
- 🧠 **Belge türü otomatik tespiti** (özgeçmiş, fatura, sözleşme vs.)
- 📝 **Prompt özelleştirme** belge türüne göre
- 💻 **Streamlit arayüzü**

## 🧠 Kullanılan Teknolojiler

- `Ollama` (lokal LLM servisi)
- `Qwen:7b-chat` (çok dilli LLM, Türkçe uyumlu)
- `sentence-transformers` (embedding işlemleri için)
- `FAISS` (vektör arama)
- `Streamlit` (web arayüz)
- `fitz` (PyMuPDF)

## 🔧 Kurulum

1. Ollama'yı indir: [https://ollama.com](https://ollama.com)
2. Qwen modelini indir:
```bash
ollama pull qwen:7b-chat
```
3. Ortamı kur:
```bash
pip install -r requirements.txt
```
4. Uygulamayı başlat:
```bash
streamlit run src/app.py
```

## 📁 Proje Yapısı

```
.
├── src/
│   ├── app.py                 # Streamlit arayüzü
│   ├── qa_pipeline.py         # QA iş akışı
│   ├── prompt_builder.py      # Belge türüne göre prompt oluşturucu
│   └── document_types.json    # Belge sınıflandırma anahtar kelimeleri
├── requirements.txt
└── README.md
```

## ✍️ Örnek Kullanım

- **PDF Yükle:** `Eren_Erenturk_CV.pdf`
- **Soru Sor:** "Bu kişi kimdir ve uzmanlık alanı nedir?"
- **Cevap Al:** Model, belgeyi özetler, türünü tespit eder ve sorunu belgede geçen bilgilere göre cevaplar.

## 🤝 Katkı

PR'lar, öneriler ve model iyileştirme fikirleri memnuniyetle kabul edilir.

## 📜 Lisans

MIT Lisansı
