from  collections import Counter
from collections import Counter   # belli bir modüle ün içinden sadece ihtiyacın olan kısmı importlamak için bu kodu kullanabilrsin.
import random
liste1=random.sample(range(10),k=3)
liste2=random.sample(range(10),k=3)
liste3=random.sample(range(10),k=3)
tüm_listeler= liste1 + liste2 + liste3
listelerin_listesi= liste1,liste2,liste3
for index,liste in enumerate(listelerin_listesi):
    print('{}. liste \t {} '.format(index+1,liste))
print(tüm_listeler)
print(Counter(tüm_listeler))
print(Counter(tüm_listeler).most_common(1))

