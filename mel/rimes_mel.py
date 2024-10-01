from collections import ChainMap

with open("lyrics.txt","r",encoding="utf-8") as file:
    pass

i = {"i","î","y","outil","ean","ee"}
y = {"hu", "u", "ût"}
u = {"ou", "oun", "ouls", "oo"}
e = {"é","er","ez","ey","ai","è"}
ø = {"eu", "eux", "heu","oeu"}
o = {"au", "ô", "eau", "o"}
a = {"à", "a", }
ɛ = { "oint "," in","aint","ein","im","ien" }
œ̃un = {"un", "um"}
ɔ = {"on", "om", "ont"}
ɑ̃an = {"en", "am", "ang","em"}

def analyse_rime ():
    pass

"""
1-parcourir le texte ligne par ligne
2-obtenir le dernier mot de chaque ligne
3-prendre la dernière syllabe du mot
4-matcher la syllabe avec le dico
5-générer nouveau fichier texte avec les phonèmes
"""