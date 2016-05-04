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
	length=(length-(length%F))/F
	length=length-2

	print "length is ",length
	
	sample=sample+length
	video=np.zeros((length,F*5,240,320),dtype=np.uint8)

	ret,img = cap.read()
	#img=cv2.resize(img,(320,240))
	pre_frames=img
	for i in range(length):
		m=0
		for s in range(F):
			ret,img = cap.read()
			#img=cv2.resize(img,(240,240))

			diff_frames=img-pre_frames

			pre_frames=img
	cap.release()
	return video

#main function start here
if __name__ == '__main__':
	N=993
	F=2
	sample=0
#N=350
	n=0
	a=range(sample)
	random.shuffle(a)
	y = []
	full_path=[]
	cou=0
	text_file=open("Ac_train_name.txt")
	line=text_file.readlines()
	for i in line:
		path=i.rsplit(' ',1)[0]
		full_path.append(path)
		#print path
		label=i.rsplit(' ',1)[1]
		y.append(label)
		#print label
		cou=cou+1
	text_file.close()
	print cou




	for i in range(N):
		video_path=full_path[i]#get videos' full path
		print "in video:",i
		read_avi(video_path)
		print sample


