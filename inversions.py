#Yavor Ilija
#July 28, 2013
#Counting Inversions

from time import time
from math import pi
from copy import copy

def scale(array1, array2):
    if len(array1) > len(array2):
        scalar = len(array1) / float(len(array2))
        new = []
        for A in range(0, len(array2)):
            new.append(array1[int(A * scalar)])
        return new, array2
    elif len(array1) < len(array2):
        scalar = len(array2) / float(len(array1))
        new = []
        for A in range(0, len(array1)):
            new.append(array2[int(A * scalar)])
        return array1, new
    return array1, array2

def inversions(array):
    if len(array) <= 1:
        return 0
    middle = int(len(array) / 2)
    left = array[:middle]
    right = array[middle:]
    
    a = inversions(left)
    b = inversions(right)
    c = split(left, right)

    return a + b + c

def split(left, right):
    count = 0
    i, j = 0, 0
    lleft = len(left)
    lright = len(right)
    while i < lleft and j < lright:
        if left[i] <= right[j]:
            i += 1
        else:
            count += lleft - i
            j += 1
            
    return count

array = list(map(float, open("circle_angles.txt", "r").read().split()))
array1 = list(map(float, open("creation_angles.txt", "r").read().split()))

for X in range(-719, 720):
    temp = copy(array)
    for Y in temp:
        Y += (X / 360.0)
        Y %= (2*pi)
    m, n = scale(temp, array1)
    print(abs(inversions(temp) / float(len(temp)) - inversions(array1) / float(len(array1))))
