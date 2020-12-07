#Exercice 21 : Chercher le maximum d�une liste

liste = [65,200,14,22,1,10,9,101,18,71]

i=0
Greatest=0

for member in liste:
    if member > Greatest:
        Greatest = member



"""for member in liste:
    if liste[i-1] > liste[i]:
        Greatest = liste[i-1]
    else:
        Greatest = liste[i]
    i=i+1"""
print('--',Greatest)

# ou bien :

liste.sort()
maxValue=liste[len(liste)-1]
print('**',maxValue)