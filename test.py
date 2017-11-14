#coding=utf-8
import numpy as np
import sys,os
import caffe


net_file='deploy.prototxt'
caffe_model='bvlc_googlenet_iter_175750.caffemodel'
mean_file='AVA1_mean.npy'
#if you have no GPUs,set mode cpu
caffe.set_mode_cpu()
net = caffe.Net(net_file,caffe_model,caffe.TEST)
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))
transformer.set_raw_scale('data', 255) 
transformer.set_channel_swap('data', (2,1,0))
img = caffe.io.load_image('good01.jpg')
net.blobs['data'].data[...] = transformer.preprocess('data',img)
out = net.forward()
out1 = out["loss1/loss"][0]
print(out1)
print ("the score of the picture is:" + str(out1[1]))




