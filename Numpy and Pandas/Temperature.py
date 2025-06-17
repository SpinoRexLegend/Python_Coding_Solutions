import numpy as np
Temp = [22.1, 23.5, 21.3, 24.0, 22.8, 23.2, 21.9, 23.4, 22.0, 24.1, 23.3, 21.7, 24.2, 22.5, 23.8, 22.3, 23.1, 24.5, 22.2, 23.9, 21.6, 23.7, 22.4, 24.3, 22.9, 23.6, 21.5, 24.4, 22.7, 21.8]
Temparr = np.array(Temp)
print(Temparr.mean())
for i in range(len(Temparr) ):
    Temparr[i] = (Temparr[i] * 9/5)+32
print(Temparr)
