def index(row, col) :
	return rows * col + row

radius = 40

border = 300

out = open("creation.ppm", "w")

out.write("P3\n")
out.write("300\n")
out.write("300\n")
out.write("255\n")

for Y in range(border):
	for X in range(border):
		if X == 0 or X == border - 1 or Y == 0 or Y == border - 1:
			out.write("255 255 255\n")
		else:
			if (X - 149) ** 2 + (Y - 149) ** 2 < radius ** 2:
				out.write("0 0 0\n")
			else:
				out.write("255 255 255\n")


out.close()
