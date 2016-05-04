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
#	global sample
	print avi_path
	cap = cv2.VideoCapture(avi_path)
	length=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
	length=(length-length%F)/F
	length=length-2
	video=np.zeros((length,F*6,240,320),dtype=np.uint8)

	ret,img = cap.read()
	#img=cv2.resize(img,(320,240))
	pre_frames=img
	for i in range(length):
		m=0
		for s in range(F):
			ret,img = cap.read()
			#img=cv2.resize(img,(240,240))

			diff_frames=img-pre_frames
			video[i,m]=img[:,:,0]
			m=m+1
			video[i,m]=img[:,:,1]
			m=m+1
			video[i,m]=img[:,:,2]
			m=m+1
			video[i,m]=diff_frames[:,:,0]
			m=m+1
			video[i,m]=diff_frames[:,:,1]
			m=m+1
			video[i,m]=diff_frames[:,:,2]
			m=m+1
			pre_frames=img
	cap.release()
	return video

#main function start here
if __name__ == '__main__':
	N=993
	F=3
#	sample=0
#ddN=350
	n=0
	sample=38479
	y = []
	a=range(sample)
	random.shuffle(a)
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



	env = lmdb.open('/home/keke/AC_caffe/Acre/Acre_train_lmdb',map_size = 1024**4,map_async=True,max_dbs=0)
	for i in range(N):
		video_path=full_path[i]#get videos' full path
		#print full_path[i]
		X=read_avi(video_path)
		#print sample
		
		t=X.shape[0]
		#print t
		for p in range(t):
			with env.begin(write=True) as txn:
				datum = caffe.proto.caffe_pb2.Datum()
				datum.channels = X.shape[1]
				datum.height = X.shape[2]
				datum.width = X.shape[3]
				datum.data = X[p].tobytes()  # or .tostring() if numpy < 1.9
				datum.label = int(y[i])

				#print "X is:",X[0,0,124,113]
				#print "size is",X.shape
				
				print "label is :",y[i]
				print "number ",p,"cell in video ",i
				str_id = '{:08}'.format(a[n]) 
				n=n+1

				print "N is :",n
				txn.put(str_id.encode('ascii'), datum.SerializeToString())
