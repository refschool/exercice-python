import pandas as pd
""" réglage pour le display """
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)


data = pd.read_excel('test2.xls')
data = data.dropna(subset=['Premium Paid - 1 Week Prior to Announcement'])
#data["Age"]= data["Age"].replace(25.0, "Twenty five")
print(data.shape)
print(data.head)

data.to_excel('new.xls', index=False)