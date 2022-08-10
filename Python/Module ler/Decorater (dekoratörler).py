import time           # @dekoratörün adını yazarak kullanıcaksın.   dekoratörler fonksiyonlara uygulanan üst fonksiyon gibi. burda yaptığım dekoratör fonksiyonların çalışma sürelerini hesaplıyor
                                                                             
def fonkisyon_süresi_hesaplama(g):
    def wrapper(*args):
        başlangıç=time.time()
        print('Başlama zamanı:\t {}'.format(başlangıç))
        g(*args)
        bitiş=time.time()
        print('Bitiş zamanı:\t {}'.format(bitiş))
        print('Fonksiyonun çalışma süresi:\t {}'.format(bitiş-başlangıç))
    return wrapper

@fonkisyon_süresi_hesaplama    #dekoratör böyle yazılıyo.
def faktöriyel_hesaplama(x):
    toplam=1
    while x>1:
     toplam=toplam*x
     x=x-1
    return(toplam)

faktöriyel_hesaplama(10)