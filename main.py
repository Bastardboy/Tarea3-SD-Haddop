import wikipedia as wiki

p = ["Fútbol","Canino","Chile","Digimon","Wea","Tango","Node.js","Argentina", "Pokemon", "Turnip Boy Commits Tax Evasion"]

for i in p:
    a = wiki.page(i,auto_suggest=False)
    carpeta = "1" if p.index(i) < 5 else "2"
    with open("./"+carpeta+"/wiki"+str(i)+".txt", "w") as f:
        f.write(a.content)
        f.close()
    print("Escribio el archivo: "+i)

# For que waayaahtanwa waayaahtanonki < > 

#https://github.com/Naikelin/map-reduce-hadoop