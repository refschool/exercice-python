poids = 78
taille = "1.82"



def calcul2(poids,taille):
    resultat = poids/(taille * taille)
    return resultat



def calcul1(poids,taille):
    try:
        resultat = poids/(taille * taille)
        return resultat
    except:
        print("il y a une erreur")


imc = calcul1(poids,taille)
print(imc)
