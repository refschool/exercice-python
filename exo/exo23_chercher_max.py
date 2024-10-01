liste = [65,14,22,101,10,9,18,71]
sorted_list = []
sorted_list2 = []
def get_max(tmp_liste):
    max = tmp_liste[0]
    for x in tmp_liste:
        if(max > x):
            max = x
    return max

"""while(len(liste) > 0):
    max = get_max(liste)
    sorted_list.append(max)
    liste.remove(max)
    #liste.pop(liste.index(max))
    #remove() is shorter"""


'''for i in range(len(liste)):
    maxi = get_max(liste)
    liste.remove(maxi)
    sorted_list2.append(maxi)'''

#parcourir par valeur force à utiliser la boucle while
#parcourir par index permet d'utiliser la boucle for
for i in liste:
    maxi = get_max(liste)
    liste.remove(maxi)
    sorted_list2.append(maxi)

print(sorted_list2)

