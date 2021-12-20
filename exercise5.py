import numpy as np

path = r"C:\Users\jerzy\Desktop\sample_treated.npz"

data = np.load(r"C:\Users\jerzy\Desktop\sample_treated.npz")

lst = np.array(data['outputs'])

for i in range(len(lst)):
    lst2 = lst[i]
    length = len(lst2) - 1
    last = lst2[length]
    first = lst2[0]

    if last >= 2*first:
        print(i, first, last)

