nb_mystere = 37
ecart_precedent = 100
while(True):
    nb = int(input('Entrez un nb entre 2 et 100 : '))
    ecart_courant = abs(nb - nb_mystere)
    if(nb == nb_mystere):
        print("Trouvé")
        break
    elif( ecart_courant > ecart_precedent):
        print('Vous refroidissez')
    else:
        print('Vous chauffez')
    ecart_precedent = ecart_courant