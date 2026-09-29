# Bonus Mini Ödev: Sınıfınızdaki (hayali) 6 öğrencinin isim, üç ders notu ve şehir bilgisini içeren 
# bir DataFrame oluşturun. 
# Ortalaması 70'in üzerinde olan öğrencileri filtreleyip, sonucu yaşa göre sıralayıp yazdırın.

import pandas as pd

df = pd.DataFrame({
    "isim": ["Ahmet", "Ayşe", "Mehmet", "Fatma", "Ali", "Zeynep"],
    "ders1": [80, 95, 60, 85, 50, 90],
    "ders2": [75, 90, 65, 70, 55, 85],
    "ders3": [85, 100, 70, 80, 60, 95],
    "sehir": ["İstanbul", "Ankara", "İzmir", "İstanbul", "Bursa", "Ankara"],
    "yas": [22, 20, 24, 21, 23, 19]
})

# Üç dersin ortalamasını sütun olarak ekleme
df["ortalama"] = (df["ders1"] + df["ders2"] + df["ders3"]) / 3

# Ortalaması 70 üzeri 
basarili_ogrenciler = df[df["ortalama"] > 70]

# Sonucu yaşa göre küçükten büyüğe sıralama ve yazdırma
sonuc = basarili_ogrenciler.sort_values(by="yas")
print(sonuc)