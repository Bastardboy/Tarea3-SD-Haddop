from flask import Flask, request, render_template  
import json
import wikipedia as wiki

app = Flask(__name__)

p = ["Fútbol","Canino","Chile","Digimon","Wea","Tango","Node.js","Argentina", "Pokemon", "Turnip Boy Commits Tax Evasion"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET']) #Para definir el tipo de peticion y como hacerla
def search():
    f = open("database.json", "r")
    search = request.args['search']
    db = json.load(f)
    
    if(search not in db):
        return "no hay KK"
    macs = 0
    archivo = 0
    for i in db[search]:
        if(macs < db[search][i]):
            macs = db[search][i]
            archivo = i

    return wiki.page(p[int(archivo)-1],auto_suggest=False).url

if __name__ == '__main__':
    app.run(debug=True)