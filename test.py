import pandas as pd

df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]},index=['falcon', 'dog'])
print(df)
print(df.iloc[1,1])