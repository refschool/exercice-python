try:
    masse= int(input('Masse en kg : '))
    taille = float(input('Votre taille en cm : '))
    imc = masse / (taille * taille)
except ValueError:
    print('Valeur invalide')