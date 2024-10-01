"""   2-obtenir le dernier mot de la ligne  """
ligne = "La Cigale, ayant chantés ou"
listerime = []

dico = {
    "E" : ["é","er","ez","ey","ai","è","és"],
    "U" : ["ou", "oun", "ouls", "oo"]
        }
def has_son(e,son):
    if(son in e):
        return True
    else:
        return False

""" parcourir à l'envers pour extraire le minimum de lettre qui fait un son"""

for key,value in dico.items():
    son = ""
    for i in range(len(ligne)-1,0,-1):
        son = ligne[i]+son
        resultat = has_son(value,son)
        print(value,resultat,"son=",son,":")
        if resultat == True:
            print("dans true")
            listerime.append(key)
            break

print(listerime)