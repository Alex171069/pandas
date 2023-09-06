from flask import Flask
  
app = Flask(__name__)

def doc():
    return "DOC"

@app.route('/')
def index():
    return "Главная!"

@app.route('/<username>')
def show(username):
    return "Это "+ username

@app.route('/second/<int:id>')
def second(id):
    return "second"+" "+str(id)

app.add_url_rule('/doc/',view_func=doc)

def test():
    return "привет"


if __name__ == '__main__': 
    app.run(debug=True)