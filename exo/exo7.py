nombre_mystère = 90

entree,comptage = -1,0

while (True):
    entree = input('Entrez un nombre entre 0 et 100 (Entrée pour sortir) : ')
    comptage += 1
    if entree == "":
        break
    elif not entree.isdigit():
        print ("Réentrez un nombre")
    elif int(entree) < nombre_mystère:
        print ("trop petit")
    elif int(entree) > nombre_mystère:
        print ("trop grand")
    else:
        print ("trouvé en:", comptage, ' tentatives.')
        comptage = 0

print("Merci d'avoir joué")





#si 1ere tentative = 30
#et 2nde tentative = 35  on dit "vous chauffez"

#si 1ere tentative = 35
#et 2nde tentative = 15  on dit "vous êtes froid"