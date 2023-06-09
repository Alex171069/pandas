import socket

class NetList:
   def getHost(self):
         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет клиента
         port = 8080  # устанавливаем порт сервера
         client.connect((socket.getfqdn('10.113.5.153'), port))  # подключаемся к серверу
         hostname = socket.gethostname()  # получаем хост сервера
         data = client.recv(1024)  # получаем данные с сервера
         print ("Имя сервера ", hostname)  # выводим  имя сервера
         print("Server sent: ", data.decode())  # выводим данные на консоль
         client.close()
def main():
    netL = NetList()
    netL.getHost()

main()
