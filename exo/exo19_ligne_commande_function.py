comptage,totalHT = 0,0    # définition de variable
ligne = [(0.99,2),(5.65,4),(1.99,2),(3.99,12),(3.99,12)]  # création liste des commandes et tva


def sous_total_ligne(item):  # fonction de calcul
    return item[0] * item[1]


def total_TTC(totalHT):  # calcul ttc
    return round(totalHT * 1.20, 2)             # ligne index 4 tva, que je pourrais mettre en 0


for item in ligne:                      # boucle recuperation des données des commande
    resultat = sous_total_ligne(item)
    totalHT += resultat       # addition des hors taxe



Tva = total_TTC(totalHT) - totalHT
print ('Total Hors taxe:',totalHT, "euro")
print ('Tva:',round (Tva,2), "euro")
print ('Total TTC:', total_TTC(totalHT), "euro")