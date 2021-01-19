import json

liste = ['Yvon', 'Huynh']

montuple = ('Yvon','Huynh')

dico = { "nom":"Huynh", "prenom":"Yvon"}

fichier = open('php.txt','w')



#fichier.writelines('bonjour les Pythonists')
json = json.dumps(dico)
fichier.writelines(json)

"""
import datetime
x = datetime.datetime.now()
print('*** ',x.strftime('%B %a'))"""

import os, platform