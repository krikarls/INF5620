from numpy import *
from mesh_function import *

def f(t):
	if t >= 0 and t <= 3:
		f=exp(-t)
	elif t > 3 and t <= 4:
		f=exp(-3*t)
	else:
		print "not in the valid interval"
	return f

dt = 0.1
n = int(4/dt)
t = linspace(0,4,n)

f_values, t = mesh_function(f(t),t)

print f_values
print t


"""
f_values = zeros(len(t))

for i in range(len(t)):
	f_values[i]=f(t[i])

print f_values
print t
"""






