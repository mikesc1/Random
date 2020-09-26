"""
@author: micha
an asymetric 3D random walk
"""

import numpy as np
import matplotlib.pyplot as plt

x = [0]
y = [0]
z = [0]

for n in range(10000):
    step = np.random.randint(1,19)
    if step == 1 or step == 7 or step == 8 or step == 9 or step == 10 or step == 11 or step == 12 or step == 13 or step == 14 or step == 15 or step == 16 or step == 18 or step == 17:
        x.append(x[-1]+1)
        y.append(y[-1])
        z.append(z[-1])
    elif step == 2:
        x.append(x[-1]-1)
        y.append(y[-1])
        z.append(z[-1])
    elif step == 3:
        y.append(y[-1]+1)
        x.append(x[-1])
        z.append(z[-1])
    elif step == 4:
        y.append(y[-1]-1)
        x.append(x[-1])
        z.append(z[-1])
    elif step == 5:
        z.append(z[-1]+1)
        y.append(y[-1])
        x.append(x[-1])
    elif step == 6:
        z.append(z[-1]-1)
        y.append(y[-1])
        x.append(x[-1])
'''
print(x)
print(y)
print(z)
'''
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, color = 'b')
plt.show()
