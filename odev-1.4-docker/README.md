# Ödev 1.4 - Docker Basics & FastAPI Containerization

Bu proje, bir FastAPI uygulamasının Docker kullanılarak konteynerize edilmesini ve Docker Compose ile bir PostgreSQL veritabanı ile entegre çalıştırılmasını içermektedir.

## 🚀 Teknolojiler
- **Backend:** Python 3.11, FastAPI, Uvicorn
- **Veritabanı:** PostgreSQL (15-alpine)
- **Altyapı:** Docker, Docker Compose

## 📦 Multi-stage Build ve Optimizasyon
İmaj boyutunu minimuma indirmek ve gereksiz cache dosyalarından kurtulmak amacıyla `Dockerfile` içerisinde **Multi-stage (Çok Aşamalı)** mimari kullanılmıştır. `builder` aşamasında kütüphaneler kurulmuş, `runner` aşamasında ise sadece çalışan dosyalar transfer edilmiştir.

**Boyut Karşılaştırması:**
- 🔴 Optimizasyon Öncesi Standart İmaj Beklentisi: **~950 MB**
- 🟢 Multi-stage Build Sonrası İmaj Boyutu: **57 MB**

## 🛠️ Kurulum ve Çalıştırma

Projeyi ve veritabanını aynı anda arka planda çalıştırmak için terminalde şu komutu kullanabilirsiniz:
`docker compose up -d`

Servislerin durumunu kontrol etmek için:
`docker ps`

Sistemi durdurmak ve konteynerleri kaldırmak için:
`docker compose down`
