"""taille_sapin = int(input("Taille sapin :"))
for i in range(taille_sapin):
    print(" " * (taille_sapin - i) + "*" * (2 * i - 1))

print ('*'.center(taille_sapin *2))
print ('*'.center(taille_sapin *2))
print ('*'.center(taille_sapin *2))"""


"""print("hello {0}".format("Yvon"))
print("hello {0} ton compte possède {1:9.3f} euros".format("Yvon",1000))
"""
# Nombre de lignes de l'arbre
num_lignes = int(input("Entrez le nombre de lignes que vous souhaitez pour l'arbre (le nombre doit être supérieur à 4) : "))

# Vérifier si le nombre de lignes est supérieur à 4
if num_lignes <= 4:
    print("ERROR: Le nombre de lignes doit être supérieur à 4.")
else:
    # Afficher la partie triangle de l'arbre
    for i in range(1, num_lignes + 1, 2):
        espaces = (num_lignes - i) // 2
        étoiles = i
        cime = ' ' * espaces + '*' * étoiles
        print(cime)

    # Calcule le nombre d'espaces à gauche du tronc
    espaces_tronc = (num_lignes - 3) // 2

    # Afficher le tronc de l'arbre pour les lignes paires
    if num_lignes % 2 == 0:
        for _ in range(espaces_tronc):
            print(' ' * (espaces_tronc + 1) + '*')
    # Afficher le tronc de l'arbre pour les lignes impaires
    else:
        for _ in range(espaces_tronc - 1):
            print(' ' * (espaces_tronc + 1) + '*')

    # Afficher les deux dernieres étoiles
    print(' ' * (espaces_tronc + 1) + '*')
    print(' ' * (espaces_tronc + 1) + '*')