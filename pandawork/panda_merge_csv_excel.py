import pandas as pd
df = pd.DataFrame()
fichier1 = pd.read_excel('fichier1.xlsx',engine='openpyxl')
fichier2 = pd.read_excel('fichier2.xlsx',engine='openpyxl')

df = pd.concat([fichier1,fichier2])
#df = df.iloc[: , 1:]
df.to_excel("excelexcel.xlsx",index=False)

"""import pandas as pd
df = pd.DataFrame()
fichier1 = pd.read_csv('fichier2.csv')
fichier2 = pd.read_csv('fichier1.csv')
df = pd.concat([fichier1,fichier2])


df.to_csv("csvcsv.csv")"""