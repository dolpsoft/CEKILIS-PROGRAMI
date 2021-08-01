import random
import time
ceklisListesi=[]
print("ÇEKİLİŞ YAP !")
print("-"*50)
print("Çekiliş yapma programına hoş geldiniz. Bu programda bir çekiliş listesi oluşturabilirsiniz, ve biz o çekiliş listesinden rastgele bir isimi seçip size bildireceğiz.")
print("-"*50)
while True:
    seceneks= int(input("Seçenekler\n1-Çekiliş Listesi Oluştur\n2-Çekiliş Listesini Görüntüle\n3-Çekiliş Listesini Sıfırla\n4-Programdan Çık\n\nSeçiminiz: "))
    while seceneks<1 or seceneks>4:
        print("-"*50)
        print("Lütfen seçiminizi 1 ile 4 arasında (1 ve 4 dahil) giriniz. Tekrar deneyin.")
        print("-"*50)
        seceneks= int(input("Seçenekler\n1-Çekiliş Listesi Oluştur\n2-Çekiliş Listesini Görüntüle\n3-Çekiliş Listesini Sıfırla\n4-Programdan Çık\n\nSeçiminiz: "))
    if seceneks== 1:
       while True: 
           print("-"*50)
           adGir=input("Çekiliş listesi oluşturmak için, çekiliş listesinde olmasını istediğiniz adları giriniz. Bir ad ekledikten sonra başka adlar da ekleyebilirsiniz. (Eğer bir çekiliş listesi oluşturup 1. seçeneği seçerseniz, oluşturulan listenin üzerine ekleme yapılır) Bu bölümden çıkmak için 1 yazabilirsiniz: ")
           if adGir =="1":
               print("-"*50)
               print("Menüye döndünüz.")
               print("-"*50)
               break
           ceklisListesi.append(adGir)
           print("-"*50)
           print( " '{}' , çekiliş listesine eklendi.". format (adGir))
           
    elif seceneks== 2 and len(ceklisListesi)==0:
        print("-"*50)
        print ("Herhangi bir çekiliş listesi oluşturmadınız veya listeyi sıfırladınız. Bir çekiliş listesi oluşturduktan sonra listenizi görüntüleyebilirsiniz.")
        print("-"*50)
    elif seceneks== 2 and len(ceklisListesi)!=0:
        print( "Çekiliş listeniz aşağıdaki gibidir: ")
        print("-"*50)
        sayac= 1
        for i in ceklisListesi:
              print(sayac,")", i)
              sayac+=1
        print("-"*50)
        print("Çekiliş listesi üzerinde aşağıdaki işlemleri yapabilirsiniz: ")
        while True: 
          seceneks2= int(input("1-Çekiliş Listesinden Birini Çıkar\n2-Çekiliş Listesine Birini Ekle\n3-Çekilişi Yap!\n4-Menüye Dön\n\nSeçiminiz: "))
          while seceneks2<1 or seceneks2>4:
                  print("-"*50)
                  print("Lütfen seçiminizi 1 ile 4 arasında (1 ve 4 dahil) giriniz. Tekrar deneyin.")
                  print("-"*50)
                  seceneks2= int(input("1-Çekiliş Listesinden Birini Çıkar\n2-Çekiliş Listesine Birini Ekle\n3-Çekilişi Yap!\n4-Menüye Dön\n\nSeçiminiz: "))
               
          if seceneks2== 1 and len(ceklisListesi)== 0:
               print("Çekiliş listenizden tüm kişileri çıkardığınız için herhangi başka bir kişi çıkarmazsınız.")
          elif seceneks2== 1:
               print("-"*50)
               sayac= 1
               for i in ceklisListesi:
                    print(sayac,")", i)
                    sayac+=1
               print("-"*50)
               kisiCikar=int(input ("Çekiliş listesinden çıkarmak istediğiniz kişinin numarasını yazınız: "))
               print("-"*50)
               cikti=ceklisListesi.pop(kisiCikar-1)
               print("-"*50)
               print (" '{}' çekiliş listesinden kaldırıldı.".format(cikti))
               print("-"*50)
               print("Değişiklikler sonucunda oluşan çekiliş listeniz: ")
               print("-"*50)
               sayac= 1
               for i in ceklisListesi:
                 print(sayac,")", i)
                 sayac+=1
               print("-"*50)
               print("Aşağıdan başka işlemler yapabilirsiniz.")
               print("-"*50)
        
         
          elif seceneks2== 2:               
               print("-"*50)
               sayac= 1
               for i in ceklisListesi:
                   print(sayac,")", i)
               sayac+=1
               print("-"*50)
               kisiEkle=input ("Çekiliş listesine eklemek istediğiniz kişinin adını yazınız: ")
               ceklisListesi.append(kisiEkle)
               print("-"*50)
               print (" '{}' çekiliş listesine eklendi.".format(kisiEkle))
               print("-"*50)
               print("Değişiklikler sonucunda oluşan çekiliş listeniz: ")
               print("-"*50)
               sayac= 1
               
               for i in ceklisListesi:
                 print(sayac,")", i)
                 sayac+=1
               print("-"*50)
               print("Aşağıdan başka işlemler yapabilirsiniz.")
               print("-"*50)
         
          elif seceneks2== 3 and len(ceklisListesi)== 0:
               print("-"*50)
               print("Çekiliş listenizde herhangi bir isim bulunmadığından, çekiliş yapılamıyor. Lütfen öncelikle listeye birkaç kişi ekleyin.")
               print("-"*50)
          elif seceneks2== 3:                
               kazanan= random.choice(ceklisListesi)
               cekilisBaslat=input ("Çekilişi başlatmak için herhangi bir şey yazın: ")
               print("Çekiliş yapılıyor...")
               time.sleep(1)
               print("•")
               time.sleep(1)
               print("•")
               time.sleep(1)
               print("•")
               print("Çekiliş tamamlandı. Kazanan: ' {} ' çekilişi kazandı !!!".format(kazanan))
               while True:
                       sec= input ("Kazanan kişi listeden kaldırılsın mı? Evet ise 'E' hayır ise 'H' yazınız: ")
                       if sec== "E":
                          ceklisListesi.remove(kazanan)
                          print("-"*50)
                          print ("Çekilişi kazanan '", kazanan, "' çekiliş listesinden kaldırılmıştır.")
                          sayac= 1
                          print("-"*50)
                          print("Değişiklikler Sonucunda Oluşan Çekiliş Listeniz: ")
                          for i in ceklisListesi:
                                print(sayac,")", i)
                                sayac+=1
                          print("-"*50)
                          print("")
                          print("Aşağıdan çekiliş listesi ile ilgili başka işlemler seçebilirsiniz.")
                          print("-"*50)
                          break
                       else:
                           print("-"*50)
                           print(" Çekilişi kazanan kişi listeden kaldırılmadı.")
                           print("Çekiliş Listeniz: ")
                           sayac= 1
                           print("-"*50)
                           for i in ceklisListesi:
                                print(sayac,")", i)
                                sayac+=1
                           print("-"*50)
                           print("Aşağıdan çekiliş listesi ile ilgili başka işlemler seçebilirsiniz.")
                           print("-"*50)
                           break
                           
          else:
              print("-"*50)
              print ("Menüye Döndünüz.")
              print("-"*50)
              break                  
           
    elif seceneks == 3 and len(ceklisListesi) == 0:
         print("-"*50)        
         print("Çekiliş listeniz de herhangi bir isim bulunmadığından listeniz sıfırlanamaz. Aşağıdan başka işlemler seçebilirsiniz.")
         print("-"*50)
    elif seceneks == 3 and len(ceklisListesi)!= 0:       
              print ("Çekiliş Listeniz:")
              sayac= 1
              print("-"*50)
              for i in ceklisListesi:
                    print(sayac,")", i)
                    sayac+=1
              print("-"*50)
              karar= int(input("Çekiliş listenizi sıfırlamak istediğinize emin misiniz? Tüm adlar listeden silinecektir. Onaylamak için 1 iptal edip menüye dönmek için 0 yazınız:"))
              if karar== 1:
                  ceklisListesi.clear()
                  print("-"*50)
                  print("Çekiliş listeniz sıfırlandı. Aşağıdan başka seçenekler seçebilirsiniz.")
                  print("-"*50)
                  
              else:
                  print("-"*50)
                  print("İşlem iptal edildi. Menüye döndünüz.")
                  print("-"*50)
                 
    else:
              print("-"*50)
              print("Programı kapattınız. Sonraki çekilişlerde de bizi seçmeniz dileğiyle ! ")
              print("-"*50)
              exit ()
              
              
              
              