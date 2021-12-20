import numpy as np

path = r"C:\Users\jerzy\Desktop\iris.csv"
data = np.loadtxt(path, delimiter=",", skiprows=1, usecols=np.arange(0,4))

print("Średnia dla każdej z kolumn: ", np.mean(data,0))
print("mediana dla każdej z kolumn: ", np.median(data,0))
print("odchylenie standardowe dla każdej z kolumn: ", np.std(data,0))
