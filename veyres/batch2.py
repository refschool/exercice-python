"""from os import listdir
from os.path import isfile, join
monchemin = ".\\batch2\\"  #le chemin vers les fichiers
print(listdir(monchemin))

fichiers = []
for f in listdir(monchemin):
    print(listdir(join(monchemin,f)))"""
"""    if isfile(join(monchemin, f)):
        fichiers.append(f)"""
"""print(fichiers)"""


import glob

# root_dir needs a trailing slash (i.e. /root/dir/)
for filename in glob.iglob('**/*.svg', recursive=True):
     print(filename)