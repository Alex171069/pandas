from flask import Flask
import threading, time, timer
import requests
  
app = Flask(__name__)

def query_web():
    response = requests.get("http://www.yandex.ru")
    r = response.text              # .find('ядерная')
    inS = r.find("ядерный") 
   # print(r)
    print(inS)
web_qr = threading.Timer(100.0, query_web)
web_qr.start()

    
@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__': 
    app.run(debug=False)