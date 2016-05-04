#!/usr/bin/python
import os
import numpy as np
import cv2
import caffe
import lmdb
import random
def read_avi(avi_path):
	global video
	global F
	global sample
	print avi_path
	cap = cv2.VideoCapture(avi_path)
	length=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
	print length
	if length<54:
		print "length is less than 50" 
		rand_list=range(length)
	else:
		rand_list=random.sample(range(1,length-1),50)
		rand_list.sort()
		length=50

	length=(length-length%F)/F
	
	sample=sample+length

#main function start here
if __name__ == '__main__':
	#N=313
	N=995
	F=2
	sample=0
#N=350
	n=0
	#sample=3130
	y = []
	full_path=[]
	cou=0
	text_file=open("Ac_train_name.txt")
	line=text_file.readlines()
	for i in line:
		path=str(i.rsplit(' ',1)[0])
		full_path.append(path)
		#print path
		label=int(i.rsplit(' ',1)[1])
		y.append(label)
		#print label
		cou=cou+1
	text_file.close()
	print cou

	for i in range(N):
		video_path=full_path[i]#get videos' full path
		#print full_path[i]
		read_avi(video_path)
		print sample
