#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys
import re
fi = 0
for line in sys.stdin:
    l = line.lower()
    if("xdxdxd" in l):
        fi = int(l[0])
    else:
        for char in [",", ".", '"', "'", "(", ")", "\\", ";", ":", "$1", "$", "&"]:
            l = l.replace(char, '')
            
        word = l.split()

        for words in enumerate(word):
            print('{}\t{}'.format(words[1], fi))