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
    
    #urls_cont = 0
    urls = {}
    
    
    while(len(db[search])>0): #hasta que se vacia busca
        macs = 0
        archivo = 0
        for j in db[search]: #busca el archivo con mas coincidencias
            if(macs < int(db[search][j])): #si hay mas coincidencias
                macs = db[search][j] #actualiza el maximo, tonces aqui el max seria que valor? el de repeticiones de la palabra
                archivo = j #actualiza el archivo (aqui el archivo que era? el indice con mas weas del diccionario)
                #ah ya archivo key macs value?
        db[search].pop(archivo) #elimina el indice esto? elimina el objeto con ese indice se supone
        urls[archivo] = wiki.page(p[int(archivo)],auto_suggest=False).url   
    return  urls


if __name__ == '__main__':
    app.run(debug=True)