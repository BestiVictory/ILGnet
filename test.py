import sys
import caffe
import numpy as np
import os

dir = os.path.join(
    os.path.dirname(os.path.realpath(__file__)))
model_file = os.path.join(dir, 'bvlc_googlenet_iter_175750.caffemodel')
net_file = os.path.join(dir, 'deploy.prototxt')
#if you have no GPUs,set mode cpu
caffe.set_mode_gpu()
net = caffe.Net(net_file, model_file, caffe.TEST)
transformer = caffe.io.Transformer({'data':net.blobs['data'].data.shape})
#set mean file may improve the result,but isn't must be
#transformer.set_mean('data', np.load('../../python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1))
transformer.set_transpose('data',(2,0,1))
transformer.set_raw_scale('data',255)
transformer.set_channel_swap('data',(2,1,0))
net.blobs['data'].reshape(1,3,227,227)
img = caffe.io.load_image('C:/Users/gaoxi/Pictures/262.jpg')
net.blobs['data'].data[...] = transformer.preprocess('data',img)
out = net.forward()
out1 = out["prob"][0]
print "the probility of good picture is:" + str(out1[0])
print "the probility of bad picture is:" + str(out1[1])