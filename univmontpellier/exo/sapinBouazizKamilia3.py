liste = int(input("Bonjour, quelle taille de sapin souhaitez vous ? :"))
sapin = []

for i in range(0,liste*2,2):
    if i == 0 :
        sapin.append("*")
    else:
        sapin.append("*" * (i+1))

largeur = 2 * liste - 1
sapin.append("*")
sapin.append("*")
for ligne in sapin:
    print(ligne.center(largeur))