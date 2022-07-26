class Oyun():
 oyunun_platformu='Steam'
oyun1=Oyun()                                      #Class yapısı  
print (oyun1.oyunun_platformu)


class Oyun():
 oyunun_platformu='Steam'
 def __init__(self, tür, fiyat, sistem_gereksinimleri, beğenisi):     #object'li Class yapısı  object class'ın alt sınıfı gibi özellik atayabiliyorsun. (self kendinden olan özel komut çoğu zaman yaz)
    self.tür=tür
    self.fiyat=fiyat
    self.sistem_gereksinimleri=sistem_gereksinimleri
    self.beğenisi=beğenisi
oyun2=Oyun('Eglence', 55, 'Yüksek', 'Güzel')
print(oyun2.tür)      


class Oyun():
 oyunun_platformu='Steam'
 def __init__(self, tür, fiyat, sistem_gereksinimleri, beğenisi):    
   self.tür=tür
   self.fiyat=fiyat
   self.sistem_gereksinimleri=sistem_gereksinimleri
   self.beğenisi=beğenisi
 def oyuna_ait_cümle_yazdır(self):                                      # Class ve object'e method eklenmiş şekli.
  return('{} türünde {} tl fiyatlı {} sistem isteyen {} bir oyun.').format(self.tür,self.fiyat,self.sistem_gereksinimleri,self.beğenisi)
oyun3=Oyun('Co-op',43,'Düşük','Fena olmayan' )
print (oyun3.oyuna_ait_cümle_yazdır())



class Oyun():
 oyunun_platformu='Steam'
 def __init__(self, tür, fiyat, sistem_gereksinimleri, beğenisi):    
   self.tür = tür
   self.fiyat=fiyat
   self.sistem_gereksinimleri=sistem_gereksinimleri
   self.beğenisi = beğenisi
 def oyuna_ait_cümle_yazdır(self):                                      
  return('{} türünde {} tl fiyatlı {} sistem isteyen {} bir oyun.').format(self.tür,self.fiyat,self.sistem_gereksinimleri,self.beğenisi)
 def oyunun_güncel_fiyatı(self):
   return self.fiyat
 def oyunun_indirimli_fiyatı(self, indirim_miktarı=1):
   if indirim_miktarı < self.fiyat:
    self.fiyat -= indirim_miktarı
    return self.fiyat                                                    # Methodlarla birlikte değişebilir dinamik Class yapısı.               
   else:
    return('Oyununuz bedava olmuştur.')  
oyun3=Oyun('Co-op',43,'Düşük','Fena olmayan' )
print (oyun3.oyunun_indirimli_fiyatı(17))

class FallGuys(Oyun):
 def __init__(self, takım_sayısı, tür, fiyat, sistem_gereksinimleri, beğenisi):
   Oyun.__init__(self, tür, fiyat, sistem_gereksinimleri, beğenisi)
   self.takım_sayısı=takım_sayısı
fallguys=FallGuys(4,'Eğlence',59,'Orta','Yüksek')                                      # Alt üst class yapısı Oyun üst class(super class), Fallguys alt class(sub class). Alt class'ın kendine ait 
print (fallguys.takım_sayısı)                                                          # özellikleri vardır. Özelliklerine ek olarak üst class ın özelliklerini de döndürebilir. 
print (fallguys.tür)
print(fallguys.oyunun_indirimli_fiyatı(54))    
     




