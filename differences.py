#Sparkery
#August 19, 2013
#Another Approach: Finite Differences

#angles = list(map(float, open("creation_angles.txt", "r").read().split()))
angles = [1, 4, 9, 16, 25, 36, 49]

while len(angles) > 1:
    new = []
    print(angles)
    for A in range(len(angles) - 1):
        new.append(angles[A + 1] - angles[A])
    angles = new

print(angles)
