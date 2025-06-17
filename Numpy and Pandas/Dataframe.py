import pandas as pd
import numpy as np
b = np.zeros(4)
a1 = ['apple', 'mango', 'banana', 'mango']
a1= np.array(a1)
for i in range(4):
    if (a1[i] == 'mango'):
        b[i] = True
print(a1)
print(b)
rand = np.random.randint(0,10,(4,5))
print("Rnadom array is: ",rand)

filled = np.full((3,4),5)
print("The filled array is: ",filled)

nrange = np.arange(5)
print("The arange array is: ",nrange)

