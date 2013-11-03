#Sparkery
#August 12, 2013
#Angle Experiment

from time import time
from math import sqrt, pi

#a1 = open("circle_angles.txt", "r").read().split()
#b1 = open("cat_angles.txt", "r").read().split()

a = list(map(float, open("circle_angles.txt", "r").read().split()))
b = list(map(float, open("circle_angles.txt", "r").read().split()))

b[-1] += 10 #change in w dw for fun

#for A in a1:
#    a.append(float(A))
#for B in b1:
#    b.append(float(B))

def scale(array1, array2):
    if len(array1) > len(array2):
        scalar = int(len(array1) / len(array2) + 0.5)
        new = []
        for A in range(0, len(array1), scalar):
            new.append(array1[A])
        return new, array2
    
    elif len(array1) < len(array2):
        scalar = int(len(array2) / len(array1) + 0.5)
        new = []
        for A in range(0, len(array2), scalar):
            new.append(array2[A])
        return a, new
    
    return array1, array2

def delimeter(ref):
    return sqrt(ref) + 1

def randoo(array):
    error = 0
    s = sum(array)
    for Q in range(len(n)):
        error += len(array) * Q - s
    return error / len(array)

start = time()
best = 9999999999999

print(len(a), len(b))

for X in range(0, 360):
    for Y in range(len(a)):
        a[Y] += pi * (X / 360.0)
        a[Y] %= pi
    m, n = scale(a, b)

    stuff = randoo(n)
    theoretical = randoo(m)

    paces = abs(stuff - theoretical)
    #print(str(paces) + " paces.")

    if paces <= delimeter(max(len(m), len(n))):
        print("Yes.")
        break
    else:
        pass

    best = min(paces, best)
    print(str(paces))

print(str(abs(paces - delimeter(len(m)))) + " paces away from threshold.")
print(str(best))

print(str(time() - start) + " seconds.")
