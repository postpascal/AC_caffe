#!/usr/bin/python
import os
import numpy as np
import random
def makelmdb(path):
	global video_label
	global y
	global full_path
	global i
	dir_list=os.listdir(path)#read all action folders
	for dir_action in dir_list:
		if (dir_action[0]=="."):
			pass
		else:
			video_path=os.listdir(path+'/'+dir_action)#read all videos' name in one action folder
			video_label=video_label+1
			for file in video_path:
				#full_path.append(path+'/'+dir_action+'/'+file)#make vedio's fullpath
				y.append(video_label)
				p=path+'/'+dir_action+'/'+file
				f.write(p+" ")
				ss=str(video_label)
				f.write(ss+"\n")
				i=i+1

#N=510
y = []
video_label=-1
full_path=[]
i=0
f=open("Ac_test_name.txt","w")
makelmdb('/home/keke/AC_caffe/python/UCF_10/ucf_10_test')
f.close()
#shuffle videos' path
lines = open('Ac_test_name.txt').readlines()
random.shuffle(lines)
open('Ac_test_name.txt', 'w').writelines(lines)
print i,"videos in this testset\n"
