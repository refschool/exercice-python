import pandas as pd
import openpyxl
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)
df223 = pd.read_excel('aymensample3.xlsx',engine='openpyxl',sheet_name='French FinT rounds 223')
df4221 = pd.read_excel('aymensample3.xlsx',engine='openpyxl',sheet_name='UE FinT 4221')


organization_name223 = df223['Organization Name']
organization_name4221 = df4221['Organization Name']


#chercher une valeur dans une colonne
#copier un row avec pandas
#construire le dataframe 2


# get column names
liste_nom_columns = []
for col in df4221.columns:
    liste_nom_columns.append(col)


#creation du dataframe vide
data2 = pd.DataFrame(columns=liste_nom_columns)


for nom_entreprise in organization_name4221:
    #print(nom_entreprise)
    t = df4221.loc[df4221['Organization Name'] == nom_entreprise]
    #print('trouvé')
    print(t)
    data2.append(t)


data2.to_excel('data2.xlsx',index=False)
"""    
result = pd.concat([df223,t], axis=1, ignore_index=True)

result.to_excel('concat.xlsx', index=False)
"""
#pandas column by index
# append row to a dataframe