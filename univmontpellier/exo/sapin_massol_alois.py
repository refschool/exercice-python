taille_sapin=int(input("taille sapin :"))

for i in range (taille_sapin):
    val=((i+1)*2)-1
    print(("*"*val).center(taille_sapin*2))
for j in range(2):
    print("*".center(taille_sapin*2))