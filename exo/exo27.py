import json

liste = ['Yvon', 'Huynh']
montuple = ('Yvon','Huynh')
dico = { "nom":"Huynh", "prenom":"Yvon"}
#fichier = open('php.txt','w')
#fichier.writelines('%s\n' % liste)
#fichier.writelines('%s\n' % dico)
#fichier.write(''.join(montuple))

#fichier.writelines('bonjour les Pythonists')


# méthode 1 pour dumper un dico
"""json = json.dumps(dico)
print("*",type(dico))
print("**",type(json)) # sérialization
fichier.writelines(json)"""


#méthode plus rapide

fichier = open('toto.txt','w')
json.dump(dico,fichier)