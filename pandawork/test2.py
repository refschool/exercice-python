import pandas as pd
import sqlite3
con = sqlite3.connect("datasci.db")
"""
data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

#purchases = pd.DataFrame(data)

purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

print(purchases.loc['June'])
"""


df = pd.read_csv('sample2.csv', index_col=0)
#df.to_json('new_purchases.json')
df.to_sql('new_purchases', con)
