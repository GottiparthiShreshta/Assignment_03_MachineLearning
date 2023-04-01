'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import matplotlib.pyplot as plt
import numpy as np
y = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
mylabels = ["Java", "Python", "PHP", "JavaScript","C#","C++"]
plt.pie(y,labels=mylabels, shadow=True,explode=(0.1, 0, 0, 0,0,0), autopct='%1.2f%%')
plt.show()
