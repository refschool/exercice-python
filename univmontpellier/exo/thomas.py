#Version 5
taille_sapin=int(input("Taille sapin :"))
val_max=((taille_sapin)*2)-1

for i in range(taille_sapin):
    val=((i+1)*2)-1

    print(" "*round((val_max-val)/2)+"*"*val)
for j in range(2):
    print(" "*(taille_sapin-1)+"*")