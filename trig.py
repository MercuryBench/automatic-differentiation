from math import *
def sine(x):
	if x >= 0:
		n = x // (2 * pi)
		x = x - n*2*pi
	else:
		n = -x // (2 * pi)
		x = x + n*2*pi
		x = 2*pi + x
	if x <= pi/2:
		return sine_constr(x)
	elif x <= pi:
		return sine_constr(pi-x)
	elif x <= 3*pi/2:
		return -sine_constr(x - pi)
	else:
		return -sine_constr(2*pi-x)

def cosine(x):
	if x >= 0:
		n = x // (2 * pi)
		x = x - n*2*pi
	else:
		n = -x // (2 * pi)
		x = x + n*2*pi
		x = 2*pi + x
	if x <= pi/2:
		return cosine_constr(x)
	elif x <= pi:
		return -cosine_constr(pi-x)
	elif x <= 3*pi/2:
		return -cosine_constr(x - pi)
	else:
		return cosine_constr(2*pi-x)
		
def sine_constr(x):
	return x - x*x*x/(3.0*2) + x*x*x*x*x/(5.0*4*3*2) - x*x*x*x*x*x*x/(7.0*6*5*4*3*2)
	
def cosine_constr(x):
	return 1.0 - x*x/2.0 + x*x*x*x/(4.0*3*2) - x*x*x*x*x*x/(6.0*5*4*3*2)
