import pandas as pd

achat = pd.read_csv('achats.csv')

col_pommes = achat["pommes"]
col_orange = achat["oranges"]
moy = col_pommes.mean()
moy2 = col_orange.mean()

col_pommes.fillna(moy, inplace=True)
col_orange.fillna(moy2, inplace=True)

print(achat.describe())