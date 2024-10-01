import pandas as pd
import matplotlib.pyplot as plt
""" réglage pour le display """
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 5000)

df = pd.read_excel('donnees-acquiror.xlsx',engine='openpyxl')
new_df = pd.read_excel('donnees.xlsx',engine='openpyxl')


""" add empty new col"""
df["Target As Acquiror Date"] = ""

""" cette liste est un extrait des colonnes qui nous sont nécessaires pour trouver les targets qui sont aussi acquiror"""
""""on va trouver les target qui ont été acquiror il y a moins de 5 ans"""
target = df['Acquiror Full Name'].tolist()
acquiror_date = pd.concat([df['Acquiror Full Name'],df['Date Announced']],axis=1)

print(acquiror_date)
also_acquiror = []

def get_also_acquiror(value):
    """ si le target est aussi acquiror """
    if(value in target):
        """ on met dans la liste also_acquiror pour trouver les dates dans un second temps"""
        also_acquiror.append(value)

        return value
    return 'No'




df['gotcha'] = df['Target Full Name'].apply(get_also_acquiror)

df.to_excel('also_acquiror.xlsx', index=False)

boolean_serie = new_df['Acquiror Full Name'].isin(also_acquiror)
filtered_df = new_df[boolean_serie]


filtered_df.to_excel('final.xlsx', index=False)

print('allso acquiror, ',also_acquiror)