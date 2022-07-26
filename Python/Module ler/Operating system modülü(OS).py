##klasörler için olan kısım.                                                                     # os modüle u dosya ve klasör için kullanılır. 
import os                    ##os bilinen bir modül (operating system)
print (os.listdir())         # şuan bulunduğun yerdeki klasörleri yazdırır
print(os.getcwd())           #klasörün path ini verir
print(os.mkdir('deneme'))    # yeni klasör ekler
print (os.listdir())         
print (os.listdir('Class yapıları'))
print (os.rmdir('deneme'))   #içi boş klasörü siler
print (os.listdir())



##dosyalar için olan kısım.             #os.O_RDONLY>> Sadece oku  os.O_WRONLY>>> Sadece yaz  os.O_RDWR>>>> Oku ve yaz  os.O_CREAT>>> Yeni dosya oluştur
yeni_dosya='yeni_dosya.txt'
os.unlink(yeni_dosya.encode())



