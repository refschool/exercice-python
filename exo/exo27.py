import json

liste = ['Yvon', 'Huynh']
montuple = ('Yvon','Huynh')
dico = { "nom":"Huynh", "prenom":"Yvon"}
fichier = open('php.txt','w')
fichier.writelines('%s\n' % liste)
#fichier.writelines('%s\n' % dico)

#fichier.writelines('bonjour les Pythonists')
"""json = json.dumps(dico)
print("*",type(dico))
print("**",type(json)) # sérialization
fichier.writelines(json)"""

"""
import datetime
x = datetime.datetime.now()
print('*** ',x.strftime('%B %a'))"""

import os, platform