#! /usr/bin/bash

# for output
#mkdir -p ${HOME}/results

# Python3 command
PY3="python"

# first, traing a classifier.

#mytrain
${PY3} mytrian_class.py  -o ./results/my_classifier_0402  -i D:/github/dataset  -c ./sampledata/teeth.txt  -l ./results/my_classifier_0402.log  --dataset-type 'teeth' --device cuda:0

# train PointNet-LK. fine-tune the PointNet feature for classification (the above file).
#${PY3} train_pointlk.py   -o ./results/ex1_pointlk_0915   -i D:/github/ModelNet40 -c ./sampledata/modelnet40_half1.txt   -l ./results/ex1_pointlk_0211.log  --transfer-from ./results/ex1_classifier_0211_feat_best.pth  --epochs 400 --device cuda:0



#EOF
