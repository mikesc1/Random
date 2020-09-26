# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:08:34 2018

@author: Michael Curtis

"""
import numpy as np
from scipy.linalg import solve
N = int(input("Input Number of Resistors (Even Numbers Only):  "))

#these two arrays are the base for the top and bottom lines of the matrix A

top = np.array([3,-1,-1,0])
bottom = np.array([0,-1,-1,3])

#this section adds zeros to the front and back of the top and bottom lines to scale them
#to the proper size before they are put into the A Matrix

topzeros = np.pad(top, (0,N-4), 'constant')
zeroarray = np.zeros([N-4])
bottomzeros = np.hstack([zeroarray,bottom])

#this sections generates the banded matrix that is used generated to account for any number of 
#N internal resistor connectons. It then cuts off the first and last line so that the modified top and bottom
#lines can replace them and the matrix will be square and correct.

matrix = np.eye(N,N,k=-2)*-1 + np.eye(N,N,k=-1)*-1 + np.eye(N,N)*4 + np.eye(N,N,k=1)*-1 + np.eye(N,N,k=2)*-1
firstdelete = np.delete(matrix,0,0)
lastdelete = np.delete(firstdelete,-1,0)

#these lines add the top and bottom lines onto the modified banded matrix generated above.

addbottom = np.append(lastdelete,bottomzeros)
addtop = np.append(topzeros,addbottom)
FinalA = addtop.resize(N,N)


print("\n")
print("Matrix A is ")

print(addtop)

#this line scales the matrix b in order for it to be the correct size to be solved with matrix A.

b = np.array([5]*2 + [0]*(N-2))
print("\n")
print("Matrix b is ")
print(b)
print("\n")

solution = solve(addtop,b)

print("Using Av=b the voltage drops across the resistors are\n\n ")
print(str(solution) + " \n\nvolts respectively for V1, V2, V3, ...VN")

#if you feed this input 4 resistors the results are exactly the same as the
#code for problem 1 which should be expected.



