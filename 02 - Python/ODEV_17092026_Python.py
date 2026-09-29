# 1. Pandas Kurulumu ve İçe Aktarma Pandas kütüphanesini pd takma adıyla içe aktaran kodu yazın. 
# Pandas'ın hangi versiyonda kurulu olduğunu pd.version ile kontrol edin.

import pandas as pd

print("Pandas Versiyonu: ", pd.__version__)


# 2. Series — Tek Boyutlu Veri Yapısı [100, 200, 300, 400] değerlerinden bir Series oluşturup yazdırın. 
# Şehir isimlerini index, nüfuslarını değer olarak kullanan bir Series oluşturun (en az 4 şehir). 
# Oluşturduğunuz Series'ten belirli bir şehrin nüfusunu index adıyla seçip yazdırın. 
# Bir Series'teki tüm değerlerin toplamını .sum() ile bulun.

sayilar = pd.Series([100, 200, 300, 400])
print("Sayılar Series:", sayilar)

sehirler = pd.Series(
    [15800000, 5800000, 4400000, 2600000],
    index=["İstanbul", "Ankara", "İzmir", "Bursa"]
)
print( sehirler)

print("\nAnkara'nın Nüfusu:", sehirler["Ankara"])

# Nüfusların toplamı
toplam_nufus = sehirler.sum()
print("Toplam Nüfus:", toplam_nufus)


# 3. DataFrame — Tablo Yapısı urun, fiyat ve stok sütunlarından oluşan, en az 5 satırlık bir DataFrame oluşturun. 
# Sınıf arkadaşlarınızın isim, yaş ve bölüm bilgilerini içeren bir DataFrame oluşturup yazdırın. 
# Oluşturduğunuz DataFrame'in kaç satır ve kaç sütundan oluştuğunu söyleyin 
# (koda bakmadan tahmin edip sonra kontrol edin). 

urunler_df = pd.DataFrame({
    "urun": ["Laptop", "Mouse", "Klavye", "Monitör", "Kulaklık"],
    "fiyat": [25000, 450, 850, 4500, 1200],
    "stok": [15, 50, 30, 20, 40]
})
print("Ürünler DataFrame:\n", urunler_df)

ogrenciler_df = pd.DataFrame({
    "isim": ["Ahmet", "Ayşe", "Mehmet", "Fatma", "Ali"],
    "yas": [22, 20, 25, 21, 23],
    "bolum": ["Endüstri Müh.", "Bilgisayar", "Makine", "Endüstri", "Yazılım"]
})
print("Öğrenciler DataFrame:\n", ogrenciler_df)

# Tahmin: 5 satır, 3 sütun var.
print("DataFrame Boyutu (Satır, Sütun):", ogrenciler_df.shape)


# 4. CSV Dosyası Okuma ve Yazma Sorular 3'te oluşturduğunuz DataFrame'i ogrenciler.csv adıyla kaydedin. 
# Kaydettiğiniz CSV dosyasını tekrar okuyup ekrana yazdırın. 
# index=False parametresini kullanmadan bir CSV kaydedin ve dosyayı açıp aradaki farkı gözlemleyin.

# index=False ile temiz bir şekilde kaydetme
ogrenciler_df.to_csv("ogrenciler.csv", index=False)

okunan_df = pd.read_csv("ogrenciler.csv")
print("Okunan CSV Dosyası:\n", okunan_df)

# index=False kullanılmadan kaydetme
ogrenciler_df.to_csv("ogrenciler_indexli.csv")
okunan_indexli_df = pd.read_csv("ogrenciler_indexli.csv")
print("index=False Olmadan Okunan CSV:\n", okunan_indexli_df)


# 5. Veriyi İnceleme (İlk Bakış) Bir DataFrame oluşturup .head() ve .tail() ile 
# ilk 3 ve son 2 satırını görüntüleyin. 
# .shape ile DataFrame'in boyutunu öğrenin. 
# .info() kullanarak sütunların veri tiplerini inceleyin. 
# .describe() ile sayısal bir sütunun (örneğin yaş veya maaş) ortalama, min ve max değerlerini bulun.

