"""etoiles = [1,3,5,7,9,1,1]
espaces = [4,3,2,1,0,4,4]

for i in range(7):
    print( " " * espaces[i], "*" * etoiles[i])"""

#Version 2
sapin = int(input("Taille du sapin :"))
tron = int(input("Taille du tron :"))

nb_etoiles = sapin * 2
nb_espaces = sapin - 1

etoiles = list(range(1, nb_etoiles, 2))
espaces = list(range(nb_espaces, -1, -1))

for i in range(sapin):
    print( " " * espaces[i], "*" * etoiles[i])

for _ in range(tron):
    print( " " * nb_espaces, "*")