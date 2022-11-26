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
        return "no se encontró esta palabra"
    
    #urls_cont = 0
    urls = {}
    
    
    while(len(db[search])>0): 
        macs = 0
        archivo = 0
        for j in db[search]: 
            if(macs < int(db[search][j])): 
                macs = db[search][j]
                archivo = j 
        db[search].pop(archivo)
        urls[archivo] = wiki.page(p[int(archivo)],auto_suggest=False).url   
    return  urls


if __name__ == '__main__':
    app.run(debug=True)