#  https://stackoverflow.com/questions/29042276/plotting-a-dataframe-pandas-in-pycharm-not-displaying/29042575

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('titanic.xls')

data = data.drop(['name','sibsp','parch','ticket','cabin','embarked','boat','body','home.dest',],axis=1)


data = data.dropna(axis=0)

print(data['pclass'].value_counts())

data['pclass'].value_counts().plot.bar()

plt.show()