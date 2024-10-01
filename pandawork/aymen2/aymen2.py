import pandas as pd
import openpyxl
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)
cible = pd.read_excel('aymenoriginal.xlsx',engine='openpyxl',sheet_name='cible',index_col="Organization Name")
source = pd.read_excel('aymenoriginal.xlsx',engine='openpyxl',sheet_name='source',index_col = "Organization Name")


""" extraction de la colonne index"""
liste_nom_columns = source.index.tolist()


""" chercher les rows par index"""
rows = cible.loc[liste_nom_columns]

""" insérer dans un autre df """
tmpdf = pd.DataFrame(rows)

tmpdf.append(rows)
print('tmpdf shape = ',tmpdf.shape)
print('source shape = ',source.shape)

""" le fichier data3 est à copier-coller dans Excel (pas réussi à faire en programmatique (erreur sur les données??)
le copier coller dans Excel est très facile donc ce n'est pas une problème, investiguer en Python prendrait peut etre des jours
"""
tmpdf.to_excel('data3.xlsx',index=True)