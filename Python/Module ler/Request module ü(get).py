from sqlite3 import paramstyle
import requests

bölge_url = 'https://data.police.uk/api/forces'
response = requests.get(bölge_url)
print(response.status_code)     #200 status code u başarılı olduğu anlamına geliyor.
print(response.url)
print(response.text)
print(response.json())


kategoriler_url = 'https://data.police.uk/api/crime-categories'
payload = {'date':'2022-05'}
response=requests.get(kategoriler_url, params=payload)
print(response.json())


suç_url='https://data.police.uk/api/crimes-no-location'                          # https://data.police.uk/api/crimes-no-location?category=all-crime&force=leicestershire&date=2017-03 soru işaretinden sonraki kısımlar parametreler
payload={
    'category' :'all-crime',
    'force' : 'city-of-london',
    'date' : '2022-06'}
response=requests.get(suç_url,params=payload)
print(response.json())

from collections import Counter
# örnek uygulama
class Suç_Raporu():
    def __init__(self, bölge, tarih, kategori='all-crime'):
        self.bölge= bölge
        self.tarih= tarih
        self.kategori= kategori
        self.suçlar=self.suçları_bul()
    def suçları_bul(self):
        suçlar_url='https://data.police.uk/api/crimes-no-location'
        payload={
            'category': self.kategori,
            'force': self.bölge,
            'date': self.tarih}
        response=requests.get(suçlar_url, params=payload)
        
        if response.status_code==200:
            return response.json()
        else:
            return None
    def suçları_Raporla(self):
     suçlar_listesi= []
     
     if self.suçlar is not None:
         for suç in self.suçlar:
          suçlar_listesi.append(suç['category'])
         return Counter(suçlar_listesi)    

bakılmak_istenen_yer=Suç_Raporu('city-of-london','2022-07')
print(bakılmak_istenen_yer.suçları_Raporla())
