import numpy as np;
import pandas as pd;
arr = np.random.randint(1,10,(3,3));
subarr = arr[0][0:2];
print(arr);
print(subarr);
calories = {"day1": 420, "day2": 380, "day3": 390}
nig = pd.Series(calories);
print(nig)

