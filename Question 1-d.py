'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
b = np.reshape(a,(3,2))
print("Reshape to 3x2:")
print(b)
res = np.reshape(a,(2,3))
print("Reshape to 2x3:")
print(res)