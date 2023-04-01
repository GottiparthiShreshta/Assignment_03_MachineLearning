'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import numpy as np
m = np.array([[3, -2],
			[1, 0]])
print("Original square array:\n",
	m)
w, v = np.linalg.eig(m)
print("Eigen values of the given square array:\n",
	w)

print("Right eigenvectors of the given square array:\n",
	v)
