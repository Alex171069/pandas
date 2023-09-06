from flask import Flask
  
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

<<<<<<< HEAD
@app.route('/<username>')
def show(username):
    return "Это "+ username

=======
>>>>>>> 489cc25b10b64be9b11b059bea28c60b7e53e98c

if __name__ == '__main__': 
    app.run(debug=True)