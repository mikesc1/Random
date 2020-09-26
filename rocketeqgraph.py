# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:41:38 2018

@author: Michael
"""

import numpy as np
import matplotlib.pyplot as plt

mf_over_m0 = np.logspace(-0.5, -10, 20)

delta_v_over_ve = -np.log(mf_over_m0)

# that's it - the rest is just plotting @@!

fig = plt.figure(figsize=[16, 8])

xlab,   ylab   = "mf / m0",             "delta v / v exhaust"
title1, title2 = "x-axis linear scale", "x-axis log scale"

ax1 = plt.subplot(121, xlabel=xlab, ylabel=ylab, title=title1)
ax2 = plt.subplot(122, xlabel=xlab, ylabel=ylab, title=title2)

# from here: http://stackoverflow.com/a/14971193/3904031
for ax in [ax1, ax2]:
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
                 ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(20)
    ax.invert_xaxis()

for ax in [ax1, ax2]:
    ax.plot(mf_over_m0, delta_v_over_ve, 'ok')
    ax.plot(mf_over_m0, delta_v_over_ve, '-b')
ax2.set_xscale('log')

plt.savefig("rocket equation question")
plt.show()