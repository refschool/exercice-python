# Import seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame


Index= ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
#Cols = ['A', 'B', 'C', 'D']
Cols = ['A', 'B']

obj = {
    'A':[1,2,3,4,5,12,4,3,5],
    'B':[5,4,6,3,2,0.1,7,8,6]
}

df = DataFrame(obj)

#df = DataFrame(abs(np.random.randn(5, 2)), index=Index, columns=Cols)

sns.heatmap(df, annot=True)

plt.show()