from flask import Flask
  
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/<username>')
def show(username):
    return "Это "+ username


if __name__ == '__main__': 
    app.run(debug=True)