#
# Simple cube plot
#

import numpy as np 
import matplotlib.pyplot as plt

v0 = 5
g = 9.81
t = np.linspace(1, 3, 3)

y = t**3

plt.plot(t, y)
plt.xlabel('Length of side')
plt.ylabel('Volume')
plt.show()