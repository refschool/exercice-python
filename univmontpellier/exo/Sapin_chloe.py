def print_sapin(hauteur):
    for i in range(1, hauteur + 1):
        print(" " * (hauteur - i) + "*" * (2 * i - 1))
    for _ in range(2):
        print(" " * (hauteur - 1) + "*")

hauteur_sapin = 4  # Vous pouvez changer cette valeur pour ajuster la hauteur du sapin
print_sapin(hauteur_sapin)
