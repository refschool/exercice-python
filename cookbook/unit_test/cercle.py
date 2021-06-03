
from math import pi

def cercle_area(r):
    #Si r est négatif ==> raise ValueError
    #Si le type de r n'est pas "float" ou "int" ==> raise TypeError
    verif = (type(r) == float or type(r) == int )
    if (verif == False):
        raise TypeError(" r n\'est pas un nombre ")
    elif (r < 0) :
        raise ValueError(" r est négatif ")
    else:
        return pi * (r**2)




