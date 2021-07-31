#https://medium.com/@danalindquist/https-medium-com-danalindquist-bar-chart-of-weekly-data-count-using-pandas-5c95a536a08e
import pandas as pd
import matplotlib.pyplot as plt
""" réglage pour le display """
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)

data = pd.read_excel('donnees-friendly.xlsx',engine='openpyxl')
#transformer friendly en 1 0 sinon (col G)

def year(value):
    """ Timestamp.year"""
    return value.year

#replace date by year
data['Date Announced'] = data['Date Announced'].apply(year)
#group by year

#byyear = data.groupby([data['Date Announced']])['value'].count()
"""sort_index does sort by date"""
data['Date Announced'].value_counts().sort_index().plot.bar()
plt.show()

#byyear.plot(kind='bar',figsize=(10,5),legend=None)

#data.to_excel('donnees-year.xlsx',index=False)
