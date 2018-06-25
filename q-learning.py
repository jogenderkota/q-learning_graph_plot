import sys
import time
import numpy as np
import matplotlib.pyplot as plt

xt=[0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,1,1,1]
tt=[0,0.2,0.25,0.5,0.7,0.75,0.85,0.9]
xt1=[]
for y in range(0,len(xt),3):
    x=xt[y:y+3]
    num = 0
    for b in x:
        num = 2 * num + b
    xt1.append(num)

plt.scatter(xt1,tt,c='red')
plt.grid()
# plt.show()

itr=-1
mew=0.5
w1=np.zeros(shape=(3,9))

def out(x,w):
    s=0
    for i in range(0,3):
        s=s+w[i]*x[i]
    return s

w=[]
for i in range(0,3):
    r=np.random.rand()
    w.append(r)

for y in range(0,len(xt),3):
    x=xt[y:y+3]
    itr=itr+1
    target=tt[itr]
    inlen=len(x)

    for i in range(0,99):
        output=out(x,w)
        # update weights
        for j in range(0,3):
            w[j]=w[j]+mew*(target-output)*x[j]
    print(target,output)
#     w1[itr]=w
# print(w1)

#Feed Forward
sum=0
x=[0,1,0]
for i in range(0,3):
    s=sum+w[i]*x[i]
print(s)
itr=-1
oty=[]
for y in range(0,len(xt),3):
    x=xt[y:y+3]
    itr=itr+1
    target=tt[itr]
    output=out(x,w)
    oty.append(output)
plt.plot(xt1,oty)
plt.show()
g=[]
g=[int(x) for x in bin(8)[2:]]
