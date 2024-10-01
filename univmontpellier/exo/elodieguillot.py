#sapin
"""pos_etoiles= [1,3,5,7,1,1]
pos_espaces= [3,2,1,0,3,3]
sapin=len(pos_etoiles)
for i in range(sapin):
    print(" "*pos_espaces[i]+"*"*pos_etoiles[i])
    """


#sapin
taille=int(input("choisir la taille"))
for i in range(1,taille*2,2):
    print(("*"*i).center(taille*2))
print(("*").center(taille*2))
print(("*").center(taille*2))