#positionnel et nommé
#questions : peut on inverser les nommés?
#le nommé doit être en derniere position
try:
    masse= int(input('Masse en kg : '))
    taille = float(input('Votre taille en cm : '))
    imc = masse / (taille * taille)
except ValueError:
    print('Valeur invalide')