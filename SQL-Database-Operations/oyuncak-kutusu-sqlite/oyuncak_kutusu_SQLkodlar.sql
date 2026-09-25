-- Bölüm 1 – Tablo kurma 
-- oyuncaklar adında bir tablo oluştur. Şu sütunlar olsun:
-- id: otomatik artan numara
-- isim: yazı, boş bırakılamaz
-- cesit: yazı
-- fiyat: sayı, 0'dan büyük olmalı
-- renk: yazı, yazılmazsa kırmızı olsun

CREATE TABLE oyuncaklar(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	isim TEXT NOT NULL,
	cesit TEXT,
	fiyat INTEGER CHECK(fiyat>0),
	renk text DEFAULT 'Kırmızı'
);


-- Bölüm 2 – Ekleme
-- Kutuya Şimşek adlı 50 liralık bir araba ekle (rengini yazma, ne olacak?).
INSERT INTO oyuncaklar('isim','fiyat') VALUES ('Şimşek',50); -- renk default olarak KIRMIZI olacaktır.

-- Tek komutla şu dört oyuncağı ekle: 
-- Ayıcık (peluş, 80, kahverengi), Kale Seti (lego, 150, gri), 
-- Zıpzıp (top, 20, sarı), Barbi (bebek, 90, pembe).
INSERT INTO oyuncaklar('isim','cesit','fiyat','renk') 
VALUES ('Ayıcık','peluş', 80, 'kahverengi'), ('Kale Seti','lego', 150, 'gri'), 
('Zıpzıp', 'top', 20, 'sarı'), ('Barbi','bebek', 90, 'pembe');

-- Bölüm 3 – Bulma
-- Kutudaki tüm oyuncakları göster.
SELECT * FROM oyuncaklar;
-- Fiyatı 80 lira ve üstü olan oyuncakların sadece ismini ve fiyatını göster.
SELECT isim, fiyat FROM oyuncaklar
WHERE fiyat >= 80;
-- En pahalı 2 oyuncağı listele.
SELECT * from oyuncaklar
ORDER BY fiyat DESC
LIMIT 2;
-- İsmi Z harfiyle başlayan oyuncakları bul.
SELECT * FROM oyuncaklar
WHERE isim like ('Z%');
-- Sadece araba ve topları göster.
SELECT * FROM oyuncaklar
WHERE cesit='araba' or cesit ='top';
-- Fiyatı 20 ile 60 lira arasında olanları listele.
SELECT * FROM oyuncaklar
WHERE fiyat BETWEEN 20 AND 60;


-- Bölüm 4 – Değiştirme ve silme 
-- Şimşek'in rengini mavi yap.
UPDATE oyuncaklar SET renk='mavi';
-- Zıpzıp'ı kutudan çıkar (sil).
-- Bonus: DELETE FROM oyuncaklar; yazarsan ne olur? Denemeden önce tahmin et.
DELETE FROM oyuncaklar WHERE isim='Zıpzıp'  -- Satır silinir ama ID numarası atlayarak devam eder.

-- Bölüm 5 – Tabloyu düzenleme
-- Tabloya kimin adında yeni bir sütun ekle.
ALTER TABLE oyuncaklar ADD COLUMN 'kimin' TEXT;
-- Kale Seti'nin sahibini Ali yap.
UPDATE oyuncaklar SET kimin='Ali' WHERE isim='Kale Seti';
-- cesit sütununun adını tur olarak değiştir.
ALTER TABLE oyuncaklar RENAME COLUMN 'cesit' to 'tur'


