import requests
import socket
import ipaddress

class IP:
    
  def __init__ (self):
     
     self._tetra = dict()  # создаем ассоциативный словарь.    
     self._tetra[1] = 0
     self._tetra[2] = 0 
     self._tetra[3] = 0
     self._tetra[4] = 0 
     self._storeIP = 0 
     
   
  def getIP(self, ip_in):      # процедура получения инкремента адреса 
     if(ip_in >= 255):
         return 0        
     else:
        ip_in += 1
        return ip_in
   
  def StrIp(self, ip_inc):
     return (str(self._storeIP))
        
  def SumStrIp(self,strIPAtom):
       if   self._tetra[1] == 0:
            self._tetra[1] = strIPAtom
       elif self._tetra[2] == 0:
            self._tetra[2] = strIPAtom
       elif self._tetra[3] == 0:
            self._tetra[3] = strIPAtom
       elif self._tetra[4] == 0:
            self._tetra[4] = strIPAtom
       else:   
          return str(self._tetra[4])+'.'+str(self._tetra[3])+'.'+str(self._tetra[2])+'.'+str(self._tetra[1])  # если все четыре тетрады не равны 0 то выводим всю строку адреса
            
           
        
 
  def CreateIP4(Tetr_ip): # преобразование строки адреса в IP адрес
     if(len(Tetr_ip)>0):
         return ipaddress.IPv4Address(Tetr_ip)
     else:
         return 0 
OpenIp = IP()    
while OpenIp._storeIP < 255:
  storeIPRes = OpenIp.getIP(OpenIp._storeIP)
  print(OpenIp.SumStrIp(storeIPRes))
  #print(CreateIP4(StrIp(storeIP)))
   

#Ghost = socket.gethostbyaddr('127.0.0.1')
#a = list(Ghost)   # list
#print(a[1])

#DomenHostN = socket.getfqdn('127.0.0.1')
#print(DomenHostN)

#Hget = requests.get('https://ya.ru')
#if Hget.status_code == 200:
#    print('Получилось!')
   # print(Hget.content)
#elif Hget.status_code == 404:
#    print('Невышло.')

