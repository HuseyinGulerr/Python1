from operator import concat
from re import X
from webbrowser import get


def büyük_sayıyı_döndür(a,b):   #def=define(tanıtmak)
 if a>b:
  return(a)                     # Fonksiyonlarda print yerine return kullanılır. Print yazarsan none output unu alırsın.
 elif b>a: 
  return(b)
print (büyük_sayıyı_döndür(7,9))

def cümle_yazdırma(a,b):
 büyük_sayı=büyük_sayıyı_döndür(a,b)
 cümle=('{} daha büyük sayıdır'.format(büyük_sayı))
 return(cümle)
print()

#args komutu ile fonksiyonlarda 2 den fazla eleman koyabilirsin kullanırken başına '*' getirerek.  kwargs(keyword) komutu ile de dictionary şeklinde yazdırabilirsin isim=Hüseyin gibi
def ailedeki_isimler(*args):
 çocuk='Hüseyin'
 abla='Fevriye'
 anne='Esma'
 baba='Sebahattin'
 return(çocuk,abla,anne,baba)
print (ailedeki_isimler())

input(c=(int('Bir sayı yazınız.'))
if c<100
  print(c)
else:
 print('{} x den büyüktür.'.format(c))




def rakamları_yazdır(number):
 for rakam in number:
  if rakamm<=9:
   get(rakam)
  else:
   continue
 return(rakam)     
print(rakamları_yazdır(5)) 