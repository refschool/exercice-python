import os
#listdir liste les fichier d'un répertoire
#join contraire de split

from os import listdir            #utlisé pour lister tout dans un répertoire et fichiers
from os.path import isfile, join  #utilisé pour lister des fichiers
mypath = ".\\batch2\\"
print(listdir(mypath)) # affiche tous les sous-repertoires de batch2

for f in listdir(mypath):
    print(listdir(join(mypath,f))) # afficher tous les fichiers.svg des sous-répertoires
    list_SVG=join(mypath,f)
search_text="--uatb2b--c.visual"
replace_text=".lightning."



for filename in os.listdir(list_SVG):  #retourne une liste contenue dans un répertoire
    with open(os.path.join(list_SVG, filename),'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)
    with open(os.path.join(list_SVG, filename),'w') as file:
        file.write(data)

print(list_SVG)
print("Text replaced")







