# -*- coding: utf-8 -*-
"""
This code unpacks a csv file and creates a set of superimposed bar graphs with
a good amount of figure customization.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

colnames = ['Country','Deployed','Total','Status']
df = pd.read_csv('NPData.csv',names=(colnames))
df = df.reset_index(drop=True)

#print(df) <- for troubleshooting dataframe

totcol = '#cc0000'
depcol = 'white'
bg = '#e6e6ff'
cap = '#99e6e6'
x = np.arange(1,10,1)
labels = (df['Country'])
no = []
total = df['Total']
dep = df['Deployed']
width = .9

# for loop for getting rid of _ in stings

for i in labels:
    if '_' in i:
        no.append(i.replace("_", " "))
    else:
        no.append(i)
        
# Building the plot

fig = plt.figure(figsize = (10,6))
ax = fig.add_subplot(111)
axes = plt.gca()
axes.yaxis.grid(color = 'white')
axes.set_axisbelow(True)
ax.set_facecolor(bg)

ax.bar(x=no, 
       height=total,
       width=width, 
       align='center', 
       color = totcol, 
       edgecolor = 'black',
       label = 'Total Warheads')

ax.bar(x=no, 
       height=dep, 
       width=width/2,  
       align='center', 
       color = depcol, 
       edgecolor = 'black', 
       hatch="///", 
       label = 'Deployed Warheads')

ax.legend(facecolor=cap, 
          framealpha=.75, 
          edgecolor = 'black', 
          shadow = True)

ax.text(4, 4325, 
        'Estimates from the Federation of American Scientists\nlatest update was in November 2018', 
        style='italic',
        bbox={'facecolor': cap, 'alpha': 0.75, 'pad': 5})

plt.ylabel('Total and Deployed Warheads')
plt.xticks(rotation = 'vertical')
plt.show()