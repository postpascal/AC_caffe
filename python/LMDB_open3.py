#!/usr/bin/python
import caffe
import lmdb
import numpy as np
import time
import os
import caffe.proto.caffe_pb2
from caffe.io import datum_to_array

lmdb_env = lmdb.open('/home/keke/AC_caffe/Acre/Acre_test_lmdb')
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe.proto.caffe_pb2.Datum()

i=0
for key, value in lmdb_cursor:
    datum.ParseFromString(value)
    label = datum.label
    print "label is :",label
    data = caffe.io.datum_to_array(datum)
    time.sleep(1)
    for d in data:
	print np.shape(d)
        print "image is:",d[200,200]
        print i
        i=i+1
