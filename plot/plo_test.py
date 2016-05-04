#!/usr/bin/python

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import logistic

def extract(filename,star):
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
		q=q+200
		b.append(q)
	b=np.array(b)
	return b



if __name__ == '__main__':  
	
	a=extract("RGB_op_3.txt",1165)
	a=np.array(a)

	b=extract("out_RGB_diff_2.txt",1165)
	b=np.array(b)

	plt.figure(1)
	plt.axis([0,4000,0,1])
	plt.axhline(y=0, color='k')
	plt.axvline(x=0, color='k')
	plt.title('Sigmoid')
	plt.plot(pl(a),a,'r-',pl(b),b,'g-')



	
	plt.show()
