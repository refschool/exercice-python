
Paris = {
    "Centre Pompidou" : {'Chagall', 'Delaunay', 'Matisse', 'Miro', 'Munch',
'Picasso'},
"Musee d'Art Moderne" : {'Delaunay', 'Picabia', 'Picasso', 'Warhol'},
"Musee de l'Orangerie" : {'Matisse', 'Picasso'},
"Musee d'Orsay" : {'Munch'},
"Musee Picasso" : {'Picasso', 'Braque', 'Miro'}
}

def tous_artistes(Paris):
    artistes = set()
    for cle in Paris:
        artistes = artistes | Paris[cle]
    return artistes

def expose_artiste(Paris,artiste):
    musees = set()
    for cle in Paris:
        if artiste in Paris[cle]:
            musees.add(cle)
    return musees

def conversion(Paris):
    """ on extrait tous les artistes dédoublonnés"""
    artistes_set = set()
    artistes_set = tous_artistes(Paris)

    """ on initialise les variables"""
    artiste_dict = {}
    """ on boucle sur le artistes_set
     pour chaque artiste on cherche les musées"""
    for artiste in artistes_set:
        musees = set()
        musees = expose_artiste(Paris,artiste)
        artiste_dict[artiste] = musees

    return artiste_dict

print(conversion(Paris))