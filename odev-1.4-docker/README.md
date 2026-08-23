# Ödev 1.4 - Docker Basics & FastAPI Containerization

Bu proje, bir FastAPI uygulamasının Docker kullanılarak konteynerize edilmesini ve Docker Compose ile bir PostgreSQL veritabanı ile entegre çalıştırılmasını içermektedir.

Aşağıdaki terminal dökümünde teknolojiler, multi-stage build optimizasyon raporu ve komut kılavuzu tek parça halinde belgelenmiştir:

```text
# ==========================================
# 1. TEKNOLOJİ STACK VE SÜRÜM BİLGİSİ
# ==========================================
- Backend: Python 3.12, FastAPI, Uvicorn
- Veritabanı: PostgreSQL (15-alpine)
- Altyapı: Docker, Docker Compose


# ==========================================
# 2. İMAJ BOYUTU OPTİMİZASYON KANITI (Multi-stage)
# ==========================================
# Standart imaj ile multi-stage optimize imajın gerçek ölçüm sonuçları:

REPOSITORY   TAG       DISK USAGE   CONTENT SIZE
api-eski     latest    1.69GB       439MB
api-yeni     latest    228MB        54.6MB

- Optimizasyon Öncesi (api-eski): Standart Python 3.12 imajı -> 1.69 GB
- Optimizasyon Sonrası (api-yeni): Multi-stage slim mimari -> 228 MB
- Tasarruf: %85+ oranında disk alanı kazanımı sağlanmıştır.


# ==========================================
# 3. KURULUM VE ÇALIŞTIRMA KOMUTLARI
# ==========================================
# Projeyi ve veritabanını arka planda ayağa kaldırma:
docker compose up -d

# Servislerin durumunu kontrol etme:
docker ps

# Sistemi durdurma ve konteynerleri kaldırma:
docker compose down
