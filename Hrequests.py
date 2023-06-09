import requests
import socket
import ipaddress

storeIP = 0 
strIP = ""
def getIP(ip_in):      # процедура получения инкремента адреса 
    if(ip_in >= 255):
        return 0        
    else:
        ip_in += 1
        return ip_in
   
def StrIp(ip_inc):
      strIP = str(storeIP)+'.'+str(ip_inc)
        
 
def CreateIP4(Tetr_ip): # преобразование строки адреса в IP адрес
     if(len(Tetr_ip)>0):
         return ipaddress.IPv4Address(Tetr_ip)
     else:
         return 0 
       
while storeIP < 255:
  storeIP = getIP(storeIP)
 
  StrIp(storeIP)

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

