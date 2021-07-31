import pandas as pd

""" réglage pour le display """
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)

data = pd.read_excel('donnees-dropna.xlsx',engine='openpyxl')
#transformer friendly en 1 0 sinon (col G)

def condition(value):
    if value in ['Friendly','friendly']:
        return 1
    return 0


data['Deal Attitude'] = data['Deal Attitude'].apply(condition)
data.to_excel('donnees-friendly.xlsx',index=False)
