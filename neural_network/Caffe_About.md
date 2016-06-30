# Caffe Configuration

+ Author: Tianchu(Alex) Liang
+ Email: liangtianchu@gmail.com
+ Github: github.com/tianchuliang

## AWS Instance

The training of our multi-label Convolutional Neural Network (CNN) is trained using GPU-supported Caffe.
Our Caffe framework is installed, configuered, and hosted at an AWS instance. (Instance ID: ...)

Our AWS instance has the following hardware composition:
+ Instance Type: g2.2xlarge
+ Root Device Type: ebs
+ Root Device: /dev/sda1
+ Block Devices: /dev/sda1, /dev/sdc
+ GPU: Nvidia GPU Grid K250
+ CUDA: Cuda-7.5

Our AWS instance has the following OS and software composition:
+ AMI ID: ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-20160114.5 (ami-fce3c696)
+ Caffe: https://github.com/BVLC/caffe (Most up-to-date as of June 30th 2016); GPU version with Cuda-7.5 (without cuDNN)
+ Python: Python2.7.6
+ GCC:
+ gFortran:
+ Numpy:
+ Boost:
+ protobuf:
+ pip:

__NOTE__: The Makefile.config of our Caffe installation gives more detailed info.
