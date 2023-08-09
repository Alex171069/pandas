from flask import Flask
import scheduler(timefunc=time.monotonic,)
  
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__': 
    app.run(debug=False)