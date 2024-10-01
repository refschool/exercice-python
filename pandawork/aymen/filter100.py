#https://medium.com/@danalindquist/https-medium-com-danalindquist-bar-chart-of-weekly-data-count-using-pandas-5c95a536a08e
import pandas as pd
import matplotlib.pyplot as plt
""" réglage pour le display """
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)

data = pd.read_excel('donnees-friendly.xlsx',engine='openpyxl')

equal_100 = data[data["Percentage of Stock"]  == 100]
less_100 = data[data["Percentage of Stock"]  < 100]


equal_100.to_excel('donnees-100.xlsx',index=False)
less_100.to_excel('donnees-less100.xlsx',index=False)
