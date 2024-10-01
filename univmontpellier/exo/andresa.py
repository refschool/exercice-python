# Demande le nombre de lignes pour l'arbre à l'utilisateur
num_lignes = int(input("Entrez le nombre de lignes de l'arbre (le nombre doit être supérieur à 4) : "))

# Vérifie si le nombre de lignes est supérieur à 4
if num_lignes <= 4:
    print("ERROR: Le nombre de lignes doit être supérieur à 4.")
else:
    # Imprime la cime de l'arbre (triangle)
    for i in range(1, num_lignes + 1, 2):
        espaces = (num_lignes - i) // 2
        astérisques = i
        cime = ' ' * espaces + '*' * astérisques
        print(cime)

    # Calcule le nombre d'espaces à gauche du tronc
    espaces_tronc = (num_lignes - 3) // 2

    # Imprime le tronc de l'arbre pour les lignes paires
    if num_lignes % 2 == 0:
        for _ in range(espaces_tronc):
            print(' ' * (espaces_tronc + 1) + '*')
    # Imprime le tronc de l'arbre pour les lignes impaires
    else:
        for _ in range(espaces_tronc - 1):
            print(' ' * (espaces_tronc + 1) + '*')

    # Imprime les deux derniers astérisques
    print(' ' * (espaces_tronc + 1) + '*')
    print(' ' * (espaces_tronc + 1) + '*')