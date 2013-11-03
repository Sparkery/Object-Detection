def index(row, col) :
        return rows * col + row

radius1 = 50
radius2 = 100

border = 300

out = open("creation_r1.ppm", "w")

out.write("P3\n")
out.write("300\n")
out.write("300\n")
out.write("255\n")

for Y in range(border):
        for X in range(border):
                if X == 0 or X == border - 1 or Y == 0 or Y == border - 1:
                        out.write("255 255 255\n")
                else:
                        if abs(X - 149) < radius1 and abs(Y - 149) < radius2:
                                out.write("0 0 0\n")
                        #if X - radius < 149 and Y - radius < 149:
                        #        out.write("0 0 0\n")
                        #elif X + radius > 149 and Y + radius > 149:
                        #        out.write("0 0 0\n")
                        else:
                                out.write("255 255 255\n")


out.close()

