import pandas as pd
import numpy as np
import openpyxl

""" on paramètre panda pour qu'il nous montre plus de colonne et lignes """
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)

# Ouverture du fichier Excel
df1= dataframe_feuil1 = pd.read_excel('Batch_OutputGenerated_creation.xlsx',engine='openpyxl',sheet_name='Feuil1')
df1['start date']=pd.to_datetime(df1['start date']).dt.date
df1['8million']=df1['8million'].astype(str).str.replace(',0',"")

liste2D= [] # va être transformé en Dataframe après remplissage
listing=[]
ligne=[]
i=1
for index,row in dataframe_feuil1.iterrows():# parcourir ligne par ligne
    rangee = []# variable temporaire pour stocker les info de la ligne
    # construction de la rangée

    if(isinstance(row['pn'],str)): # renvoi le PN kit si la cellule est vide ou non
        labelpn = row['pn']
    if(isinstance(row['kit'], str)):
        rangee.append(row['kit'])
    else:
        rangee.append(labelpn)
    rangee.append("TRUE")
    if(isinstance(row['kit'], str)):
        labelst=row['start date']
        label2='B2B_8MillionKit'
        label3='related'
    else:
        labest=labelst
        label2=label2
        label3=label3
    rangee.append(labelst)
    rangee.append("2099-05-11")
    if (isinstance(row['kit'], str)):
        rangee.append(label2)
    else:
        rangee.append(label3)
    liste2D.append(rangee)


print(liste2D)
liste_million = df1['8million']


for million in liste_million:

    for pn in liste2D:
        ligne = pn + ligne
        ligne.append(million)
        ligne.append(pn[0]+'-'+million+'-'+pn[4])
        ligne.append(i)
        if (isinstance(row['kit'], str)):
            ligne.append(row['n°série debut'])
            ligne.append(row['n°série fin'])
        else:
            ligne.append('')
            ligne.append('')
        listing.append(ligne)
        ligne = []
        i=i+1

#print(listing)
df4= pd.DataFrame(listing)
df4.columns=["ccrz__RelatedProduct__r:ccrz__E_Product__c:ccrz__SKU__c","ccrz__Enabled__c","ccrz__StartDate__c","ccrz__EndDate__c","ccrz__RelatedProductType__c","ccrz__Product__r:ccrz__E_Product__c:ccrz__SKU__c","ccrz__RelatedProductId__c","ccrz__Sequence__c","B2B_SerialNumberRangeStart__c","B2B_SerialNumberRangeEnd__c"]
df4=df4.dropna(subset=['ccrz__Product__r:ccrz__E_Product__c:ccrz__SKU__c'])
#print(df4)
df4.to_excel('CC_Related.xlsx',sheet_name='CC_Price_List_Item',index=False)