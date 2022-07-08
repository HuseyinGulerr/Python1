sayilar=[23,44,6,78,65,79]
def karelerini_alma(x):
 return x**2  
print (*map(karelerini_alma,sayilar)) #map komutu listedeki her elemana foknksiyonu uygulatmayı sağlar.


def tek_mi_çift_mi(x):
 if x%2==0:
  return x
 else:
   return None       
print(*filter(tek_mi_çift_mi,sayilar)) #filter komutu listedeki elemanlara o fonskiyonun kuralını uygulatır. kısacası filtreler


print(*map(lambda x: x+5,sayilar))  # lambda map ve filter ile birlikte kullanılabilir satırın içinde fonksiyonu oluşturmaya yarar.

