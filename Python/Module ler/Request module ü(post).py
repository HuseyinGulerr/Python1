from io import BytesIO
from PIL import Image
from urllib import response
import requests
# pasta dilimi grafiği
site_URL= 'https://image-charts.com/chart'
payload={                                                               #https://image-charts.com/chart
 'cht':'p3',
 'chs':'999x999',
 'chd':'t:49,51',
 'chl':'Ronaldo|Messi',
 'chan': None,
 'chf':'ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1'
}
response=requests.post(site_URL, data=payload)             #params parametres ın kısaltılmış hali        post komutunda servera data yolluyosun server o dataları kullanıp sana geri dönüyo.       get komutunda ise direkt serverdan data alıyosun
print(response.content)
print(type(response.content))
image=Image.open(BytesIO(response.content))
image.show()

#dota versiyon grafik (radar grafiği)
site_URL= 'https://image-charts.com/chart'
payload={
   'chco': '3092de',
   'chd':  't:81,65,50,67,59,81',
   'chdl': 'Falcao',
   'chdlp': 'b',
   'chl': 'Hız|Şut|Defans|Dribbling|Fizik|Pas',
   'chs': '999x999',
   'cht': 'r',
   'chtt': 'Futbolcu özellikleri'
}
response=requests.post(site_URL, data=payload)
image=Image.open(BytesIO(response.content))
image.show()

# asıl karşılaştırma yapılan kısım
class Futbolcu():
    def __init__(self, isim, hız, şut, defans, dribbling, fizik, pas):
        self.isim = isim
        self.hız = hız
        self.şut = şut
        self.defans = defans
        self.dribbling = dribbling
        self.fizik = fizik
        self.pas = pas
    
    def yetenekleri_görselleştirme(self):
        site_URL= 'https://image-charts.com/chart'
        payload={
           'chco': '3092de',
           'chd':  't:' + self.yetenekleri_hazırla(),
           'chdl': self.isim,
           'chdlp': 'b',
           'chl': 'Hız|Şut|Defans|Dribbling|Fizik|Pas',
           'chs': '999x999',
           'cht': 'r',
           'chtt': 'Futbolcu özellikleri',
           'chxl': '0:|0|20|40|60|80|100',
           'chxt': 'x',
           'chxr': '0,0.0,100.0',
           'chm': 'B,AAAAAABB,0,0,0'
           }
        response=requests.post(site_URL, data=payload)
        image=Image.open(BytesIO(response.content))
        image.show()   
    def yetenekleri_hazırla(self):
        return ','.join([
            str(self.hız),
            str(self.şut),
            str(self.defans),
            str(self.dribbling),
            str(self.fizik),
            str(self.pas),
            str(self.hız)
        ])    
    def yetenekleri_karşılaştır(self, diğer_futbolcu):
        site_URL= 'https://image-charts.com/chart'
        payload={
           'chco': '3092de,027182',
           'chd':  't:'+ self.yetenekleri_hazırla() + '|' + diğer_futbolcu.yetenekleri_hazırla(),
           'chdl': self.isim + '|' + diğer_futbolcu.isim,
           'chdlp': 'b',
           'chl': 'Hız|Şut|Defans|Dribbling|Fizik|Pas',
           'chs': '999x999',
           'cht': 'r',
           'chtt': 'Futbolcu özellikleri',
           'chxl': '0:|0|20|40|60|80|100',
           'chxt': 'x',
           'chxr': '0,0.0,100.0',
           'chm': 'B,AAAAAABB,0,0,0|B,0073CFBB,1,0,0'
        }
        response=requests.post(site_URL, data=payload)
        image=Image.open(BytesIO(response.content))
        image.show()  
mertens=Futbolcu('Mertens',84,89,34,85,69,82)
valencia=Futbolcu('Valencia',75,83,32,79,81,72)
messi=Futbolcu('Messi',89,94,45,96,72,93)
ronaldo=Futbolcu('Ronaldo',87,94,35,86,81,73)
print(messi.yetenekleri_karşılaştır(ronaldo))