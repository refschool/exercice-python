""" chaine de caractères == liste """

bonne_liste = "EST CE QUE TOUT LE MONDE EST LA?"
print(bonne_liste.lower())
#              0 1 2 3 4 5
""" on accède à un élément à la position i"""
#print(bonne_liste[5])

""" manipulation de liste : extraction d'une sous liste
inversion d'une liste 
CRUD : create (append), read, update, delete (remove)
"""
sousliste = bonne_liste[0:3]
sousliste = bonne_liste[2:5]
sousliste = bonne_liste[0:6]
sousliste = bonne_liste[::-1]
"""inversion d'une sousliste"""
sousliste = bonne_liste[0:3][::-1]

grille = [1,2,3,'X','X',6,7,8,9,10,'X',12,13]
i=0
grille.append(i)
numeros_choisis = [5,4,11,23,40] # input