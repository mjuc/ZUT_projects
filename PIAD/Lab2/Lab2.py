import pandas as pd
import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt
import os

# Zadanie 1
print("Zadanie 1")
df = pd.DataFrame({"x": [1, 2, 3, 4, 5], 'y': ['a', 'b', 'a', 'b,', 'b']})
gr = df.groupby(["x"])
print(gr)

# Zadanie 2
#tst = pd.Series(df)
#vc = tst.value_counts()
#print(vc)

# Zadanie 3
print("Zadanie 3")
at1 = pd.read_csv("C:/PIAD/autos.csv")
#at2 = np.loadtxt("C:/PIAD/autos.csv")
print(at1)
#print(at2)

# Zadanie 4
print("Zadanie 4")
dtfr = at1.groupby(['make'])
mct = at1.groupby(['make']).mean()
print(mct)

# Zadanie 5
print("Zadanie 5")
tst = pd.Series(dtfr["fuel-type"])
a = tst.value_counts()
print(a)

# Zadanie 6
print("Zadanie 6")
ar61 = at1["city-mpg"].to_list()
ar62 = at1["length"].to_list()
a1 = np.polyval(ar62,ar61)
a2 = np.polyfit(ar62,ar61,2)
print(a1)
print(a2)

# Zadanie 7
print("Zadanie 7")
vr = sp.pearsonr(ar62,ar61)
print(vr)

# Zadanie 8
print("Zadanie 8")
plt.plot(ar62,ar61,'b.')
#plt.plot(ar62)
plt.show()

# Zadanie 9
print("Zadanie 9")
x=np.linspace(0,10,500)
est = sp.gaussian_kde(ar62)
plt.plot(x,est(x))
plt.show()

# Zadanie 10
print("Zadanie 10")
ar10 = at1["width"].to_list()
estw = sp.gaussian_kde(ar10)
fig = plt.figure()
fig, ax = plt.subplots(2)
ax[0].plot(x,est(x))
ax[1].plot(x,estw(x))
plt.show()