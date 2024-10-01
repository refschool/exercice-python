import pandas as pd
import openpyxl
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)
cible = pd.read_excel('crypto.xlsx',engine='openpyxl',sheet_name='cible',index_col="Nom")
source = pd.read_excel('crypto.xlsx',engine='openpyxl',sheet_name='source',index_col = "Nom")

""" chercher les rows par index"""
rows = cible.loc[["ETH","ADA","BTC","BTC"]]


""" insérer dans un autre df """


tmpdf = pd.DataFrame(rows)

tmpdf.append(rows)

result = pd.concat([source,tmpdf],axis=1,join = "inner")
print(result)

result.to_excel('data2.xlsx',index=True)


"""
sourceName = source['Nom']
cibleNAme = cible['Nom']


#chercher une valeur dans une colonne
#copier un row avec pandas


#construire le dataframe 2
# get column names
liste_nom_columns = []
for col in cible.columns:
    liste_nom_columns.append(col)
#creation du dataframe vide
df = pd.DataFrame(columns=liste_nom_columns)

df.loc[-1] = [2,3,6]


print(df.head)
#data2.to_excel('data2.xlsx',index=False)
"""