df = pd.DataFrame({
    "isim": ["Ahmet", "Ayşe", "Mehmet", "Fatma", "Ali", "Can"],
    "yas": [26, 17, 30, 19, 42, 28],
    "sehir": ["İstanbul", "Ankara", "İstanbul", "İzmir", "İstanbul", "Ankara"],
    "maas": [25000, 15000, 35000, 22000, 40000, 28000]
})

# İlk 3 satır
print("İlk 3 Satır:\n", df.head(3))

# Son 2 satır
print("Son 2 Satır:\n", df.tail(2))

print("DataFrame Boyutu:", df.shape)

# Veri tipleri ve genel bilgi
print("Veri Bilgisi:")
df.info()

# Sayısal sütunun özeti
print("Maaş Sütunu İstatistikleri:\n", df["maas"].describe())


# 6. Sütun ve Satır Seçme Bir DataFrame'den sadece "isim" sütununu seçip yazdırın. 
# "isim" ve "yas" sütunlarını birlikte seçip yazdırın. 
# .loc[] kullanarak DataFrame'in ilk 3 satırını seçin. 
# .iloc[] kullanarak 2. satır ile 2. sütunun kesiştiği değeri bulun.

# Sadece "isim" sütununu seçme
print("Sadece İsim Sütunu:\n", df["isim"])

# "isim" ve "yas" sütunları
print("İsim ve Yaş Sütunları:\n", df[["isim", "yas"]])


print("İlk 3 Satır:\n", df.loc[0:2])

print("2. Satır ve 2. Sütundaki Değer:", df.iloc[1, 1])


# 7. Filtreleme (Koşullu Seçim) Yaşı 25'ten büyük olan kişileri filtreleyip listeleyin. 
# Maaşı 20000 ile 30000 arasında olan kişileri bulun (iki koşulu & ile birleştirin). 
# Belirli bir şehirde (örneğin "İstanbul") yaşayan kişileri filtreleyin. 
# Yaşı 20'den küçük VEYA 40'tan büyük olanları | operatörüyle bulun.

# Yaşı 25'ten büyük olanlar
print("Yaşı 25'ten Büyük Olanlar: ", df[df["yas"] > 25])

# Maaşı 20000 ile 30000 arasında olanlar
print("Maaşı 20.000 - 30.000 Arasında Olanlar:", df[(df["maas"] >= 20000) & (df["maas"] <= 30000)])

# Şehri İstanbul olanlar
print("İstanbul'da Yaşayanlar:\n", df[df["sehir"] == "İstanbul"])

# Yaşı 20den küçük veya 40an büyük olanlar
print("Yaşı < 20 veya > 40 Olanlar:\n", df[(df["yas"] < 20) | (df["yas"] > 40)])


# 8. Yeni Sütun Ekleme ve Güncelleme Bir DataFrame'e "dogum_yili" sütunu ekleyin (2026 - yas formülüyle). 
# Maaş sütunundaki tüm değerleri %10 artırıp güncelleyin. 
# apply() ve lambda kullanarak yaşı 18'den büyük olanlara "Yetişkin", 
# küçük olanlara "Çocuk" yazan yeni bir sütun oluşturun.

df["dogum_yili"] = 2026 - df["yas"]

# Maaşı %10 artırma
df["maas"] = df["maas"] * 1.10

df["durum"] = df["yas"].apply(lambda y: "Yetişkin" if y > 18 else "Çocuk")

print("Güncellenmiş Tablo:", df)


# 9. Sıralama Bir DataFrame'i "yas" sütununa göre küçükten büyüğe sıralayın. 
# Aynı DataFrame'i "maas" sütununa göre büyükten küçüğe sıralayın. 
# İki sütuna göre aynı anda sıralama yapın (örneğin önce "sehir", sonra "yas").

# Yaşa göre küçükten büyüğe sıralama
print("Yaş Sıralaması:", df.sort_values(by="yas"))

# Maaşa göre büyükten küçüğe
print("Maaşa Göre Büyükten Küçüğe:", df.sort_values(by="maas", ascending=False))

# İki sütuna göre aynı anda sıralama 
print("Önce Şehir, Sonra Yaşa Göre Sıralama:", df.sort_values(by=["sehir", "yas"]))