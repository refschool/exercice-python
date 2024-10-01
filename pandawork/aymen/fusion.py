import pandas as pd
import openpyxl
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)
acq_df = pd.read_excel('sample2.xlsx',engine='openpyxl',sheet_name='Acq1k')
immuable_df = pd.read_excel('sample2.xlsx',engine='openpyxl',sheet_name='immuable')

df = acq_df.drop(acq_df[acq_df['Name'] == '#ERROR'].index)

""" Acquiror RIC """
uniques = []

uniques = acq_df['Acquiror RIC'].unique()

#acq_df2 = acq_df[~acq_df['Name'].str.contains("#ERROR")]
print(type(uniques))
print(uniques)


