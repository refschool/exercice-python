#fonction

def nom_fonction(parametre1,parametre2):
    """ le code de ma fonction """
    """ return existe dans les fonctions seulement"""
    resultat = parametre1 + parametre2
    return resultat
    """ return est la dernière instruction exécutée dans une fonction"""
    print('bonjour')

#print(nom_fonction(1,2))


def cuire(plat):
    plat = plat + " Cuit 20 minutes"
    return plat

def faire_pizza(ingredient1,ingredient2,ingredient3):
    pizza_crue = ingredient1 + ingredient2 + ingredient3
    return pizza_crue

pizza1 = faire_pizza("Patate","Sauce","Fromage")

print("pizza1",pizza1)



