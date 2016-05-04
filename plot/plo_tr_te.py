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

	

	a=extract_test("RGB_op2.txt",1166)
	a=np.array(a)

	b=extract_test("RGB_op_3.txt",1165)
	b=np.array(b)

	c=extract_test("RGB_3_diff.txt",1165)
	c=np.array(c)

	d=extract_test("out_RGB_diff_2.txt",1165)
	d=np.array(d)
	

	plt.figure(1)
	plt.axis([0,4000,0,1])
	plt.axhline(y=0, color='k')
	plt.axvline(x=0, color='k')
	plt.ylabel("Accuracy")
	plt.xlabel("Iterations")
	plt.title('Four types of Dataset')
	plt.plot(pl_te(a),a,'r-',pl_te(b),b,'y--',pl_te(c),c,'g--',pl_te(d),d,'b--')
	plt.annotate('RGB+op 2', xy=(1500, 0.33), xytext=(1000, 0.1),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
	plt.annotate('RGB+op 3', xy=(2700, 0.62), xytext=(2700, 0.9),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

	plt.annotate('RGB+diff 3', xy=(600, 0.44), xytext=(300, 0.7),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
	plt.annotate('RGB+diff 2', xy=(3000, 0.57), xytext=(2500, 0.2),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

	plt.show()
