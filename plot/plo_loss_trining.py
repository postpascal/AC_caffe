#!/usr/bin/python

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import logistic

def extract(filename,star):
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
					print q2
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

			
def pl(m):
	b=[]
	q=0
	for f in m:
		q=q+20
		b.append(q)
	b=np.array(b)
	return b



if __name__ == '__main__':  
	
	a=extract("RGB_3_diff.txt",1166)
	a=np.array(a)

	b=extract("out_RGB_diff_2.txt",1166)
	b=np.array(b)

	plt.figure(1)
	plt.axis([0,4000,0,2.5])
	plt.axhline(y=0, color='k')
	plt.axvline(x=0, color='k')
	#plt.title('Sigmoid')
	plt.plot(pl(a),a,'r-',pl(b),b,'b--')
	plt.ylabel("Loss")
	plt.xlabel("Iterations")
	plt.title('3frames/sample vs 3frames/sample')
	

	plt.annotate('3frames/sample', xy=(500, 1), xytext=(250, 0.25),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
	plt.annotate('3frames/sample', xy=(3200, 1), xytext=(2000, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

	
	plt.show()
