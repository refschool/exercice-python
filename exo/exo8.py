nb_mystere = 30
ecart_precedent = 100
nb = 40
while(nb != nb_mystere):
    nb = int(input('Entrez un nb entre 2 et 100 : '))
    ecart_courant = abs(nb - nb_mystere)
    if( ecart_courant > ecart_precedent):
        print('Vous refroidissez')
        ecart_precedent = ecart_courant
    else:
        print('Vous chauffez')
        ecart_precedent = ecart_courant
