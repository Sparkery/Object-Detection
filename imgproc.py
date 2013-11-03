#Sparkery
#August 2, 2013
#Border Detection

from sys import argv
from math import atan2, sin, cos
import time

def index(row, col) :
	return rows * col + row
    
#pic = input("")
out = open("test_circle.ppm", "w")

image = open("circle.ppm", "r").read().split()

#
#Timer start
#
start = time.time()
#
#Timer end
#

rows = int(image[1])
cols = int(image[2])
rgb = list(map(int, image[4:]))

out.write("P3\n")
out.write(str(rows) + "\n")
out.write(str(cols) + "\n")
out.write("255\n")

array = []

for X in range(0, len(rgb), 3):
	temp = int(0.299 * rgb[X] + 0.587 * rgb[X + 1] + 0.114 * rgb[X + 2])
	array.append(temp)
	#print(temp, temp, temp)

array2 = []
for Y in range(cols):
	for X in range(rows):
		if X == 0 or X == rows - 1 or Y == 0 or Y == cols - 1:
			#print(array[index(X, Y)], array[index(X,Y)], array[index(X,Y)])
			array2.append(array[index(X, Y)])
			continue
		#val = int((4*(array[index(X,Y)])+2*(array[index(X+1,Y)]+array[index(X-1,Y)]+array[index(X,Y+1)]+array[index(X,Y-1)])+ (array[index(X-1, Y-1)]+array[index(X-1, Y+1)] + array[index(X+1, Y-1)] + array[index(X+1,Y +1)]))/16)

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
		
		#print(val, val, val)
		array2.append(val)

gx = 0
gy = 0
grr = []

for Y in range(cols):
	for X in range(rows):
		if X == 0 or X == rows - 1 or Y == 0 or Y == cols - 1:
			#print(array2[index(X, Y)], array2[index(X,Y)], array2[index(X,Y)])
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
			val = abs(gx) + abs(gy)
#print(array2[index(X, Y)], array2[index(X,Y)], array2[index(X,Y)])
			grr.append(val)

m = float(max(grr))
for X in range(len(grr)):
	grr[X] = grr[X] / m

for X in range(len(grr)):
	if grr[X] > 0.20:
		out.write("0 0 0\n")
	else:
		#print(rgb[X * 3], rgb[X * 3 + 1], rgb[X * 3 + 2]
		out.write("255 255 255\n")

out.close()

print(time.time() - start)
