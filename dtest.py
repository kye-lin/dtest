'''Classifies critical points of a function f(x, y) as local maxima, minima, or saddle points.'''

def func(x, y): 
	return x**4 + y**3 - 3*x**2 + y**2 + x - 2*y + 1

def fxx(x, y):
	return 12*x**2 - 6

def fyy(x, y):
	return 6*y + 2

def fxy(x, y):
	return 0

def dtest(x, y):
	return fxx(x, y) * fyy(x, y) - (fxy(x, y)**2)

def display(x, y):
	d_result = dtest(x, y)
	fxx_result = fxx(x, y)
	print('D(' + str(x) + ', ' + str(y) + ') = ' + str(d_result))
	print('fxx(' + str(x) + ', ' + str(y) + ') = ' + str(fxx_result))
	if d_result < 0:
		print('Saddle point')
	elif d_result > 0:
		if fxx_result > 0:
			print('Local min')
		elif fxx_result < 0:
			print('Local max')
	elif d_result == 0:
		print('Inconclusive')

def evaluate(f, x, y):
	'''Returns f(x, y)'''
	return f(x, y)

x1 = 0.170
x2 = 1.131
x3 = -1.301
y1 = 0.549
y2 = -1.215

x_list = [x1, x2, x3]
y_list = [y1, y2]

for x in x_list:
	for y in y_list:
		display(x, y)
		print('f = ' + str(evaluate(func, x, y)))
		print('') # new line