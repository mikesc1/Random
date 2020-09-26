# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 11:08:55 2018

@author: micha

not sure what this was
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

s = 10
r = 28 
b = 8/3

# definition of the ODE as vector function
def f(d,t):
    # x and y are vector elements
    x=d[0]
    y=d[1]
    z=d[2]
    fx = s*(y-x)
    fy = r*x-y-x*z
    fz = x*y-b*z
    return np.array([fx,fy,fz],float)

start = 0.0 
end = 50
numSteps = 1000
stepSize = (end-start)/numSteps

tpoints = np.arange(start, end, stepSize)
xpoints = []
ypoints = []
zpoints = []
# initial conditions for x and y
d = np.array([0,1.0,0],float)   

# all steps are as normal RK4, but vector valued quantities used
for t in tpoints:
    xpoints.append(d[0])
    ypoints.append(d[1])
    zpoints.append(d[2])
    k1 = stepSize*f(d,t)        
    k2 = stepSize*f(d+0.5*k1,t+0.5*stepSize)   
    k3 = stepSize*f(d+0.5*k2,t+0.5*stepSize)
    k4 = stepSize*f(d+k3,t+stepSize)
    d += (k1+2.*k2+2.*k3+k4)/6

plt.plot(tpoints,xpoints,label='x')
plt.plot(tpoints,ypoints,label='y')
plt.plot(tpoints,zpoints,label='z')
plt.title("RK4 Solution for Two Variables")
plt.xlabel("t")
plt.legend(loc='upper right')
plt.show()

plt.plot(xpoints,zpoints)
plt.show()

lib = odeint(f,[0,1,0],tpoints)

plt.plot(tpoints,lib)
plt.show()
