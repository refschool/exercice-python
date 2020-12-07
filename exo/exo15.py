try:
    liste = [1,2,5,3]
    x= int(input('entrez un chiffre:'))
    print(liste[x])
except IndexError:
    print('index hors liste')
except ValueError:
    print('Entrez un chiffre !')