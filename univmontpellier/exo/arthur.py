taille_sapin=int(input("Taille sapin :"))
taille_tronc=int(input("Taille tronc :"))
nb_sapin=int(input("Nombre de sapins :"))
val_max=((taille_sapin)*2)-1

for i in range(taille_sapin):
    val=((i+1)*2)-1
    print((" "*round((val_max-val)/2)+"*"*val+" "*round((val_max-val)/2)+" ")*nb_sapin)
for j in range(taille_tronc):
    print((" "*(taille_sapin-1)+"*"+" "*(taille_sapin-1)+" ")*nb_sapin)