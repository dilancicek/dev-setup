# Bölüm 1.2 - CLI Veri İşleme Egzersizi Raporu

Bu belgede, veri mühendisliği görevi kapsamında terminal (Git Bash) kullanılarak yapılan veri işleme adımları, uygulanan komutlar ve bu komutların gerçek terminal çıktıları belgelenmiştir.

## 1. Ham Veri Setinin Satır Sayısını Doğrulama
150.000 satırlık verinin (1 satır başlık dahil) kontrolü yapılmıştır.

**Komut:**
```bash
wc -l veri.csv
```

**Çıktı (Kanıt):**
```text
150001 veri.csv
```

---

## 2. Kolon Frekans Tablosu (En Çok Tekrar Edenler)
Ödev yönergesine uygun olarak 3. kolon (`deger`) alınmış, en çok tekrar eden ilk 10 değer bulunmuş ve sıralanmıştır.

**Komut:**
```bash
cut -d',' -f3 veri.csv | sort | uniq -c | sort -nr | head -n 10
```

**Çıktı (Kanıt):**
```text
    355 199
    352 87
    349 436
    349 124
    347 333
    346 86
    346 67
    345 74
    344 89
    344 83
```

---

## 3. İstenen Koşulu ("True") Sağlayan Satırları Filtreleme
3. kolonda ("deger" kolonu) "True" kelimesi aranmıştır.

**Mühendislik Notu:** Verinin yapısı (`head -n 5 veri.csv`) incelendiğinde 3. kolonun tamamen sayısal değerlerden (`28, 327, 425...`) oluştuğu görülmüştür. Bu nedenle tüm dosyada rastgele `grep "True"` yapmak yerine, sadece 3. kolona `awk` ile bakılmış ve beklenen şekilde **0** eşleşme bulunmuştur.

**Komut:**
```bash
awk -F',' '$3 == "True"' veri.csv > filtrelenmis_veri.csv
wc -l filtrelenmis_veri.csv
```

**Çıktı (Kanıt):**
```text
0 filtrelenmis_veri.csv
```

---

## 4. Ortak ID (1. Kolon) Üzerinden Dosyaları Birleştirme (Join)
İki veri seti `id` kolonları üzerinden eşleştirilerek birleştirilmiş ve elde edilen kesişim satır sayısı doğrulanmıştır.

**Komut:**
```bash
join -t',' -1 1 -2 1 <(sort -t',' -k1,1 veri.csv) <(sort -t',' -k1,1 ek_bilgi.csv) > birlesmis_veri.csv
wc -l birlesmis_veri.csv
```

**Çıktı (Kanıt):**
```text
1002 birlesmis_veri.csv
```
