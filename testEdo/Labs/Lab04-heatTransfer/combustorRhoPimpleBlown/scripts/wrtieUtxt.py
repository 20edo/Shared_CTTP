#Import necessary packages
import 	numpy 	as np
from 	math 	import *
import	pandas	as pd

# define the response of a first order lsys
def order1_response(tau,startTime,endTime,time):
	'''This function outputs the response of a unitary gain linear system triggered at time startTime and with a flat and from time endTime on'''
	y = 1.0 - np.exp(- ( time - startTime) / tau)
	# Set to 0 times before startTime
	idxZero	= np.where( time < startTime)	
	for i in idxZero:
		y[i] = 0.0
	# Set to 1 times after endTime
	idxOne = np.where( time > endTime )
	for i in idxOne:
		y[i] = 1.0
	return y

# Create time discetization
time = np.arange(start = 0.0, stop = 2.0, step=1e-3)

Ux_inlet = 10*order1_response(1e-3, 0 , 1e-1, time)

data =np.array([ time , Ux_inlet, np.zeros(np.shape(time)), np.zeros(np.shape(time))])
#np.savetxt('U_inlet.txt', data.transpose())

# Save file
file1 = open('U_inlet.txt','a')
file1.write('( \n')
for t in range(0, np.shape(time)[0]):
	file1.write( '( ' + str(time[t]) + ' ( ' + str(Ux_inlet[t]) + ' 0 0 ) )' + '\n' )

file1.write(')')
file1.close
