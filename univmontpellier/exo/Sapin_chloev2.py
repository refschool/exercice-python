def print_sapin(hauteur):
    for i in range(1, hauteur + 1):
        print(" " * (hauteur - i) + "*" * (2 * i - 1))
    for _ in range(2):
        print(" " * (hauteur - 1) + "*")

# Demander à l'utilisateur de saisir la hauteur qu'il veut
hauteur_sapin = int(input("Entrez la taille de votre sapin (à partir de 3): "))
print_sapin(hauteur_sapin)
