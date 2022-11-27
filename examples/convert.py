import json

files = {}
a_file = open("outhadoop/part-00000","r")

next(a_file)
for line in a_file:
    l = line.strip()
    word, pos = l.split("\t",1)

    P = pos.split(" ")
    for i in P:
        a, c = (i.replace("(","").replace(")","")).split(",")
        if(word in files):
            files[word][a] = int(c)
        else:
            files[word] = {a:int(c)}

with open("../seeker/database.json", "w") as outfile:
    json.dump(files, outfile, indent = 4)