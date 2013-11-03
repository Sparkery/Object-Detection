#Sparkery
#August 16, 2013
#Conglomeration

#Works with similar shapes, with a confidence rating over 99%
#Is able to detect shapes from objects (circle from a cat at 78% confidence)

#Needed to adjust error calculation

#Detects dilations!!!

'''Is 10000 paces a good threshold???'''
'''Scaled size ^2 / 2 = paces???'''
'''Scaling the randoo makes 10 paces a good threshold???'''

'''Quadratic running time!!! Might be able to make it n log n using a heap???'''
'''Does not work of object is too small!!!'''

'''Stuff a machine with a bunch of pictures of basic objects. If a given
picture is under the threshold of any of the rudimetanry pictures, a suggestion
is given. If said picture is over the threshold, it is discarded from future
diagnosis. This will be needing quite a lot of pictures, but so does the human
mind; we all have some steriotypical image of everything to reference upon.'''

'''Needed more test data. Only have circle, different sized circles, and a
cat. Maybe needed dog, horse, triangle, square, trapezoid, etc. Needed moar
moar moar moar moar MOAR test data.'''

'''Moar'''

#
#
#Input
#
#

images = ["creation_r", "cat"]

print("Input done.")
#
#
#Functions
#
#

from sys import argv
from math import atan2, sin, cos, pi, sqrt, log
from time import time
from copy import copy, deepcopy

def index(row, col) :
    return rows * col + row

def angle(gy, gx):
    return atan2(gy, gx)

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

    return float(a + b + c)

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
            
    return float(count)


def delimeter(a, b):
    return log(b) / (log(a) / a)

print("Functions done.")
#
#
#Edge Detection
#
#

start = time()

for QQ in images:
    data = open(QQ + "_angles.txt" , "w")
    image = open(QQ + ".ppm").read().split()

    rows = int(image[1])
    cols = int(image[2])
    rgb = list(map(int, image[4:]))
    pixel = []
    votes = []

    array = []

    for X in range(0, len(rgb), 3):
            temp = int(0.299 * rgb[X] + 0.587 * rgb[X + 1] + 0.114 * rgb[X + 2])
            array.append(temp)
            
    array2 = []
    for Y in range(cols):
            for X in range(rows):
                    if X == 0 or X == rows - 1 or Y == 0 or Y == cols - 1:
                            array2.append(array[index(X, Y)])
                            continue

                    tl = array[index(X - 1, Y - 1)] * 1
                    tc = array[index(X - 1, Y)] * 2
                    tr = array[index(X - 1, Y + 1)] * 1
                    cl = array[index(X, Y - 1)] * 2
                    cc = array[index(X, Y)] * 4
                    cr = array[index(X, Y + 1)] * 2
                    bl = array[index(X + 1, Y - 1)] * 1
                    bc = array[index(X + 1, Y)] * 2
                    br = array[index(X + 1, Y + 1)] * 1
                    val = int((tl + tc + tr + cl + cc + cr + bl + bc + br) / 16.0)
                    
                    array2.append(val)

    gx = 0
    gy = 0
    grr = []
    gxl = []
    gyl = []

    array3 = []

    for Y in range(cols):
            for X in range(rows):
                    array3.append(0)
                    if X == 0 or X == rows - 1 or Y == 0 or Y == cols - 1:
                            gxl.append(0)
                            gyl.append(0)
                            grr.append(array[index(X, Y)])
                    else:

                            tl1 = array2[index(X - 1, Y - 1)] * -1
                            tl2 = array2[index(X - 1, Y - 1)] * 1

                            tc2 = array2[index(X - 1, Y)] * 2

                            tr1 = array2[index(X - 1, Y + 1)] * 1
                            tr2 = array2[index(X - 1, Y + 1)] * 1

                            cl1 = array2[index(X, Y - 1)] * -2

                            cr1 = array2[index(X, Y + 1)] * 2

                            bl1 = array2[index(X + 1, Y - 1)] * -1
                            bl2 = array2[index(X + 1, Y - 1)] * -1

                            bc2 = array2[index(X + 1, Y)] * -2

                            br1 = array2[index(X + 1, Y + 1)] * 1
                            br2 = array2[index(X + 1, Y + 1)] * -1

                            gx = int(tl1 + tr1 + cl1 + cr1 + bl1 + br1)
                            gy = int(tl2 + tc2 + tr2 + bl2 + bc2 + br2)
                            gxl.append(gx)
                            gyl.append(gy)
                            val = abs(gx) + abs(gy)
                            grr.append(val)

    m = float(max(grr))
    for X in range(len(grr)):
            grr[X] = grr[X] / m

    print("Edges done.")
#
#
#Angle Calculation
#
#
    dictionary = {}
    for Y in range(cols):
        for X in range(rows):
            if X == 0 or X == rows - 1 or Y == 0 or Y == cols - 1:
                array3[index(X, Y)] = 255
                continue
            if grr[index(X, Y)] > 0.2:
                theta = angle(gyl[index(X, Y)], gxl[index(X, Y)]) + 0.5 * pi
                data.write(str(theta) + "\n")
    data.close()

print("Angles done.")
#
#
#Angle Comparison
#
#

a = list(map(float, open(images[0] + "_angles.txt", "r").read().split()))
b = list(map(float, open(images[1] + "_angles.txt", "r").read().split()))
print(len(a), len(b))

paces = abs(inversions(a) / len(a) - inversions(b) / len(b))
print(paces)

if paces <= delimeter(len(a), len(b)):
    print("Yes.")
else:
    print("No.")

end = time()

print("Calculations done.")

#
#
#Diagnosis
#
#
    
print("\n" + str(end - start) + " elapsed seconds.")
