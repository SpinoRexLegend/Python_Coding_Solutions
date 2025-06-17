import numpy as np
import pandas as pd
def sorte():
    n = int(input("Enter the length of the list: "))
    L = [] 
    for i in range(n):
        L.append(int(input("Enter the value: ")))
    print(L)
    for i in range (len(L)-1):
        print(L[i])
        if (L[i] > L[i+1]):
            return False
    return True
print(sorte())
