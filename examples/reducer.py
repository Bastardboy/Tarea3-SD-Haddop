#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys
import json

current_word = None
current_count = 0
word = None

count_file = 0
files = {}
# palabra = {1:89}
for line in sys.stdin:
    l = line.strip()

    word, num = l.split("\t",1)
    if("xdxdxd" in l):
        count_file += 1
    else:
        if(word in files):
            if(count_file in files[word]):
                files[word][count_file] += 1
            else:
                files[word][count_file] = 1
        else:
            files[word] = {count_file:1}


f = open("output.txt", "w")
f.write("Palabra\t(Archivo, Cantidad)\n")
for word in files:
    f.write(word+"\t")
    print(word+"\t")
    for file in files[word]:
        f.write("("+str(file)+","+str(files[word][file])+")"+" ") #output
        print(str(file)+"\t"+str(files[word][file])+" ") #consola
    f.write("\n")
f.close()

with open("../seeker/database.json", "w") as outfile:
    json.dump(files, outfile, indent = 4)


#word | (file1, count1), (file2, count2), (file3, count3)
#hola | (1, 2), (2, 1), (3, 1)