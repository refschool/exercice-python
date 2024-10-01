master = ['J','V','R','J']
master_copy = []
propal = ['J','V','V','B']
propal_copy = []

nb_noire = 0
for index in [0,1,2,3]:
    if propal[index] == master[index]:
        nb_noire = nb_noire + 1
    else:
        master_copy.append(master[index])
        propal_copy.append(propal[index])

nb_blanc = 0
for couleur in master_copy:
    if couleur in propal_copy:
        propal_copy.remove(couleur)
        nb_blanc = nb_blanc + 1

print(master)
print(propal)
#print(propal_copy)
print("N" * nb_noire,"B" * nb_blanc)