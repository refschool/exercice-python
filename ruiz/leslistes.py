""" les liste contiennent des choses homogènes"""
bonne_liste = [1,5,4,7,8,6]
bonne_liste = "Julien"
#              0 1 2 3 4 5
mauvaise_liste = ["jules",31,[3,2,1]]

"""methode souvent utilisée mais pas la plus puissante"""
"""for element in bonne_liste:
    print(element)
"""
""" on accède à un élément à la position i"""
#print(bonne_liste[5])

""" manipulation de liste : extraction d'une sous liste
inversion d'une liste 
CRUD : create (append), read, update, delete (remove)
"""
sousliste = bonne_liste[0:3]
sousliste = bonne_liste[2:5]
sousliste = bonne_liste[0:6]
sousliste = bonne_liste[:]
"""inversion d'une sousliste"""
sousliste = bonne_liste[0:3][::-1]

#print('2',sousliste)


new_liste = [5,9,11]
"""  ajout d'un élément """
#new_liste.append(40)
"""effacement d'un élément"""
#new_liste.remove(9)
""" remplacement d'un élément"""
new_liste[0] = 'X'
print(new_liste)
