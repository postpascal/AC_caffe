#!/usr/bin/python

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import logistic

def extract_training(filename,star):
	s=0
	a=[]

	file=open(filename,'r')
	x=1
	y=0
	i=0
	for line in file:
		i=i+1
		if s<star:
			s=s+1
		else:
			if y<42:
				if x>2:
					path=line.rsplit(' ',1)[0]
					label=line.rsplit(' ',1)[1]
					label=float(label)
					#print label
					a.append(label)
					#print "y is:",y
					y=y+1
					x=0	
				else:
					x=x+1
					y=y+1

			else:
				y=0
				x=1
	return a
def extract_test(filename,star):
	s=0
	a=[]

	file=open(filename,'r')
	x=43
	i=0
	for line in file:
		i=i+1
		if s<star:
			s=s+1
		else:
				if x>41:
					path=line.rsplit(' ',1)[0]
					label=line.rsplit(' ',1)[1]
					label=float(label)
					print label

					a.append(label)
					#print "y is:",y
					x=0

				else:
					x=x+1
	return a

			
def pl(m):
	b=[]
	q=0
	for f in m:
		q=q+20
		b.append(q)
	b=np.array(b)
	return b



if __name__ == '__main__':  
	
	a=extract("RGB_op_3.txt",1166)
	a=np.array(a)

	b=extract("out_RGB_diff_2.txt",1166)
	b=np.array(b)

	c=extract("RGB_3_diff.txt",1166)
	c=np.array(c)

	plt.figure(1)
	plt.axis([0,4000,0,1])
	plt.axhline(y=0, color='k')
	plt.axvline(x=0, color='k')
	#plt.title('Sigmoid')
	plt.plot(pl(a),a,'r-',pl(b),b,'b-')

	plt.figure(2)
	plt.axis([0,4000,0,1])
	plt.axhline(y=0, color='k')
	plt.axvline(x=0, color='k')
	#plt.title('Sigmoid')
	plt.plot(pl(c),c,'g-',pl(b),b,'b-')

	
	plt.show()
