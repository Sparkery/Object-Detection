from math import exp
from time import time
from random import random

epoch = 100000


def calculate(x, y):
        return 1 / (1 + exp(-1 * (w6 + w7*(1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))) + w8*(1 / (1 + exp(-1 * (w3 + w4*x + w5*y)))))))

def sigmoid(w, x, z):
	y = w + w1*x + w2*z
	sig = 1 / (1 + exp(-y))
	return sig

w0 = -4
w1 = 12
w2 = 8
w3 = -12
w4 = 12
w5 = 8
w6 = -12
w7 = 8
w8 = -4   #randoo

test = [(0, 0, 0), (1, 0, 1), (0, 1, 1), (1, 1, 0)]
#test = [(0, 0, 1), (1, 0, 0), (0, 1, 0), (1, 1, 1)]

#for (x, z, p) in test:
#	print((x, z, p), sigmoid(w0, x, z))

#print()

start = time()
for A in range(epoch):
	error = 0
	for (x, y, p) in test:
		h1 = 1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))
		h2 = 1 / (1 + exp(-1 * (w3 + w4*x + w5*y)))
		z = 1 / (1 + exp(-1 * (w6 + w7*(1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))) + w8*(1 / (1 + exp(-1 * (w3 + w4*x + w5*y)))))))
		error += 0.5 * (z - p)**2
	#print(error)
	dw = 0.001
	error0 = 0
	error1 = 0
	error2 = 0
	error3 = 0
	error4 = 0
	error5 = 0
	error6 = 0
	error7 = 0
	error8 = 0
	for(x, y, p) in test:
		error0 += 0.5 * ( 1 / (1 + exp(-1 * (w6 + w7*(1 / (1 + exp(-1 * ((w0 + dw) + w1*x + w2*y)))) + w8*(1 / (1 + exp(-1 * (w3 + w4*x + w5*y))))))) - p )**2
		error1 += 0.5 * ( 1 / (1 + exp(-1 * (w6 + w7*(1 / (1 + exp(-1 * (w0 + w1*(x + dw) + w2*y)))) + w8*(1 / (1 + exp(-1 * (w3 + w4*x + w5*y))))))) - p )**2
		error2 += 0.5 * ( 1 / (1 + exp(-1 * (w6 + w7*(1 / (1 + exp(-1 * (w0 + w1*x + w2*(y + dw))))) + w8*(1 / (1 + exp(-1 * (w3 + w4*x + w5*y))))))) - p )**2
		error3 += 0.5 * ( 1 / (1 + exp(-1 * (w6 + w7*(1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))) + w8*(1 / (1 + exp(-1 * ((w3 + dw) + w4*x + w5*y))))))) - p )**2
		error4 += 0.5 * ( 1 / (1 + exp(-1 * (w6 + w7*(1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))) + w8*(1 / (1 + exp(-1 * (w3 + w4*(x + dw) + w5*y))))))) - p )**2
		error5 += 0.5 * ( 1 / (1 + exp(-1 * (w6 + w7*(1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))) + w8*(1 / (1 + exp(-1 * (w3 + w4*x + w5*(y + dw)))))))) - p )**2
		error6 += 0.5 * ( 1 / (1 + exp(-1 * ((w6 + dw) + w7*(1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))) + w8*(1 / (1 + exp(-1 * (w3 + w4*x + w5*y))))))) - p )**2
		error7 += 0.5 * ( 1 / (1 + exp(-1 * (w6 + w7*((1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))) + dw) + w8*(1 / (1 + exp(-1 * (w3 + w4*x + w5*y))))))) - p )**2
		error8 += 0.5 * ( 1 / (1 + exp(-1 * (w6 + w7*(1 / (1 + exp(-1 * (w0 + w1*x + w2*y)))) + w8*((1 / (1 + exp(-1 * (w3 + w4*x + w5*y)))) + dw)))) - p )**2

	w0 += 0.8 * (error - error0)
	w1 += 0.8 * (error - error1)
	w2 += 0.8 * (error - error2)
	w3 += 0.8 * (error - error3)
	w4 += 0.8 * (error - error4)
	w5 += 0.8 * (error - error5)
	w6 += 0.8 * (error - error6)
	w7 += 0.8 * (error - error7)
	w8 += 0.8 * (error - error8)

print(time() - start)
print(error, h1, h2)
print(w0, w1, w2, w3, w4, w5, w6, w7, w8)
print(calculate(0, 0), calculate(0, 1), calculate(1, 0), calculate(1, 1))
