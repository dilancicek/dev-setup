# 📦 Python Bağımlılık Yönetimi Araştırması: uv, Poetry, pip-tools ve Conda

Python ekosisteminde projelerin bağımlılıklarını yönetmek, alt sürümleri sabitlemek (lock) ve tekrarlanabilir geliştirme ortamları kurmak kritik bir mühendislik prensibidir. Bu doğrultuda endüstri standardı haline gelmiş dört farklı aracın (uv, Poetry, pip-tools, Conda) mimarileri, kullanım senaryoları ve yerel hız testi performansları aşağıda incelenmiştir.

## 🧪 1. Laboratuvar Ölçümleri ve Performans Testi

Bu araştırma kapsamında, araçların bağımlılık çözümleme (resolution) ve sabitleme (lock) performanslarını ölçmek amacıyla yerel bir Windows PowerShell ortamı kurulmuştur. `FastAPI` paketinin alt bağımlılıklarını çözümleme işlemi için `Measure-Command` aracı ile elde edilen gerçek dünya verileri şöyledir:

| Paket Yöneticisi | Kullanılan Komut | Tamamlanma Süresi |
| :--- | :--- | :--- |
| **uv** | `uv pip compile` | **2.14 Saniye** |
| **Poetry** | `poetry lock` | 2.30 Saniye |
| **pip-tools** | `pip-compile` | 6.60 Saniye |

Test sonuçlarına göre, Astral ekibi tarafından Rust diliyle baştan yazılan **uv**, Python paket yönetimindeki standart araçlara kıyasla ciddi bir performans avantajı sağlamıştır. **Poetry** kapsamlı mimarisine rağmen oldukça tatmin edici bir hız sunarken, geleneksel Python ekosistemini kullanan **pip-tools** çözümleme aşamasında en yavaş araç olmuştur.

> **📌 Not (Conda Ölçümü Hakkında):**
> Başlıkta incelenen araçlar arasında Conda bulunmasına rağmen hız ölçümü tablosuna dahil edilmemiştir. Bunun sebebi; Conda'nın standart Python paket yöneticilerinden (pip, uv vb.) farklı olarak işletim sistemi seviyesindeki kütüphaneleri (C/C++ vb.) de içeren çok daha ağır bir ortam çözme (environment resolution) mimarisine sahip olmasıdır. Bu nedenle diğer hafif araçlarla saniye bazında birebir hız kıyaslamasına sokulması adil ve pratik bir metrik sunmayacağı için ölçüm dışı bırakılmıştır.

## ⚙️ 2. Araçların Karakteristik Özellikleri

*   **uv:** Son derece hızlıdır ve `pip` ile `pip-tools` iş akışlarına doğrudan (drop-in replacement) entegre olacak şekilde tasarlanmıştır. Dış bir bağımlılık gerektirmez.
*   **Poetry:** Sadece paket kurulumu yapmaz; `pyproject.toml` üzerinden tüm projeyi yapılandırır, sanal ortamı otomatik yönetir ve kodun PyPI gibi repolarda yayınlanması için paketleme (build) süreçlerini üstlenir.
*   **pip-tools:** Sadeliği merkeze alır. Karmaşık konfigürasyonlar yerine, geleneksel `requirements.txt` standardını koruyarak sadece paketlerin alt versiyonlarını sabitleme görevine odaklanır.
*   **Conda:** Sadece bir Python paket yöneticisi değil, dil bağımsız bir çevre (environment) yöneticisidir. İşletim sistemi seviyesindeki kütüphaneleri ve derlenmiş C/C++ binary dosyalarını da yönetebilir.

## 🎯 3. Hangi Durumda Hangisi Seçilmeli?

*   **Makine Öğrenmesi ve Veri Bilimi (Conda):** Projenizde TensorFlow, PyTorch veya GPU hızlandırma gerektiren (CUDA, cuDNN) karmaşık sistem seviyesi kütüphaneler varsa kesinlikle Conda tercih edilmelidir.
*   **Kütüphane Geliştirme ve Dağıtım (Poetry):** Açık kaynaklı bir araç yazıyorsanız ve bunu standart bir yapıda paketleyip yayınlamak istiyorsanız, tüm proje yaşam döngüsünü yöneten Poetry en iyi seçenektir.
*   **Modern Web ve Mikroservisler (uv):** CI/CD süreçlerinde hızın kritik olduğu, Docker imajlarının hızlıca derlenmesi gereken FastAPI veya Django gibi web projelerinde, hız avantajından dolayı uv seçilmelidir.
*   **Eski Projeleri Modernize Etme (pip-tools):** Halihazırda eski bir `requirements.txt` yapısı kullanan ve radikal bir araç değişikliğine gitmek istemeyen ekipler için en güvenli liman pip-tools aracıdır.
