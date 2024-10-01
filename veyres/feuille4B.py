import pandas as pd
import numpy as np
import openpyxl

""" on paramètre panda pour qu'il nous montre plus de colonne et lignes """
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)

# Ouverture du fichier Excel
df1= dataframe_feuil1 = pd.read_excel('fichier1.xlsx',engine='openpyxl',sheet_name='Feuil1')
liste_prix=['PLEXPLODEDVIEWS-EUR','PLEXPLODEDVIEWS-GBP','PLEXPLODEDVIEWS-NOK','PLEXPLODEDVIEWS-DKK','PLEXPLODEDVIEWS-USD','PLEXPLODEDVIEWS-CHF']
liste2D= [] # va être transformé en Dataframe après remplissage
tmpliste = []


for index,row in dataframe_feuil1.iterrows():# parcourir ligne par ligne
    rangee = []# variable temporaire pour stocker les info de la ligne
    # construction de la rangée

    if(isinstance(row['kit'],str)): # renvoi le PN kit si la cellule est vide ou non
        labelkit=row['kit'] # renvoi le PN kit pour chaque code prix
        labeldate=row['start date']# renvoi la date si la cellule est vide ou non
        rangee.append(labeldate)
        rangee.append('2099-12-31')  # renvoi les valeurs des colonnes feuille1
        rangee.append('99999')
        rangee.append(labelkit)
        """ on met la ligne entière dans la liste 2D """
        liste2D.append(rangee)

    else:
        pass


print(liste2D)

print(liste_prix)
""" on ajoute les prix"""

for prix in liste_prix:
    ligne = []
    for kit in liste2D:
        ligne.append(prix)
        ligne = ligne + kit
        ligne.append(prix+'-'+kit[3])
        tmpliste.append(ligne)
        ligne = []

print(tmpliste)
df4= pd.DataFrame(tmpliste)
df4.columns=["prix","ccrz__StartDate__c","ccrz__EndDate__c","ccrz__Price__c","ccrz__Product__r:ccrz__E_Product__c:ccrz__SKU__c","concat_prix"]
print(df4)
df4.to_excel('feuil4.xlsx', index=False)
