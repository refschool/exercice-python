liste = [1,2,3,4]
liste_carre= []
def carre(liste):
    for i in liste:
        carre = i * i
        liste_carre.append(carre)
    return liste_carre

resultat = carre(liste)
print(resultat)

""" [1,4,9,16] """