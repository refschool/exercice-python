import matplotlib

print(matplotlib.__version__)
print(__name__)


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 200])

plt.plot(xpoints, ypoints)
plt.show()
