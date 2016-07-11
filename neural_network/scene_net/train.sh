#!/usr/bin/env sh

./build/tools/caffe train \
    -solver scene_net/scene_net/solver.prototxt \
    -weights models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel \
    -gpu 0
