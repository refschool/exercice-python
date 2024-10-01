hauteur_sapin = int(input("Quelle est la taille de votre sapin :"))

for i in range(hauteur_sapin) :
    val = ((i+1)*2)-1
    print(("*"*val).center(hauteur_sapin*2))
for j in range (2) :
    print("*".center(hauteur_sapin*2))
