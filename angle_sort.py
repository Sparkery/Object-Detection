f = list(map(float, open("creation_r_angles.txt", "r").read().split()))
g = list(map(float, open("creation_r1_angles.txt", "r").read().split()))

dictionary = {}

for X in f:
    if X not in dictionary.keys():
        dictionary[X] = 1
    else:
        dictionary[X] += 1

for X in dictionary.keys():
    print(str(X) + " " + str(dictionary[X]))

print("\n")
dictionary = {}

for X in g:
    if X not in dictionary.keys():
        dictionary[X] = 1
    else:
        dictionary[X] += 1

for X in dictionary.keys():
    print(str(X) + " " + str(dictionary[X]))
