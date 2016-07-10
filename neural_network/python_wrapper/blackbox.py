import sys 
import os
import numpy as np
import os.path as osp
import matplotlib.pyplot as plt
from copy import copy
import caffe 
import matplotlib.image as mpimg

caffe_root = '/usr/local/caffe/'
caffe.set_mode_cpu()
mu = np.load(caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy')
mu = mu.mean(1).mean(1) 

scenes = np.asarray(['artstudio',
                     'bar',
                     'bathroom',
                     'bedroom',
                     'children_room',
                     'classroom',
                     'dining_room',
                     'gameroom',
                     'garage',
                     'kitchen',
                     'livingroom',
                     'meeting_room',
                     'office',
                     'restaurant'])

objects = np.asarray(['aeroplane', 
						'bicycle', 
						'bird', 
						'boat', 
						'bottle', 
						'bus', 
						'car', 
						'cat', 
						'chair', 
						'cow', 
						'table', 
						'dog', 
						'horse', 
						'motorbike', 
						'person', 
						'plant', 
						'sheep', 
						'sofa', 
						'train', 
						'table'])

class WF_Vision:

	def __init__(self, img_path):
		self.img_path = img_path
		self.scene_model_weights = '/Users/tianchuliang/Documents/Projects/wayfair_hackathon/scene_net/scene_net_snapshot_iter_1000.caffemodel'
		self.scene_model_def = '/Users/tianchuliang/Documents/Projects/wayfair_hackathon/scene_net/deploy.prototxt'
		self.object_model_weights = caffe_root + 'examples/pascal_multilabel_with_datalayer/snapshot_iter_258.caffemodel'
		self.object_model_def = caffe_root + 'examples/pascal_multilabel_with_datalayer/deploy.prototxt'

	def recognize_scene(self, img_name):
		deployed_net = caffe.Net(
    	self.scene_model_def,
    	self.scene_model_weights,
    	caffe.TEST
		)

		test_img=mpimg.imread(self.img_path+'/'+img_name)

		transformer = caffe.io.Transformer({'data': deployed_net.blobs['data'].data.shape})
		transformer.set_transpose('data', (2,0,1))  # move image channels to outermost dimension
		transformer.set_mean('data', mu)            # subtract the dataset-mean value in each channel
		transformer.set_channel_swap('data', (2,1,0)) 
		transformed_image = transformer.preprocess('data',test_img)
		
		deployed_net.blobs['data'].data[...] = transformed_image
		
		output = deployed_net.forward()

		return scenes[output['prob'][0].argsort()[::-1]][:3].tolist()

	def recognize_objects(self, img_name):
		deployed_net = caffe.Net(
			self.object_model_def,
			self.object_model_weights,
			caffe.TEST
			)

		test_img=mpimg.imread(self.img_path+'/'+img_name)

		transformer = caffe.io.Transformer({'data': deployed_net.blobs['data'].data.shape})
		transformer.set_transpose('data', (2,0,1))  # move image channels to outermost dimension
		transformer.set_mean('data', mu)            # subtract the dataset-mean value in each channel
		transformer.set_channel_swap('data', (2,1,0)) 
		transformed_image = transformer.preprocess('data',test_img)
		
		deployed_net.blobs['data'].data[...] = transformed_image
		
		output = deployed_net.forward()

		return objects[np.where(output['score'][0]>0)[0]].tolist() 

if __name__ == "__main__":
	wf_v = WF_Vision('/Users/tianchuliang/Desktop')
	# print wf_v.recognize_scene('test_kitchen.jpg')
	print wf_v.recognize_objects('test_living_room_1.jpg')

