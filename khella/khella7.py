

def eboult_possible(liste):
    for i in range(0,len(liste)-1):
        if (liste[i] - liste[i+1]) >= 2:
            return True
    return False


def indice_eboult(liste):
    for i in range(0,len(liste)-1):
        if (liste[i] - liste[i+1]) >= 2:
            return i
    return False


liste = [8,5,3,3,2]
#liste = [8,7,1]
if(eboult_possible(liste) == True):
    print(indice_eboult(liste))

def eboult_col(liste,indice):
    liste[indice] = liste[indice] - 1
    liste[indice+1] = liste[indice+1] + 1
    return liste


def stabilisation(liste):
    while(eboult_possible(liste) == True):
        indice = indice_eboult(liste)
        liste = eboult_col(liste,indice)

    return liste

