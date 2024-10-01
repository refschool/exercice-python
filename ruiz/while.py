#boucle for  == ceinture jaune
""" on utilise for quand on sait à l'avance combien fois on va exécuter le bloc de code"""
"""for i in range(5):
    print(i)"""
#while == ceinture bleue

"""on utilise while quand on ne sait pas à l'avance combien de fois on va exécuter le code"""
i = 0 # o initialise la variable i à 0
"""while i < 5: # condition:tant que i est < 5 on va exécuter le bloc de code
    #le bloc de code à exécuterr tant que la condition est vraie
    print("hello i =", i)
    i = i + 1"""

# deviner un nombre

"""for i in range(5):
    nb = int(input("entrez un nombre : "))
    if (nb == nombre_a_deviner):
        print("Bravo vous avez trouvé le nombre mystère")
    else:
        print("Désolé vous avez perdu")"""

# la boucle while résoud le problème

nombre_a_deviner = 5
np = 0
while np != nombre_a_deviner :
    np = int(input("entrez un nombre : "))
    if (np == nombre_a_deviner):
        print("Bravo vous avez trouvé le nombre mystère")
    else:
        print("Désolé vous avez perdu")

" on joue à un jeu, je pense à un nombre, et tu devras proposer un nombre et (...) tu n'auras" \
"pas trouvé tu devras continuer  "