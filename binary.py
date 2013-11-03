from math   import exp
from random import random
#

def sig(x,w):
	#
	y = 0.0
	#
	x = [1.0] + x # add in the bias term
	#
	j = 0
	#
	while j < len(w):
		#
		y += ( w[j] * x[j] ) # weighted sum
		#
		j += 1
		#
	#
	if y >  100.0: return 1.0
	#
	if y < -100.0: return 0.0
	#
	return 1.0 / ( 1.0 + exp( -y ) )
	#
#
def myrand():
	#
	mymin = -1.0
	mymax =  1.0
	#
	return mymin + (mymax - mymin) * random()
	#
#
#
#
x   = [0,0,0,0,0,0,0,0]    # input layer
test = [[1,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0], [0,0,1,0,0,0,0,0], [0,0,0,1,0,0,0,0], [0,0,0,0,1,0,0,0], [0,0,0,0,0,1,0,0], [0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,1]]
#
wh1 = [0,0,0,0,0,0,0,0,0]  # weights to the hidden layer
wh2 = [0,0,0,0,0,0,0,0,0]
wh3 = [0,0,0,0,0,0,0,0,0]
for X in range(9):
	wh1[X] = -1 + 2 * random()
	wh2[X] = -1 + 2 * random()
	wh3[X] = -1 + 2 * random()
#
wz0 = [0,0,0,0]            # weights to the output layer
wz1 = [0,0,0,0]
wz2 = [0,0,0,0]
wz3 = [0,0,0,0]
wz4 = [0,0,0,0]
wz5 = [0,0,0,0]
wz6 = [0,0,0,0]
wz7 = [0,0,0,0]
#
for X in range(4):
	wz0[X] = -1 + 2 * random()
	wz1[X] = -1 + 2 * random()
	wz2[X] = -1 + 2 * random()
	wz3[X] = -1 + 2 * random()
	wz4[X] = -1 + 2 * random()
	wz5[X] = -1 + 2 * random()
	wz6[X] = -1 + 2 * random()
	wz7[X] = -1 + 2 * random()
#
z   = [0,0,0,0,0,0,0,0]    # output layer
#
#
#
epoch = 1
#
while epoch <= 10000: # ten thousand
	#
	err = 0.0
	#
	pos = 0        # place a single 1 in the input x
	#
	while pos < 8: # eight slots == entire test data
		#
		x[pos] = 1
		#
		# calculate hidden neurons
		#
		h1 = sig( x , wh1 )
		h2 = sig( x , wh2 )
		h3 = sig( x , wh3 )
		#
		# calculate output neurons
		#
		z[0] = sig( [h1,h2,h3] , wz0 )
		z[1] = sig( [h1,h2,h3] , wz1 )
		z[2] = sig( [h1,h2,h3] , wz2 )
		z[3] = sig( [h1,h2,h3] , wz3 )
		z[4] = sig( [h1,h2,h3] , wz4 )
		z[5] = sig( [h1,h2,h3] , wz5 )
		z[6] = sig( [h1,h2,h3] , wz6 )
		z[7] = sig( [h1,h2,h3] , wz7 )
		#
		for X in range(8):
			err += 0.5 * (z[pos] - x[pos]) ** 2
		#
		#
		#
		x[pos] = 0 # important!
		#
		pos += 1
		#
	#
	print(err)
	#
	#
	for X in range(4):
		wz0[X] += err
		wz1[X] += err
		wz2[X] += err
		wz3[X] += err
		wz4[X] += err
		wz5[X] += err
		wz6[X] += err
		wz7[X] += err

	for X in range(8):
		wh1[X] += err
		wh2[X] += err
		wh3[X] += err
	#
	#
	epoch += 1
	#
#print(wh1)
#print(wh2)
#print(wh3)

#
# end of file
#

