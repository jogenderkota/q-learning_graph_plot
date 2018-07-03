import numpy as np
import matplotlib.pyplot as plt
import sys


def output(x,w):
    s=[]
    for i in range(0,len(x)):
        s.append((w[0]*x[i]**2) + (w[1]*x[i]**20)+(w[2]*1))
    return s

def error(target,prediction):
    err=[]
    for i in range(0,len(target)):
        err.append((target[i]-prediction[i])**2)
    sum_square=sum(err)
    return err,sum_square

x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7]
y=[0.2,0.43,0.61,0.756,0.8,0.84,0.95]
w=[0.1,0.1,0.1]
mew=0.1
plt.ion() # enable interactivity
# fig=plt.figure() # make a figure
for o in range(0,1000):
    predicted=output(x,w)
    # print(predicted)
    # err,sum_square=error(y,predicted)
    # print(err,sum_square)
    plt.figure(1)
    for t in range(0,len(x)):
        w[0]=w[0]+mew*(y[t]-predicted[t])*x[t]
        w[1]=w[1]+mew*(y[t]-predicted[t])*x[t]
        w[2]=w[2]+mew*(y[t]-predicted[t])*1
        # w[3]=w[3]+mew*(y[t]-predicted[t])*x[t]
    predicted=output(x,w)
    # print(predicted)
    err,sum_square=error(y,predicted)
    print(o,sum_square)
    plt.clf()
    plt.scatter(x,y,c='red')
    plt.plot(x,predicted,c='blue')
    plt.draw()
    plt.pause(0.0001)

# plt.figure(2)
# for i in range(100):
#     x = range(i)
#     y = range(i)
#     # plt.gca().cla() # optionally clear axes
#     plt.plot(x, y)
#     plt.title(str(i))
#     plt.draw()

plt.show(block=True) # block=True lets the window stay open at the end of the animation.
