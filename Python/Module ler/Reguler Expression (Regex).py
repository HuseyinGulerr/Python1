import re                                     #regex modülü metinler içinde arama yapmak için kullanılır.
cümle= 'Bugün günlerden salı ve tarih 26.7.2022'   #\d rakamları arar, \w karakterleri arar herşey bir karakterdir, \s boşlukları arar.   Bunların büyük harfli versiyonları da değilleridir.  
patern=r'\d{1,2}.\d{1,2}.\d{4}'                         # \D rakam olmayanları arar gibi.              
print(re.search(patern,cümle))
for x in re.findall(patern,cümle):
 print(x)
