grille = list(range(1,50))
j = 0
# constitution de la grille
while j < 5:
    a = input('enter number : ')
    j += 1
    grille[int(a) - 1] = 'X'
# affichage de la grille
for i in range(0,50,5):
     print(grille[i:i+5])


"""
mylist = [1,2,3,4,5,6,7,8,9,10]
for i in mylist[::2]:
    print i,
    """