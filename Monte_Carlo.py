import numpy as np
import scipy as sc
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D


#The first assignment:
def Z():
    z = np.random.uniform(.25,.75)
    return z

#The second assignment:
def Pdf(x,mean,stan):
    f = stats.norm.pdf(x,mean,stan)
    return f

#The function accept-reject:
def acc_rej():
    mean = 45.042761
    stan = 26.582525
    while True:
        x = np.random.uniform(0,90)
        y = np.random.uniform(0,0.016)
        f = Pdf(x,mean,stan)
        if y <= f:
            return x

#Calculation of pi:
def pi():
    a = 0
    for i in range(1000):
        x = np.random.uniform(-1,1)
        y = np.random.uniform(-1,1)
        if x**2 +y**2 <=1:
            a += 1
    return (a/1000)*4

l=[]
for i in range(1000):
    if i%1000 ==0: print(i)
    l.append(pi())
mu = np.mean(l)
sigma = np.std(l)

plt.hist(l, bins=200)
plt.title("pi calculation")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

#the uncertainity in pi calcualtion

l = []
sigma = []
ji = []
for j in range(100,10000,100):
    if j%1100 ==0: print(j)
    for i in range(j):
        l.append(pi())
    sig = np.std(l)
    ji.append(j)
    sigma.append(sig)
plt.plot(ji,sigma, 'b')
plt.show()

#Combing both Z and theta:

k = []
h = []
for i in range(1000):
    k.append(Z())
    h.append(acc_rej())

pyplot.hist(k,bins= 'auto',label='Z',color='b',alpha=0.5)
pyplot.hist(h,bins=50,color='g',label='Theta',alpha=0.8)
pyplot.legend(loc='upper right')
plt.show()

#3-D hostogram 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x  =  l
y  =  h
hist, xedges, yedges = np.histogram2d(x, y, bins= 200)#, range=[[0, 4], [0, 4]])

xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

# Construct arrays with the dimensions for the 16 bars.
dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='m', zsort='average')

plt.show() 

# The new distribution of Z:

def Z_():
    x = random.uniform(0.25,0.75)
    y = 1/(x+0.0001)
    return y

#The new distribution of theta:
def theta():
    x = random.uniform(0,np.pi*5/180)
    y = 1/(0.0001+x)
    return y
