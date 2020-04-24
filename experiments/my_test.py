# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:45:12 2020

@author: RenTeng
"""

"""
    Example for testing PointNet-LK.

    No-noise version.
"""

import argparse
import os
import sys
import logging
import numpy
import torch
import torch.utils.data
import torchvision
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot

# addpath('../')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
import ptlk








class Action:
    def __init__(self, num_classes):
        self.num_classes = num_classes
        self.dim_k = 1024
        self.use_tnet = False

#        if args.symfn == 'max':
        self.sym_fn = ptlk.pointnet.symfn_max
#       if args.symfn == 'avg':
#            self.sym_fn = ptlk.pointnet.symfn_avg

    def create_model(self):
        feat = ptlk.pointnet.PointNet_features(self.dim_k, self.use_tnet, self.sym_fn)
        return ptlk.pointnet.PointNet_classifier(self.num_classes, feat, self.dim_k)



    def predict(self, model, test, device):
        model.eval()
     
        point = test.to(device)
        points = point.unsqueeze(0)
        
        output = model(points)
        # print(output)
        _, pred1 = output.max(dim=1)
      
        # print(pred1)

        return pred1.item()



data_path = "D:/github/dataset/saiya/BiteScan_12.obj"

def plot(test, fig=None, ax=None):
        v = test.numpy()
        if fig is None:
            fig = matplotlib.pyplot.figure()
        if ax is None:
            ax = Axes3D(fig)
#        if p:
#            ax.add_collection3d(Poly3DCollection(p))
#        print(v,"-----")
     
        ax.scatter(v[:, 0], v[:, 1], v[:, 2],s = 1)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        matplotlib.pyplot.show()




def p(data_path):

    outer_path = data_path

    transform = torchvision.transforms.Compose([ \
        # ShapeNet2_transform_coordinate(),\
        ptlk.data.transforms.Mesh2Points(), \
        # ptlk.data.transforms.OnUnitCube(),\
        ptlk.data.transforms.Resampler(2048), \
        # ptlk.data.transforms.VoxelGridfilter(150), \
        #         ptlk.data.transforms.RandomRotatorZ(),\
        #                    ptlk.data.transforms.RandomJitter()\
    ])


    test = ptlk.data.mesh.objread(data_path)

    device = torch.device('cuda:0')
    action = Action(2)

    test = transform(test)


    
    # plot(test)

    pretrained = "./results/my_classifier_0219_model_last.pth"
    model = action.create_model()
   # model.register_forward_hook(get_activation())

  #  conv_out = LayerActivations(model.features.h1, 0)
  #  act = conv_out.features
   # print(act)



    assert os.path.isfile(pretrained)
    model.load_state_dict(torch.load(pretrained, map_location='cpu'))
    model.to(device)
   # model.plot_mid()

    res = action.predict(model,test,device)
#    if(res==1):
#        print(data_path)
    return res,test

outer_path = "D:/github/dataset/saiya"
folderlist = os.listdir(outer_path)
#  #    num_points = 1024  # 列举文件夹
# p(data_path)


# res = []
# for folder in folderlist:
#    datapath = os.path.join(outer_path, folder).replace('\\','/')
#    a = p(datapath)
   # res.append(a)
   # print(a)






#EOF







