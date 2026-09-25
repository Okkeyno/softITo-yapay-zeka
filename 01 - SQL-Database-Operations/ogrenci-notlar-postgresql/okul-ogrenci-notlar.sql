CREATE DATABASE okul;

CREATE TABLE ogrenci(
	id SERIAL PRIMARY KEY,
	ad VARCHAR(50),
	not_ort NUMERIC(4,2),
	bolum VARCHAR(50)
);

CREATE TABLE bolum(
	id SERIAL PRIMARY KEY,
	ad VARCHAR(50) NOT NULL
);

CREATE TABLE ders(
	id SERIAL PRIMARY KEY,
	ad VARCHAR(100) NOT NULL,
	kredi INT,
	bolum_id INT REFERENCES bolum(id)
);

CREATE TABLE kayit(
	ogrenci_id INT REFERENCES ogrenci(id) ON DELETE CASCADE,
	ders_id INT REFERENCES ders(id) ON DELETE CASCADE,
	notu INT,
	donem VARCHAR(25),
	PRIMARY KEY (ogrenci_id, ders_id)
	
);


-- 1. BÖLÜM VERİLERİ
INSERT INTO bolum (id, ad) VALUES
(1, 'Şanssızlık Mühendisliği'),
(2, 'Dedikodu Bilimleri ve Stratejik'),
(3, 'Uykusuzluk ve Gece 3 Mesajları'),
(4, 'Fast Food Felsefesi ve Ketçap');


-- 2. ÖĞRENCİ VERİLERİ
INSERT INTO ogrenci (ad, not_ort) VALUES
('Zıpırcan', 68.30),
('Cırcırböceği Cemal', 42.10),
('Pırtlayan Pınar', 12.50),
('Makyajlı Muhtar', 88.90),
('Çorapsız Çetin', 50.00),
('Tostçu Tayfun', 31.80),
('Biberli Bedriye', 74.20),
('Hapşıran Hikmet', 61.70);


-- 3. DERS VERİLERİ
INSERT INTO ders (ad, kredi, bolum_id) VALUES
('Kopya Çekme Teknikleri 101', 4, 1),
('Açık Unutulan Muslukları Kapatma Sanatı', 3, 1),
('Yan Masadakinin Konuşmasını Dinleme ve Raporlama', 5, 2),
('Sabah 8.00 Dersine Gidiyormuş Gibi Görünme', 2, 3),
('Ketçap ve Mayonez Dökülme Risk Analizi', 4, 4),
('Sosyal Medyada Eski Sevgilinin Profilini İnceleme', 3, 2);


-- 4. KAYIT (NOT VE DÖNEM) VERİLERİ
INSERT INTO kayit (ogrenci_id, ders_id, notu, donem) VALUES
(1, 1, 45, '2025-Güz'),
(1, 2, 70, '2025-Güz'),
(2, 3, 90, '2025-Güz'),
(3, 4, 15, '2026-Bahar'),
(4, 5, 88, '2026-Bahar'),
(5, 1, 50, '2025-Güz'),
(6, 5, 30, '2026-Bahar'),
(7, 6, 95, '2026-Bahar'),
(8, 2, 62, '2025-Güz');


SELECT o.ad AS ogrenci , d.ad AS Ders , k.notu
FROM kayit k
JOIN ogrenci o on k.ogrenci_id = o.id
JOIN ders d ON k.ders_id = d.id
ORDER  BY o.ad, k.notu  DESC


-- Not ortalaması 50'den büyük veya ismi 'P' harfi ile başlayan öğrencilerin listelenmesi:
SELECT * FROM ogrenci
WHERE not_ort > 50 OR ad LIKE ('P%')

-- Öğrencilerin aldığı dersler, bu derslerin notları, kredileri ve 
-- ait oldukları bölümlerin detaylı raporu:

SELECT o.ad AS ogrenci_adi, o.not_ort, d.ad AS ders_adi, k.notu AS ders_notu, b.ad AS bolum_adi 
FROM kayit k 
INNER JOIN ogrenci o ON k.ogrenci_id = o.id 
INNER JOIN ders d ON k.ders_id = d.id 
INNER JOIN bolum b ON d.bolum_id = b.id 
ORDER BY k.notu DESC;

-- Gruplama ve Şartlı Filtreleme
-- Bölüm bazlı toplam ders sayısı ve ortalama kredi değerleri 
-- (Sadece toplam kredisi 3'ten büyük bölümler):

SELECT b.ad AS bolum_adi, COUNT(d.id) AS toplam_ders_sayisi, 
ROUND(AVG(d.kredi), 2) AS ortalama_kredi 
FROM bolum b 
LEFT JOIN ders d ON b.id = d.bolum_id 
GROUP BY b.id, b.ad 
HAVING SUM(d.kredi) > 3;

-- Öğrencileri aldıkları ders notlarına göre sıralayan ve 
-- sınıf ortalamasının üzerinde not alanları filtreleyen sorgu
 
WITH BasariSiralamasi AS (SELECT o.ad AS ogrenci_adi, d.ad AS ders_adi, k.notu, 
AVG(k.notu) OVER() AS genel_ders_notu_ortalamasi, 
ROW_NUMBER() OVER(ORDER BY k.notu DESC) AS derece 
FROM kayit k 
JOIN ogrenci o ON k.ogrenci_id = o.id 
JOIN ders d ON k.ders_id = d.id ) 
SELECT derece, ogrenci_adi, ders_adi, notu, ROUND(genel_ders_notu_ortalamasi, 2) AS sinif_ortalamasi 
FROM BasariSiralamasi 
WHERE notu > genel_ders_notu_ortalamasi;


-- Sisteme kayıtlı olup henüz herhangi bir ders kaydı bulunmayan öğrencilerin tespiti:
SELECT id, ad, not_ort 
FROM ogrenci o 
WHERE NOT EXISTS ( SELECT 1 FROM kayit k WHERE k.ogrenci_id = o.id );