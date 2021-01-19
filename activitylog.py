import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

df = pd.read_csv('122020activitylog.csv',error_bad_lines=False)
df.set_index('Type')

#print(df[  df['Auteur'].str.match('forma')])
print(df[  df['Auteur'].str.contains('DUC')])


#print(df.head(5))
#print(df.shape)