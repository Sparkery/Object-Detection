from math import exp
from time import time
from random import random

epoch = 25000

def calculate(x, y):
        return 1 / (1 + exp(-1 * (w6 + w7*(1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))) + w8*(1 / (1 + exp(-1 * (w3 + w4*x + w5*y)))))))

def sigmoid(w, x, z):
        y = w + w1*x + w2*z
        if y > 500:
           return 1
        if y < -500:
                return 0
        sig = 1 / (1 + exp(-y))
        return sig

w0 = -4
w1 = 12
w2 = 8
w3 = -12
w4 = 12
w5 = 8
w6 = -12
w7 = 8
w8 = -4   #randoo

test = [(0, 0, 0), (1, 0, 1), (0, 1, 1), (1, 1, 0)]
#for (x, z, p) in test:
#       print((x, z, p), sigmoid(w0, x, z))

start = time()

#print()
for A in range(epoch):
        error = 0
        for (x, y, p) in test:
                a = -1 * (w0 + w1*x + w2*y)
                if a > 255:
                     h1 = 1
                elif a < -255:
                     h1 = 0
                else:
                     h1 = 1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))
                b = -1 * (w3 + w4*x + w5*y)
                if b > 255:
                     h2 = 1
                elif b < -255:
                     h2 = 0
                else:
                     h2 = 1 / (1 + exp(-1 * (w3 + w4*x + w5*y)))
                z = 1 / (1 + exp(-1 * (w6 + w7*h1 + w8*h2)))
                error += 0.5*(z - p)**2
        #print(error)
        for(x, y, p) in test:
                z =  calculate(x, y)
                error += 0.5 * (z - p)**2
                h1 = 1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))
                h2 = 1 / (1 + exp(-1 * (w3 + w4*x + w5*y)))
                w0 -= (z - p) * z * (1 - z)
                w1 -= (z - p) * z * (1 - z) * x
                w2 -= (z - p) * z * (1 - z) * y
                w3 -= (z - p) * z * (1 - z)
                w4 -= (z - p) * z * (1 - z) * x
                w5 -= (z - p) * z * (1 - z) * y
                w6 -= (z - p) * z * (1 - z)
                w7 -= (z - p) * z * (1 - z) * h1
                w8 -= (z - p) * z * (1 - z) * h2
error = 0
for (x, y, p) in test:
                h1 = 1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))
                h2 = 1 / (1 + exp(-1 * (w3 + w4*x + w5*y)))
                z = 1 / (1 + exp(-1 * (w6 + w7*h1 + w8*h2)))
                error += 0.5*(z - p)**2
print(time() - start)
print(w0, w1, w2, w3, w4, w5, w6, w7, w8)
print(error, h1, h2)
print(calculate(0, 0), calculate(0, 1), calculate(1, 0), calculate(1, 1))
