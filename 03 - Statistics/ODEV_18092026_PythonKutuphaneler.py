# 1. Hazırlık ve Ortam Ayarları
# Analiz için gerekli kütüphaneler (pandas, numpy, matplotlib, seaborn, scipy) nasıl içe aktarılır?
# Grafiklerin görsel stili (tema, renk paleti, boyut) nasıl standart hale getirilir?
# Sonuçların tekrarlanabilir olması için rastgelelik nasıl sabitlenir (random_state/seed)?
# Pandas'ta tüm sütun/satırların ve ondalık sayıların okunabilir biçimde görüntülenmesi nasıl sağlanır?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Grafik görsel stili ve boyut ayarları
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (10, 6)

# seed
np.random.seed(42)

# Pandas ayarları
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# 2. Örnek (Sentetik) Veri Setinin Oluşturulması
# 1000 müşteriden oluşan örnek bir veri seti (yaş, gelir, şehir, abonelik tipi, kayıt tarihi, 
## aylık harcama, memnuniyet puanı, churn) nasıl üretilir?
# Gerçek dünya verilerindeki tutarsızlıkları simüle etmek için şehir isimlerinde kasıtlı yazım 
## farklılıkları (İstanbul/istanbul, Ankara/ANKARA) nasıl eklenir?

n = 1000

yas = np.random.randint(18, 65, size=n)
gelir = np.random.normal(35000, 10000, size=n)
sehirler_ham = np.random.choice(["İstanbul", "Ankara", "İzmir", "Bursa", "istanbul", "ANKARA", " Izmir "], size=n)
abonelik = np.random.choice(["Temel", "Orta", "Full"], size=n)
kayit_tarihi = pd.date_range(start="2026-08-06", periods=n, freq="D")
aylik_harcama = np.random.normal(250, 80, size=n)
memnuniyet = np.random.randint(1, 10, size=n)
churn = np.random.choice([0, 1], size=n, p=[0.8, 0.2])

df = pd.DataFrame({
    'yas': yas,
    'gelir': gelir,
    'sehir': sehirler_ham,
    'abonelik_tipi': abonelik,
    'kayit_tarihi': kayit_tarihi,
    'aylik_harcama': aylik_harcama,
    'memnuniyet_puani': memnuniyet,
    'churn': churn
})

# Şehir düzeltme 
df['sehir'] = df['sehir'].str.strip().str.lower()

# 3. Kasıtlı "Kirli Veri" Enjeksiyonu
# Veri setine eksik değerler (gelir, yaş, memnuniyet puanı sütunlarında) nasıl eklenir?
# Gelir sütununda aşırı uç değerler (outlier) nasıl oluşturulur?
# Yaş sütununa mantıksız değerler (-5, 150 gibi) nasıl eklenir?
# Veri setine kasıtlı olarak yinelenen (duplicate) satırlar nasıl eklenir?

# Eksik değer (NaN) ekleme
df.loc[df.sample(frac=0.05).index, 'gelir'] = np.nan
df.loc[df.sample(frac=0.03).index, 'yas'] = np.nan
df.loc[df.sample(frac=0.04).index, 'memnuniyet_puani'] = np.nan

# Aşırı uç outlier ekleme
df.loc[0, 'gelir'] = 500000

# yaş sütunu mantıksız değerler ekleme
df.loc[1, 'yas'] = -5
df.loc[2, 'yas'] = 150

# Yinelenen (duplicate) satır ekleme
df = pd.concat([df, df.iloc[[10, 20, 30]]], ignore_index=True)


# 4. Veri Setine Genel Bakış
# Veri setinin kaç satır ve kaç sütundan oluştuğu nasıl kontrol edilir?
# Sütunların veri tipleri ve dolu/boş hücre sayıları (.info()) nasıl incelenir?
# Veri setinin ilk, son ve rastgele seçilmiş birkaç satırı nasıl görüntülenir?

# Satır ve sütun sayısı
print("Boyut (Satır, Sütun):", df.shape)

# Veri tipleri ve dolu/boş hücre bilgisi
print("Veri Bilgisi:")
df.info()

# İlk, son ve rastgele satırlar
print("İlk 3 Satır:\n", df.head(3))
print("Son 3 Satır:\n", df.tail(3))
print("Rastgele 3 Satır:\n", df.sample(3))


