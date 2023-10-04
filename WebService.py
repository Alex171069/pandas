from flask import Flask, render_template
  
app = Flask(__name__, template_folder='template')

def doc():
    return 'DOC'


@app.route('/')
def index():
    return render_template('test.html')

@app.route('/<username>')
def show(username):
    return "Это "+ username

@app.route('/second/<int:id>')
def second(id):
    return "second"+" "+str(id)

app.add_url_rule('/doc/',view_func=doc)

def test():
    return "привет"

@app.route('/db/<string:search>')
def db_search(search):
    return search

def db_conection():
    return 1 


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=4567, debug=True)