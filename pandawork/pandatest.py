import pandas as pd
"""
data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

#purchases = pd.DataFrame(data)

purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

print(purchases.loc['June'])
"""


df = pd.read_csv('sample.csv', index_col=0)
print(df)