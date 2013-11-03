#Sparkery
#August 30, 2013
#2D Curvature

from math import pi

angles = list(map(float, open("creation_angles.txt", "r").read().split()))

ref = angles[0]
avg = []

for X in range(1, len(angles)):
    avg.append((ref - angles[X]) / (X))

print(sum(avg)/len(avg))
print((sum(avg)/len(avg) - 1.0/40.0) / (1.0/40.0))
