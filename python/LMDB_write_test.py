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
def read_avi(avi_path):
	m=0
	global video
	cap = cv2.VideoCapture(avi_path)
	length=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
#	if length >150:
#		length=150
	for i in range(length):
		ret,img = cap.read()
		img=cv2.resize(img,(240,240))
		if i<1:
			pre_frames=img
		else:
			diff_frames=img-pre_frames
			video[m]=img[:,:,0]
			m=m+1
			video[m]=img[:,:,1]
			m=m+1
			video[m]=img[:,:,2]
			m=m+1
			video[m]=diff_frames[:,:,0]
			m=m+1
			video[m]=diff_frames[:,:,1]
			m=m+1
			video[m]=diff_frames[:,:,2]
			m=m+1
		#time.sleep(10)
	cap.release

	#print video[1]
	#time.sleep(5)
	#return video

#main function start here
if __name__ == '__main__':
	N=100
#N=350
	n=0
	T=10
	y = []
	video_label=0
	full_path=[]
	video=np.zeros((900,240,240),dtype=np.uint8)
	X=np.zeros((T,900,240,240), dtype=np.uint8)
	#@profile
	env = lmdb.open('/home/keke/caffe-master/Acre/Acre_test_lmdb',map_size = 1024**4,map_async=True,max_dbs=0)
	makelmdb('/home/keke/caffe-master/python/UCF_10/ucf_10_test')
	for i in range(N):
		with env.begin(write=True) as txn:
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
