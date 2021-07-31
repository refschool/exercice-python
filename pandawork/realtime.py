import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.arange(100)
y = np.random.rand(100)
df = pd.DataFrame({"x":x, "y":y})
df2 = df[0:0]

plt.ion()
fig, ax = plt.subplots()
i=0
while i < len(df):
    df2 = df2.append(df[i:i+1])
    ax.clear()
    df2.plot(x="x", y="y", ax=ax)
    plt.draw()
    plt.pause(0.2)
    i+=1
plt.show()