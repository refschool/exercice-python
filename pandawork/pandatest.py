import pandas as pd

data = {
    'pommes': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

achats = pd.DataFrame(data)


achats = pd.DataFrame(data, index=['Jules', 'Robert', 'Lea', 'David'])

achats.columns = [col.upper() for col in achats]
print(achats.columns)