'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import numpy as np
array = np.arange(6).reshape(2,3)
print("Original matrix:")
print(array)
result =  np.trace(array)
print("Sum of the diagonal element in given matrix:")
print(result)