from flask import Flask
from queue import Queue
import threading, time
import requests

Req_string = ''
queue1 = Queue() 
def questS():
    req = requests.get('http://www.yandex.ru')
    if (req.status_code==200):
        queue1.put(req.text)  
    else:
        queue1.put('ERROR PAGE')
    req.close()
    
app = Flask(__name__)
@app.route('/')
def hello():
    q_value = queue1.get()
    return q_value


if __name__ == "__main__":
    t_global = threading.Timer(50.0, questS)
    t_global.name = "Global Timer"
    t_global.start()
    app.run()
    
     