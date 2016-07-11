#!/usr/bin/env sh

./build/tools/caffe train \
    -solver object_net/solver.prototxt \
    -weights models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel \
    -gpu 0 
