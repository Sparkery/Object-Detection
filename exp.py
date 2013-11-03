#Sparkery
#August 7, 2013
#Neural Network

from math import exp
from time import time
from random import random

#Example using the XOR gate (loops)


epoch = 10000


def calculate(x, y):
        return 1 / (1 + exp(-1 * (w6 + w7*(1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))) + w8*(1 / (1 + exp(-1 * (w3 + w4*x + w5*y)))))))

def sigmoid(m, w):
    y = w[0]
    for Q in range(1, len(w)):
        y += m[Q - 1] * w[Q]

    return 1 / (1 + exp(-y))
        
w = [0, 0, 0, 0, 0, 0, 0, 0, 0]
w[0] = -4
w[1] = 12
w[2] = 8
w[3] = -12
w[4] = 12
w[5] = 8
w[6] = -12
w[7] = 8
w[8] = -4   #randoo

test = [(0, 0, 0), (1, 0, 1), (0, 1, 1), (1, 1, 0)]
#test = [(0, 0, 1), (1, 0, 0), (0, 1, 0), (1, 1, 1)]

#for (x, z, p) in test:
#   print((x, z, p), sigmoid(w0, x, z))

wh1 = [0, 0, 0]
wh2 = [0, 0, 0]
experror = [0, 0, 0, 0, 0, 0, 0, 0]

#print()
h1 = 0
h2 = 0
start = time()
for A in range(epoch):
    error = 0
    for (x, y, p) in test:
        temp1 = [w[0], w[1], w[2]]
        temp2 = [w[3], w[4], w[5]]
        temp3 = [w[6], w[7], w[8]]
        h1 = sigmoid([x, y], temp1)
        h2 = sigmoid([x, y], temp2)
        for B in range(len(wh1)):
            hold1 = temp1
            hold1[B] += 0.001
            hold2 = temp2
            hold2[B] += 0.001
            wh1[B] = sigmoid([x, y], hold1)
            wh2[B] = sigmoid([x, y], hold2)

            experror = [0, 0, 0, 0, 0, 0, 0, 0]
            for C in range(len(wh1)):
                experror[C] = 0.5 * (sigmoid([wh1[C], h2], temp3) - p) **2
            for C in range(len(wh2)):
                experror[C + len(wh1)] = 0.5 * (sigmoid([h1, wh2[C]], temp3) - p) **2
            for C in range(len(wh1) + len(wh2), len(experror) - len(wh1) - len(wh2)):
                hold3 = temp3
                hold3[C] += 0.001
                experror[C] = 0.5 * (sigmoid([h1, h2], hold3) - p) **2
                #error += 0.5 * (sigmoid([h1, h2], [temp3]) - p) **2

    for P in range(len(experror)):
        w[P] += 0.8 * (error - P)

                

print(time() - start)
for (x, y, p) in test:
    h1 = sigmoid([x, y], [w[0], w[1], w[2]])
    h2 = sigmoid([x, y], [w[3], w[4], w[5]])
    print(sigmoid([h1, h2], [w[6], w[7], w[8]]))
