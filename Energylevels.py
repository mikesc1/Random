"""
@author: micha

I think was for a a 2D energy well...
"""

size = float(input("Input Well Dimensions: "))

level = int(input("Specify Energy level: "))

energy = ((level**2)*((6.626e-34)**2)*(3.14**2))/((2)*((9.109e-31)**2)*(size**2))

print("Value of that energy level is " + str('%.2E' % energy) + " J")

