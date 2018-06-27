import sys
import time
import numpy as np
import matplotlib.pyplot as plt


xt=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7]
tt=[0.1,0.3,0.42,0.45,0.61,0.68,0.7,0.91]

plt.scatter(xt,tt,c='red')
# plt.show()

itr=-1
mew=0.1
w1=np.zeros(shape=(3,9))

def out(x,w,b):
    s=w*x+b
    return s

r=np.random.rand()
w=0.05
r=np.random.rand()
b=0.5

for y in range(0,len(xt)):
    x=xt[y]
    itr=itr+1
    target=tt[y]

    for i in range(0,100):
        output=out(x,w,b)
        # update weights
        w=w+mew*(target-output)*x
        b=b+mew*(target-output)*1
    output=out(x,w,b)
    print(target,output)
#     w1[itr]=w
# print(w1)

#Feed Forward
sum=0
itr=-1
oty=[]
for y in range(0,len(xt)):
    x=xt[y]
    itr=itr+1
    target=tt[y]
    output=out(x,w,b)
    oty.append(output)
plt.plot(xt,oty)
plt.show()
g=[]
g=[int(x) for x in bin(8)[2:]]
