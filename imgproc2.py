#Sparkery
#August 12, 2013
#Image Processing Computer Vision

from sys import argv
from math import atan2, sin, cos, pi
import math

def index(row, col) :
	return rows * col + row

def angle(gy, gx):
	return atan2(gy, gx)

out = open("creation_votes.ppm", "w")
data = open("creation_angles.txt", "w")
image = open("creation.ppm", "r").read().split()

rows = int(image[1])
cols = int(image[2])
rgb = list(map(int, image[4:]))
pixel = []
votes = []
for v in range(len(rgb)):
	votes.append(0)
	pixel.append(255)

out.write("P3\n")
out.write(str(rows) + "\n")
out.write(str(cols) + "\n")
out.write("255\n")

array = []

for X in range(0, len(rgb), 3):
	temp = int(0.299 * rgb[X] + 0.587 * rgb[X + 1] + 0.114 * rgb[X + 2])
	array.append(temp)
	#out.write(temp, temp, temp)

array2 = []
for Y in range(cols):
	for X in range(rows):
		if X == 0 or X == rows - 1 or Y == 0 or Y == cols - 1:
			#out.write(array[index(X, Y)], array[index(X,Y)], array[index(X,Y)])
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
		
		#out.write(val, val, val)
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
			#out.write(array2[index(X, Y)], array2[index(X,Y)], array2[index(X,Y)])
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
#out.write(array2[index(X, Y)], array2[index(X,Y)], array2[index(X,Y)])
			grr.append(val)

m = float(max(grr))
for X in range(len(grr)):
	grr[X] = grr[X] / m
threshold = 0.15
#for X in range(len(grr)):
	#if grr[X] > 0.15:
		#out.write(0, 0, 0)
		
	#else:
		#out.write(rgb[X * 3], rgb[X * 3 + 1], rgb[X * 3 + 2]
		#out.write(255, 255, 255)

dictionary = {}
for Y in range(cols):
	for X in range(rows):
		if X == 0 or X == rows - 1 or Y == 0 or Y == cols - 1:
			array3[index(X, Y)] = 255
			continue
		if grr[index(X, Y)] > 0.2:
			theta = angle(gyl[index(X, Y)], gxl[index(X, Y)])+0.5*math.pi
			data.write(str(theta) + "\n")
			radius = 0
			xLine1 = 0
			yLine1 = 0
			xLine2 = 0
			yLine2 = 0
			while True:
				xLine1 = int(X + cos(theta) * radius)
				yLine1 = int(Y + sin(theta) * radius)
				if xLine1 > rows or xLine1 < 0 or yLine1 > cols or yLine1 < 0:
					break
				t = xLine1, yLine1
				if t in dictionary:
					dictionary[t].append(radius)
				else:
					dictionary[t] = [radius]
				pixel[index(xLine1, yLine1)] -= 5
				votes[index(xLine1, yLine1)] += 1
				radius += 1

			while True:
				xLine2 = int(X - cos(theta) * radius)
				yLine2 = int(Y - sin(theta) * radius)
				if xLine2 < 0 or xLine2 > rows or yLine2 < 0 or yLine2 > cols:
					break
				t = xLine2, yLine2
				if t in dictionary:
					dictionary[t].append(abs(radius))
				else:
					dictionary[t] = [abs(radius)]
				pixel[index(xLine2, yLine2)] -= 5
				votes[index(xLine2, yLine2)] += 1
				radius -= 1

maxi = max(votes)
for X in range(len(votes)):
	if maxi == votes[X]:
		pixel[X] = 255


for Z in pixel:
	if Z<0: Z=0
	out.write(str(Z) + " " + str(Z) + " " + str(Z) + "\n")
data.close()
