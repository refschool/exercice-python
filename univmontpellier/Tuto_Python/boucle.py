"""boucle for et while
REPETER un bout de code tant que la condition est remplie
2 types de boucle:
boucle for (pour de 1 à 10 par exemple)
boucle while (tant que)
"""
#for itère sur un intervalle de 0 à 4
"""for i in range(5):
    print(i)"""
#syntaxe 1
"""for i in range(10):

    if(i>5):
        print("image compressé !",i)
    else:
        print("pas une image")"""

#syntaxe2
for i in [1,2,3,4,5,6,7,8,9,10]:
    """ si i est supérieur à 5 c'est une image"""
    if(i>5):
        print("image compressé !",i)
    else:
        print("pas une image")

 # "parcourir une liste de prénom" et dire bonjour prénom
listePrenom = ["pierre","paul"]
for prenom in listePrenom:
    print('bonjour',prenom)


