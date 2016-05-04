#!/usr/bin/python
import os
import numpy as np
import cv2
import caffe
import lmdb
import time
def makelmdb(path):
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
			#print full_path[n]
			#print n
			n=n+1
#@profile
def read_avi(avi_path):
	m=0
	L=3
	global video
	cap = cv2.VideoCapture(avi_path)
	for i in range(L):
		ret,img = cap.read()
		img=cv2.resize(img,(240,240))
		#img=cv2.resize(img,(320,240))
		#cv2.imwrite("ttjpg.jpg",img)
		video[m]=img[:,:,0]
		m=m+1
		video[m]=img[:,:,1]
		m=m+1
		video[m]=img[:,:,2]
		m=m+1
		#time.sleep(10)
	cap.release

	#print video[1]
	#time.sleep(5)
	#return video

#main function start here
if __name__ == '__main__':
	N=1000
	n=0
	T=10
	y = []
	video_label=0
	full_path=[]
	video=np.zeros((30,240,240),dtype=np.uint8)
	X=np.zeros((T,30,240,240), dtype=np.uint8)
	'''
	img=cv2.imread('games.jpg',0)
	video=cv2.resize(img,(240,240))
	
	video[1]=img[:,:,1]
	video[2]=img[:,:,1]
	video[3]=img[:,:,1]
	video[4]=img[:,:,1]
	video[5]=img[:,:,1]
	video[6]=img[:,:,1]
	video[7]=img[:,:,1]
	video[8]=img[:,:,1]
	video[9]=img[:,:,1]
	video[10]=img[:,:,1]
'''
	#@profile
	env = lmdb.open('mylmdb',map_size = 1024**4,map_async=True,max_dbs=0)

	with env.begin(write=True) as txn:
		makelmdb('/home/zkk/caffe/python/UCF_101')
		for i in range(N):
			video_path=full_path[i]#get videos' full path
			print full_path[i]
			read_avi(video_path)
			X[1]=video
			#print X[1]
			datum = caffe.proto.caffe_pb2.Datum()
			datum.channels = X.shape[1]
			datum.height = X.shape[2]
			datum.width = X.shape[3]
			datum.data = X[1].tobytes()  # or .tostring() if numpy < 1.9
			datum.label = int(y[i])
			#print y[i]
			print i
			str_id = '{:08}'.format(i)
			txn.put(str_id.encode('ascii'), datum.SerializeToString())
			#del X
			#gc.collect()
