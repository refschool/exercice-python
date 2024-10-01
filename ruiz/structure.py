
""" les listes sont faites pour contenir plusieurs chose
qu'une variable ne saurait pas faire car une variable
 ne contient qu'une chose"""
# listes faites pour contenir plusieurs chose homogène
maliste = [5,32,4,5,8,9]
classe3eme = ['jules','Pablo','Matt','Yvon','Jesus','Diego']

# mais il est possible de mélanger les types
#non conseillé
maliste3 = [1,"Jules",35,"Eric"]

# une classe avec 25 élèves
prenom = "Jules"
prenom2 = "Pablo"
prenom3 = "Matt"

""" pour tout type de programme Trombinoscope"""
#print(prenom)
#print(prenom2) # etc
"""for eleve in classe3eme:
    print(eleve,end='')"""

# dictionnaire pour contenir plusieurs choses différent (hétérogène)
eleve = {
    'prenom':'Pablo',
    'nom':'Ruiz',
    'adresse':'ton adress',
    'telephone':'06012446446'
}

# accès aux données du dictionnaire
print(eleve['prenom'])
print(eleve['nom'])
#et de la liste
print(classe3eme[0])
print(classe3eme[1])
