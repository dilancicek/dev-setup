# Bölüm 1.2 - CLI Veri İşleme Egzersizi Raporu

Bu belgede, veri mühendisliği staj görevi kapsamında terminal kullanılarak yapılan veri işleme adımları ve komutları belgelenmiştir.

```bash
# 1. 150.000 satırlık ham veri setinin satır sayısını doğrulama
wc -l veri.csv

# 2. Verinin 2. kolonunu alıp, en çok tekrar edenleri bulma ve sıralama
cut -d',' -f2 veri.csv | sort | uniq -c | sort -nr | head -n 10

# 3. İstenen koşulu ("True") sağlayan satırları filtreleme
grep "True" veri.csv > filtrelenmis_veri.csv

# 4. Dosyaları ortak ID (1. kolon) üzerinden birleştirme (Join)
join -t',' -1 1 -2 1 <(sort -t',' -k1,1 veri.csv) <(sort -t',' -k1,1 ek_bilgi.csv) > birlesmis_veri.csv

```
