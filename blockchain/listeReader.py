import pickle
with open("maliste.txt","rb") as fichier:
    liste = pickle.load(fichier)

print(liste)