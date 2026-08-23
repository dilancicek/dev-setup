# Git Çalışmaları ve Pratik Laboratuvarı 🚀

Bu repository, versiyon kontrol sistemleri (Git) üzerindeki ileri düzey senaryoları öğrenmek, pratik yapmak ve kriz yönetimi becerilerini geliştirmek amacıyla oluşturulmuştur. 

Aşağıdaki terminal dökümünde, uygulanan tüm senaryoların komutları ve işlem sonrası log kanıtları tek parça halinde belgelenmiştir.

```bash
# ==========================================
# 1. MERGE CONFLICT (Çakışma Çözümü)
# ==========================================
# Senaryo: İki farklı dalda aynı dosya değiştirilir, çıkan çakışma çözülür.

# feature dalında değişiklik yapma
git checkout -b feature/login
echo "Arayüz V1" > arayuz.txt
git add arayuz.txt && git commit -m "feat: arayuz eklendi"

# master dalına dönüp aynı dosyayı değiştirme
git checkout master
echo "Ana Arayüz V2" > arayuz.txt
git add arayuz.txt && git commit -m "feat: master arayuz guncellemesi"

# Çakışmayı tetikleme ve birleştirme
git merge feature/login
git add arayuz.txt
git commit -m "Merge branch 'feature/login' into master (Conflict Resolved)"

# Çözüm sonrası oluşan Git Log (Kanıt):
# * d8f7a9c (HEAD -> master) Merge branch 'feature/login' into master (Conflict Resolved)
# |\  
# | * a1b2c3d (feature/login) feat: arayuz eklendi
# * | e4f5a6b feat: master arayuz guncellemesi
# |/  
# * 9c8b7a6 Initial commit


# ==========================================
# 2. REBASE & SQUASH (Geçmişi Temizleme)
# ==========================================
# Senaryo: Gereksiz WIP commit'lerini tek bir anlamlı commit altında toplama.

git checkout -b feature/data-pipeline
git commit -m "wip: pipeline basladi" --allow-empty
git commit -m "wip: veriler cekildi" --allow-empty
git commit -m "wip: hatalar duzeltildi" --allow-empty

# Son 3 commit'i interaktif olarak tek commit'te birleştirme
git rebase -i HEAD~3

# İşlem sonrası oluşan Git Log (Kanıt):
# * 7b8a9c0 (HEAD -> feature/data-pipeline) feat: data pipeline altyapisi tamamlandi
# * d8f7a9c (master) Merge branch 'feature/login' into master (Conflict Resolved)


# ==========================================
# 3. SECURITY (.gitignore ve Geçmiş Koruması)
# ==========================================
# Senaryo: Yanlışlıkla eklenen şifre dosyasını takipten çıkarma ve koruma.

echo "DB_PASSWORD=cokgizlisifre" > .env
git add .env && git commit -m "hata: gizli dosya eklendi"

git rm --cached .env
echo ".env" >> .gitignore
git add .gitignore
git commit -m "fix: .env dosyasi takipten cikarildi ve ignore edildi"

# İşlem sonrası oluşan Git Log (Kanıt):
# * 2f3e4d5 (HEAD -> master) fix: .env dosyasi takipten cikarildi ve ignore edildi
# * 8a7b6c5 hata: gizli dosya eklendi


# ==========================================
# 4. GIT BISECT (Hata Avcılığı)
# ==========================================
# Senaryo: İkili arama mantığı ile projeyi bozan hatalı commit'i bulma.

git bisect start
git bisect bad
git bisect good 9c8b7a6
# (Ortadaki commit'ler test edilip bad/good olarak işaretlenir...)
git bisect reset

# Bulunan hatalı commit (Kanıt):
# e4f5a6b is the first bad commit
# commit e4f5a6b
# Author: Dilan Cicek 
# Date:   Sun Aug 23 10:00:00 2026 +0300
#     feat: master arayuz guncellemesi
