import pandas as pd
import math

df = pd.DataFrame({
    'IQ':[100,140,90,85,120,110,95],
    'GPA':[3.2,4.0,2.9,2.5,3.6,3.4,3.0],
    'SALARY':[45e3,150e3,30e3,25e3,75e3,60e3,38e3]
    })

# Get pairwise correlation coefficients
cor = df.corr()

print(cor)

# Independent variables
x = 'IQ'
y = 'GPA'

# Dependent variable
z = 'SALARY'

# Pairings
xz = cor.loc[ x, z ]
yz = cor.loc[ y, z ]
xy = cor.loc[ x, y ]

Rxyz = math.sqrt((abs(xz**2) + abs(yz**2) - 2*xz*yz*xy) / (1-abs(xy**2)) )
R2 = Rxyz**2

# Calculate adjusted R-squared
n = len(df) # Number of rows
k = 2       # Number of independent variables
R2_adj = 1 - ( ((1-R2)*(n-1)) / (n-k-1) )