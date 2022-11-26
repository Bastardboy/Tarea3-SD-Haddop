import json

files = {}
a_file = open("output.txt","r")

next(a_file)
for line in a_file:
    l = line.strip()
    word, pos = l.split("\t",1)

    P = pos.split(" ")
    for i in P:
        a, c = (i.replace("(","").replace(")","")).split(",")
        files[word] = {a:c}


with open("../seeker/database.json", "w") as outfile:
    json.dump(files, outfile, indent = 4)