import pandas as pd
import statsmodels.formula.api as sm


""" réglage pour le display """
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)

data = pd.read_excel('donnees-year.xlsx',engine='openpyxl')
#correlation 3 variable
data = data[['cash','stock','unknown']]



result = sm.ols(formula="cash ~ stock + unknown", data=data).fit()
print(result.params)

#data.to_excel('donnees-correlation.xlsx',index=False)
print(result.summary())