import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

#df = pd.read_csv('activity-log-exportT2.csv',error_bad_lines=False)
#df.set_index('Type')

#print(df[  df['Auteur'].str.match('forma')])
#print(df[  df['Description'].str.contains('regnault')])

fichier = open('regnault.csv','r')
for line in fichier.readlines():
    if 'regnault' in line:
        print(line)
