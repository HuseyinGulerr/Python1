from calendar import c


x=input(('Bir sayı giriniz '))
if int(x)%2==0:
    print('{} sayısı bir çift sayıdır.'.format(x))
else: 
     print('{} sayısı tek sayıdır'.format(x))    


def sayı_oluncaya_kadar_döngü():
 a=input('Bir sayı giriniz: ')
 while not a.isdigit():  #.isdigit komutu bu bir sayı mı sorusunu sorar.
    print('Sorry! This is not integer type input.')
    a=input('Bir sayı giriniz: ')
 else:
    print('Congrats! You have been typed an integer type input.')
print (sayı_oluncaya_kadar_döngü())  


def parolayı_doğru_girene_kadar_döngü():
 b=input('Type a valid password: ')
 while not (('_'in b) and ('123456789'in b)):
  print('Its not correct, try again!')
  b=input('Type a valid password: ')
 else:
  print('You have been typed a valid password!')      
print(parolayı_doğru_girene_kadar_döngü())