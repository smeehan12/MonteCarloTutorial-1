import numpy as np
import scipy as sc
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D

#Calculation of pi:
def pi():
    a = 0
    for i in range(1000):
        x = np.random.uniform(-1,1)
        y = np.random.uniform(-1,1)
        if x**2 +y**2 <=1:
            a += 1
    return (a/1000)*4

l2=[]
for i in range(1000):
    l2.append(pi())
mu = np.mean(l)
sigma = np.std(l)

plt.hist(l, bins=200)
plt.title("pi calculation")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# the uncertainity in the calculation

l3 = []
sigma = []
ji = []
for j in range(100,10000,100):
    if j%1100 ==0: print(j)
    for i in range(j):
        l3.append(pi())
    sig = np.std(l3)
    ji.append(j)
    sigma.append(sig)
plt.plot(ji,sigma, 'b')
plt.show()

