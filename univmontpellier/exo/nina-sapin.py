 

hauteur_sapin = 5
for ligne in range (hauteur_sapin): 
 espaces = hauteur_sapin - 1 - ligne 
 etoiles = 2 * ligne + 1
 ligne_sapin = " "* espaces + "*" * etoiles
 print (ligne_sapin)
print (" "*(hauteur_sapin-1)+"*")
print (" "*(hauteur_sapin-1)+"*")