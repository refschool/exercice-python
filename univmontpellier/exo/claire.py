"""consigne"""

#     *
#    ***
#   *****
#  *******
#     *
#     *

#     yvon.huynh@gmail.com

# print("*" * 3) >> ***
# for etoile in [1,3,5,7]:




"""exercice"""

#METHODE1 avec liste comme demandé


#initialisation de mes variables pour fabriquer un sapinou
nb_etage = int(input("entre le nombre d'étages que tu veux pour ton saping : "))

etoile = "*"
espace = " "

liste_etoile = []
liste_espace = []



"""
#methode de calcul que j'ai utilisé pour décomposer et comprendre l'exercice 

last_etage = nb_etage - 1 
nb_etoiles_last_etage = last_etage * 2 + 1 
nb_espace_first_etage = nb_etoiles_last_etage / 2 - 0.5
nb_espace_first_etage = int(nb_espace_first_etage)


for num_etage in range(nb_etage):
    # print("num_etage =", num_etage)
    listeetoile.append( num_etage * 2 + 1)
    liste_espace.append( nb_espace_first_etage - num_etage )
"""



for num_etage in range(nb_etage):
    liste_etoile.append(num_etage * 2 + 1)
    liste_espace.append(nb_etage - 1 - num_etage )

# print(liste_etoile)
# print(liste_espace)


#pour que le sapinou s'affiche :
for num_etage in range(nb_etage):
    etoile_ligne = etoile * liste_etoile[num_etage]
    espace_ligne = espace * liste_espace[num_etage]
    ligne = espace_ligne + etoile_ligne
    print(ligne)


#pour que le petit tronc s'affiche :
espace_avant_millieu = nb_etage - 1

print(espace * espace_avant_millieu + etoile)
print(espace * espace_avant_millieu + etoile)





#METHODE2 sans les listes

nb_etage = int(input("entre le nombre d'etages de ton sapin :"))
for num_etage in range(nb_etage):
    print( " " * (nb_etage - num_etage - 1) + '*' * (num_etage * 2 + 1) )

for tronc in range(2):
    print( " " * ( nb_etage - 1 ) + "*")  