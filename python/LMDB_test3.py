#!/usr/bin/python
import os
import numpy as np
import cv2
import caffe
import lmdb
import time
import gc

def get_videopath(path):
	global video_label
	global y
	global n
	global full_path
	dir_list=os.listdir(path)#read all action folders
	for dir_action in dir_list:
		video_path=os.listdir(path+'/'+dir_action)#read all videos' name in one action folder
		video_label=video_label+1
		for file in video_path:
			full_path.append(path+'/'+dir_action+'/'+file)#make vedio's fullpath
			y.append(video_label)
			n=n+1

def read_avi(avi_path):
	global y
	m=0
	L=3
	global i
	X=np.zeros((1,30,240,320),dtype=np.uint8)
	cap = cv2.VideoCapture(avi_path)
	for f in range(L):
		ret,img = cap.read()
		#img=cv2.resize(img,(320,240))
		#cv2.imwrite("ttjpg.jpg",img)
		X[0,m]=img[:,:,0]
		m=m+1
		X[0,m]=img[:,:,1]
		m=m+1
		X[0,m]=img[:,:,2]
		m=m+1
		#time.sleep(10)
	cap.release
	datum = caffe.proto.caffe_pb2.Datum()
	datum.channels = X.shape[1]
	datum.height = X.shape[2]
	datum.width = X.shape[3]
	datum.data = X[0].tobytes()  # or .tostring() if numpy < 1.9
	datum.label = int(y[i])
	print i
	i=i+1
	#print i
	str_id = '{:08}'.format(i)
	txn.put(str_id.encode('ascii'), datum.SerializeToString())
	del X
	gc.collect()

#main function start here
N=1000
n=0
T=100
y = []
video_label=0
full_path=[]
#@profile
env = lmdb.open('mylmdb',map_size = 1024**4,map_async=True,max_dbs=0)
with env.begin(write=True) as txn:
    get_videopath('/home/zkk/caffe/python/UCF_101')
    for i in range(N):
        read_avi(full_path[i])
