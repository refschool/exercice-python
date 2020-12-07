import json

liste = ['Yvon', 'Huynh']

montuple = ('Yvon','Huynh')

dico = { "nom":"Huynh", "prenom":"Yvon"}

fichier = open('test.txt','w')



#fichier.writelines('bonjour les Pythonists')
json = json.dumps(dico)
fichier.writelines(json)