# 5. Eksik Değer Analizi
# Her sütundaki eksik değer sayısı, benzersiz değer sayısı ve eksik değer yüzdesini gösteren bir özet tablo nasıl oluşturulur?
# Eksik değerlerin veri setindeki dağılımı bir ısı haritası (heatmap) ile nasıl görselleştirilir?

# Özet tablo oluşturma
eksik_ozet = pd.DataFrame({
    'Eksik_Sayisi': df.isnull().sum(),
    'Eksik_Yuzdesi (%)': (df.isnull().sum() / len(df)) * 100,
    'Benzersiz_Deger_Sayisi': df.nunique()
})
print("Özet Tablo:\n", eksik_ozet)

# Eksik değer ısı haritası
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Eksik Değerlerin Isı Haritası")
plt.show()


# 6. Yinelenen Kayıtların Tespiti
# Veri setinde kaç adet birebir aynı (duplicate) satır bulunduğu nasıl tespit edilir?

duplicate_sayisi = df.duplicated().sum()
print("Ducplicate Sayisi: ", duplicate_sayisi)


# 7. Kategorik Veri Temizliği
# "Şehir" sütunundaki tutarsız yazımların (büyük/küçük harf, baştaki/sondaki boşluklar) dağılımı nasıl görüntülenir?
# Şehir isimleri küçük harfe çevrilip boşluklardan nasıl arındırılır?

print("Temizlik Öncesi Şehir Dağılımı:\n", df['sehir'].value_counts())

df['sehir'] = df['sehir'].str.strip().str.lower()


# 8. Mantık Dışı (Anomali) Değerlerin Tespiti
# 0'ın altında veya 100'ün üzerinde olan, gerçekçi olmayan yaş değerlerine sahip müşteriler nasıl bulunur?

anomaliler = df[(df['yas'] < 0) | (df['yas'] > 100)]
print("Mantık Dışı Yaş Değerine Sahip Müşteriler:\n", anomaliler[['yas', 'sehir', 'gelir']])


# 9. Betimsel İstatistikler
# Sayısal sütunların temel istatistiksel özeti (ortalama, medyan, std, min/max vb.) nasıl elde edilir?
# Sayısal değişkenlerin çarpıklık (skewness) ve basıklık (kurtosis) değerleri nasıl hesaplanır?

print("Temel İstatistiksel Özet:\n", df.describe().T)

# Skewness ve Kurtosis hesaplama
sayisal_sutunlar = df.select_dtypes(include=[np.number]).columns

skew_kurt = pd.DataFrame({
    'Skewness': df[sayisal_sutunlar].skew(),
    'Kurtosis': df[sayisal_sutunlar].kurt()
})
print("Çarpıklık ve Basıklık Değerleri:\n", skew_kurt)


# 10. Dağılım Görselleştirmeleri
# Sayısal değişkenlerin dağılımları histogram ve yoğunluk eğrisi (KDE) ile nasıl gösterilir?
# Sayısal değişkenlerdeki aykırı değerler kutu grafiği (boxplot) ile nasıl görselleştirilir?

# Histogram ve KDE
plt.figure(figsize=(12, 5))
sns.histplot(df['gelir'].dropna(), kde=True, bins=30)
plt.title("Gelir Dağılımı (Histogram + KDE)")
plt.show()

# Boxplot
plt.figure(figsize=(10, 4))
sns.boxplot(x=df['gelir'])
plt.title("Gelir Sütunundaki Aykırı Değerler (Boxplot)")
plt.show()


# 11. Kategorik Değişken Analizi
# Kategorik sütunların (şehir, abonelik tipi, memnuniyet puanı, churn) yüzdesel dağılımı nasıl hesaplanır?

kategorik_sutunlar = ['sehir', 'abonelik_tipi', 'memnuniyet_puani', 'churn']

for sutun in kategorik_sutunlar:
    print(f"\n--- {sutun} Yüzdesel Dağılımı ---")
    print(df[sutun].value_counts(normalize=True) * 100)


# 12. Korelasyon Analizi
# Sayısal değişkenler arasındaki korelasyon matrisi nasıl hesaplanır?
# Korelasyon matrisi bir ısı haritası ile nasıl görselleştirilir?

# Korelasyon matrisi
korelasyon = df[sayisal_sutunlar].corr()
print("\nKorelasyon Matrisi:\n", korelasyon)

# Isı haritası (Heatmap)
plt.figure(figsize=(8, 6))
sns.heatmap(korelasyon, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Sayısal Değişkenler Arasındaki Korelasyon Isı Haritası")
plt.show() 