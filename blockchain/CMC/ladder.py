import pprint
import pickle
from os import listdir
import os
from tabulate import tabulate
""" read folder """
files = listdir("dump")
files = list(map(lambda x:"dump/" + x,files))
files.sort(key=lambda x:os.path.getmtime(x),reverse=True)

first_file = files[0]
second_file = files[1]

with open(first_file,'rb') as fichier:
    cmc0 = pickle.load(fichier)
with open(second_file,'rb') as fichier:
    cmc1 = pickle.load(fichier)

""" compute OLD position """
for i in range(len(cmc0)):
    cmc0[i].append(i+1)


for i in range(len(cmc1)):
    """ wanted est le crypto recherché """
    wanted = cmc1[i][0]
    """ sert à calculer la variation de position il est setté à zéro par défaut """
    cmc1[i].append(0)
    for j in range(len(cmc0)):
        if(cmc0[j][0] == wanted):
            cmc1[i][4] = j+1
            break
""" compute new position """
for i in range(len(cmc1)):
    cmc1[i].append(i+1)



""" compute progression """

for i in range(len(cmc1)):
    if(cmc1[i][4] != 0):
        cmc1[i].append(cmc1[i][4] - cmc1[i][5])
    else:
        cmc1[i].append('-')
        print("***NEW***",cmc1[i][0])
print(tabulate(cmc1,headers=['Crypto','Price','Variation H1','Variation H24','','','Order','Prev Order']))
#pprint.pprint(cmc1)