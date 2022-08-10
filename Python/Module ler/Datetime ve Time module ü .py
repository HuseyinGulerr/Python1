import datetime
from datetime import date
from datetime import time

bugün=date.today()
yarın=date(2022,8,3)
print(bugün.month)
print(yarın.year)
print(yarın-bugün)
geçen_zaman=yarın-bugün
print(geçen_zaman.days)

print(date.isocalendar(yarın))           # isocalendar  haftalık bilgiyi yazdırır
print(date.weekday(yarın))
print(date.ctime(bugün))     # ctime , tarihi daha okunaklı yazar 


saat=time(17,35)
print(saat)
saat=time(17,35,47)
print(saat)
print(saat.minute)

zaman_ve_tarih_birleştir=datetime.datetime(2022,8,2,00,40,35)
print(zaman_ve_tarih_birleştir)

import time          # from datetime import time dan farkı direkt gerçek tarihi kodla yazdırabiliyorsun manuel olmayarak ve .sleep gibi özel komutlar var 

başlangıç_zamanı=time.time()
print(time.time())
time.sleep(3)
bitiş_zamanı=time.time()
print(time.time())
print('Geçen süre :\t{} sn'.format(round(bitiş_zamanı-başlangıç_zamanı)))
