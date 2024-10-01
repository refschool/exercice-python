from random import randint
grille = []
for i in range(1,50):
    grille.append(i)

print(grille)

"""" tirage """
"""tirage = []
for x in range(5):
    index = randint(0,50)
    numero = grille[index]
    if(numero not in tirage):
        tirage.append(numero)"""

def getTirage(grille,taille):
    tirage = []
    for x in range(taille):
        index = randint(0,len(grille)-1)
        numero = grille[index]
        if(numero not in tirage):
            tirage.append(numero)
    return sorted(tirage)

magrille = [15,13,21]
tirage = []
i = 0
while(sorted(magrille) != sorted(tirage)):
    i = i + 1
    tirage = getTirage(grille,3)
    print("i =",i,tirage)




print("i = ",i)