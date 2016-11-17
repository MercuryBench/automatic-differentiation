from math import *
import numpy as np 
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

def expo(x):
	"""floorx = x // 1
	restx = x - floorx
	fstterm = 1 + restx*(1 + restx/2*(1 + restx/3*(1 + restx/4*(1 + restx/5*(1 + restx/6*(1 + restx/7*(1 + restx/8*(1 + restx/9*(1 + restx/10)))))))))
	sndterm = e**floorx
	return fstterm*sndterm"""
	t = 1.0
	for k in np.arange(70.0, -1, -1):
		t = exp_aux(t, x, k)
	return t
		
def exp_aux(t, x, n):
	if n <= 0:
		return t
	else:
		return (t*x/n+1)
def sine_constr(x):
	return x - x*x*x/(3.0*2) + x*x*x*x*x/(5.0*4*3*2) - x*x*x*x*x*x*x/(7.0*6*5*4*3*2)
	
def cosine_constr(x):
	return 1.0 - x*x/2.0 + x*x*x*x/(4.0*3*2) - x*x*x*x*x*x/(6.0*5*4*3*2)
