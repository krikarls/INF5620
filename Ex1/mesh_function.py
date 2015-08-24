from numpy import *

def mesh_function(f,t):
#  t er en array med alle t-verdier
#  f er en vilkArlig matematisk funksjon f(t)

	f_values=zeros(len(t))

	for i in range(len(t)):
		f_values[i]=f(t[i])

	return f, t