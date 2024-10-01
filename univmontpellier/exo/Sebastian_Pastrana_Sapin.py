def dessiner_arbre (height):
    # Boucle sur chaque ligne de l'arbre
    for i in range(1, height + 1):
        # Imprimer les espaces avant les astérisques sur chaque ligne
        for j in range(height - i):
            print(" ", end="")
        # Imprimer les astérisques sur chaque ligne
        for j in range(2 * i - 1):
            print("*", end="")
        # Passer à la ligne suivante après l'impression de chaque ligne
        print()

height = int(input("Indiquez la hauteur de l'arbre: "))
dessiner_arbre(height)

