#!/usr/bin/python

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import logistic

def extract_training(filename,star):
	s=0
	a=[]

	file=open(filename,'r')
	x=0
	y=-1
	i=0
	for line in file:
		i=i+1
		if s<star:
			s=s+1
		else:
			if y<42:
				if x>2:
					#path=line.rsplit(' ',3)[0]
					q1=line.rsplit(' ',1)[0]
					q2=q1.rsplit(' ',1)[1]
					label=float(q2)
					#print q2
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
				#path=line.rsplit(' ',3)[0]
				q1=line.rsplit(' ',1)[0]
				#print q1
				q2=q1.rsplit(' ',1)[1]
				label=float(q2)
				#print q2
				a.append(label)
				#print "y is:",y
				
				x=0	
			else:
				x=x+1

	return a
			
def pl_tr(m):
	b=[]
	q=0
	for f in m:
		q=q+20
		b.append(q)
	b=np.array(b)
	return b

def pl_te(m):
	b=[]
	q=0
	for f in m:
		q=q+200
		b.append(q)
	b=np.array(b)
	return b


if __name__ == '__main__':  
	
	a=extract_test("RGB_3_diff.txt",1166)
	a=np.array(a)

	b=extract_test("RGB_op_3.txt",1166)
	b=np.array(b)

	plt.figure(1)
	plt.axis([0,4000,0,2.5])
	plt.axhline(y=0, color='k')
	plt.axvline(x=0, color='k')
	#plt.title('Sigmoid')
	plt.plot(pl_te(a),a,'r-',pl_te(b),b,'b--')
	plt.ylabel("Loss")
	plt.xlabel("Iterations")
	plt.title('RGB-diff vs optical flow')

	plt.annotate('RGB-diff', xy=(500, 1.5), xytext=(250, 0.8),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
	plt.annotate('optical flow', xy=(2500, 1.5), xytext=(2800, 1),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

	
	plt.show()
