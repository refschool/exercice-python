liste = [65,14,22,101,10,9,18,71]
sorted_list = []

def get_max(tmp_liste):
    max = 0
    for x in tmp_liste:
        if(max < x):
            max = x
    return max

while(len(liste) > 0):
    max = get_max(liste)
    sorted_list.append(max)
    liste.remove(max)
    #liste.pop(liste.index(max))
    #remove() is shorter





print(sorted_list)

