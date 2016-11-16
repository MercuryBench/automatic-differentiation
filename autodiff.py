from math import floor, pi

class DualNumber(object):
	def __init__(self, r, e):
		# Initialization of real and infinitesimal parts.
		self.r = r
		self.e = e
	def __repr__(self):
		# How to print dual numbers.
		return str(self.r) + " + " + str(self.e) + " * e"
	def __add__(self, other):
		# Overload the addition operator for addition of dual numbers
		if not isinstance(other, DualNumber):
			new_other = DualNumber(other, 0)
		else:
			new_other = other
		r_part = self.r + new_other.r
		e_part = self.e + new_other.e
		return DualNumber(r_part, e_part)
	def __radd__(self, other):
		return self + other
	def __sub__(self, other):
		# Overload the subtraction operator for addition of dual numbers
		if not isinstance(other, DualNumber):
			new_other = DualNumber(other, 0)
		else:
			new_other = other
		r_part = self.r - new_other.r
		e_part = self.e - new_other.e
		return DualNumber(r_part, e_part)
	def __rsub__(self, other):
		return DualNumber(other, 0) - self
	def __mul__(self, other):
		# Overload the multiplication operator for addition of dual numbers
		if not isinstance(other, DualNumber):
			new_other = DualNumber(other, 0)
		else:
			new_other = other
		r_part = self.r * new_other.r
		e_part = self.r * new_other.e + self.e * new_other.r
		return DualNumber(r_part, e_part)
	def __rmul__(self, other):
		return self * other
	def __div__(self, other):
		# Overload the division operator for addition of dual numbers
		if not isinstance(other, DualNumber):
			new_other = DualNumber(other, 0)
		else:
			new_other = other
		if not new_other.r == 0:
			r_part = self.r / new_other.r
			e_part = (new_other.r*self.e - self.r*new_other.e)/(new_other.r**2)
		elif self.r == 0:
			r_part = self.e / new_other.e
			e_part = 0
		else:
			return None		
		return DualNumber(r_part, e_part)
	def __rdiv__(self, other):
	# Overload the division operator (other direction) for addition of dual numbers
		if not isinstance(other, DualNumber):
			new_other = DualNumber(other, 0)
		else:
			new_other = other
		if not new_other.r == 0:
			r_part = new_other.r / self.r 
			e_part = (new_other.e*self.r - self.e*new_other.r)/(self.r**2)
		elif self.r == 0:
			r_part = new_other.e / self.e
			e_part = 0
		else:
			return None		
		return DualNumber(r_part, e_part)
	def __floordiv__(self, other):
	# Overload the "//" division operator (other direction) for addition of dual numbers
		if not isinstance(other, DualNumber):
			new_other = DualNumber(other, 0)
		else:
			new_other = other
		division = self / other
		return DualNumber(floor(division.r), floor(division.e))
	def __neg__(self):
		return DualNumber(-self.r, -self.e)
	def __eq__(self, other):
		# Overload "==" for dual numbers
		if not isinstance(other, DualNumber):
			new_other = DualNumber(other, 0)
		else:
			new_other = other
		return self.r == new_other.r and self.e == new_other.e
	def __ne__(self, other):
		# Overload !=
		return not self == other
	def __lt__(self, other):
		# Overload "<" for dual numbers
		if not isinstance(other, DualNumber):
			new_other = DualNumber(other, 0)
		else:
			new_other = other
		return self.r < new_other.r
	def __le__(self, other):
		# Overload "<=" for dual numbers
		if not isinstance(other, DualNumber):
			new_other = DualNumber(other, 0)
		else:
			new_other = other
		return self.r <= new_other.r
	def __gt__(self, other):
		return not self <= other
	def __ge__(self, other):
		return not self < other
	
		
def AutomaticDerivative(f):
	# Accepts a function f as an argument and returns a new function that is the derivative of f, calculated using automatic differentiation
	def f_prime(x):
		f_x_plus_eps = f(DualNumber(x, 1))
		deriv = f_x_plus_eps.e
		return deriv
	return f_prime
	
if __name__ == "__main__":
	import numpy as np
	import matplotlib.pyplot as plt
	from trig import *
	f = lambda x: sine(x)
	fp = AutomaticDerivative(f)
	x = np.linspace(0, 2*pi, 500)
	f_vec = np.vectorize(f)
	fp_vec = np.vectorize(fp)
	plt.plot(x, f_vec(x))
	plt.plot(x, fp_vec(x), 'r')
	plt.show()
	d2 = DualNumber(4.0, 2.0)
	d1 = DualNumber(2.0, 1.0)
			
		
