"""
liste = [3, 6, 1, 4]

def liste_de_listes(liste):
    l = []
    for i in liste:
        l.append([i])
    return l


def inter_deux(l1,l2):
    l = []
    for i in l1:
        for j in l2:
            if i < j:
                l.append(i)
                l1.remove(index(i))
            else:
                l.append(j)




liste1 = [1, 5, 8]
liste2 = [2, 3, 7, 10, 13]

print(liste1[3])"""

liste = [1,2,3,4]
sousliste = liste[1:]
print(sousliste)