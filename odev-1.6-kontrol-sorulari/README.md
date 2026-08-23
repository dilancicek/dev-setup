# 📝 Ödev 1.6: Kontrol Soruları

**1. `pip install` ile `uv add` arasında bağımlılık çözümlemesi açısından fark nedir?**
`pip install`'ın da aslında kendi içinde bir bağımlılık çözümleyicisi (resolver) var ancak karmaşık alt paketlerde bazen kafası karışıp sürüm çakışmalarına sebep olabiliyor. Asıl fark stratejide ve kilit (lock) dosyasında yatıyor; `uv add` gelişmiş bir çözümleme stratejisiyle hem çok daha hızlı çalışıyor hem de paketi eklerken arkada hemen kesin bir kilit dosyası (`uv.lock`) oluşturuyor. Kimin hangi sürümle çalışacağını kesinleştirdiği için "benim bilgisayarımda çalışıyordu, sende niye bozuldu" sorunlarını çözüyor.

**2. `__pycache__` neden `.gitignore`'da olmalı?**
Çünkü bunların bizim yazdığımız asıl kodla bir ilgisi yok. Python'ın kodu daha hızlı çalıştırmak için kendi kendine oluşturduğu geçici dosyalar. Bunları GitHub'a atmak hem depoyu boşuna çöplüğe çevirip şişirir, hem de ekipteki başka birinin bilgisayarındaki geçici dosyalarla çakışıp durduk yere conflict (çakışma) çıkartır.

**3. Docker'da `COPY requirements.txt` ile `COPY .` sırasını neden ayırıyoruz?**
Tamamen Docker'ın cache (önbellek) mantığını kendi lehimize kullanmak için. Eğer her şeyi tek seferde `COPY .` ile atarsak, koddaki küçücük bir yazım hatasını bile düzeltip tekrar build aldığımızda, Docker en baştan bütün kütüphaneleri indirmeye çalışır ve saatler sürer. Önce requirements'ı kopyalayıp paketleri kuruyoruz ki sadece kodu değiştirdiğimizde kütüphane indirme kısmını cache'den tak diye geçebilsin.

**4. `git rebase` ile `git merge` arasındaki farkı ekip çalışması bağlamında anlat.**
`git merge` dalları birleştirirken fazladan bir "merge commiti" atar, bu da geçmişi biraz karışık ve dallı budaklı gösterir. `git rebase` ise bizim commitlerimizi alıp doğrudan diğer dalın ucuna ekler, yani git geçmişi dümdüz ve tertemiz bir çizgi gibi görünür. Ama ortak çalışılan bir branch'te (mesela master'da) rebase yapmak tehlikelidir; başkasının da üzerinde çalıştığı geçmişi değiştireceği için takım arkadaşlarının kodlarını patlatabilir.
