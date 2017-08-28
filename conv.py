#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 01:40:24 2017

@author: Bowen Wei
"""
import numpy as np
class Conv2D:
    def __init__(self,in_channel, o_channel, kernel_size, stride, mode):
        self.in_channel=in_channel
        self.o_channel=o_channel
        self.kernel_size=kernel_size
        self.stride=stride
        self.mode=mode
    def forward(self,image):
        image_size_x=image.shape[0]
        image_size_y=image.shape[1]
        kernel_size=self.kernel_size
        stride=self.stride
        o_channel=self.o_channel
        in_channel=self.in_channel
        half_size=int(np.floor(kernel_size/2))
        o_size_x=int(np.floor((image_size_x-half_size*2)/stride))
        o_size_y=int(np.floor((image_size_y-half_size*2)/stride))
        out_image=np.zeros((o_size_x,o_size_y,self.o_channel),dtype=np.int)
        num_operation=0;
        if self.mode=='known':
            k1 = np.array([[-1,-1,-1],
                        [0,0,0],
                        [1,1,1]])
            k2 = np.array([[-1,0,1],
                        [-1,0,1],
                        [-1,0,1]])
            k3 = np.array([[1,1,1],
                        [1,1,1],
                        [1,1,1]])
            k_3=np.stack((k1,k2,k3),axis=-1)
            k4 = np.array([[-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1],
                        [0,0,0,0,0],
                        [1,1,1,1,1],
                        [1,1,1,1,1]])
            k5 = np.array([[-1,-1,0,1,1],
                        [-1,-1,0,1,1],
                        [-1,-1,0,1,1],
                        [-1,-1,0,1,1],
                        [-1,-1,0,1,1]])
            k_5=np.stack((k4,k5),axis=-1)
            if kernel_size==3:
                kernel=k_3              
            elif kernel_size==5:
                kernel=k_5
            else:
                return 'kernel error'
        elif self.mode=='rand':
            kernel=np.random.rand(kernel_size,kernel_size,o_channel)
        else:
            return 'mode error'
        for outchannel in range (0,o_channel):  
            for i1 in range(0,o_size_x):
                for j1 in range(0,o_size_y):
                    x_c=half_size+i1*stride
                    y_c=half_size+j1*stride
                    sum=0;
                    for i2 in range(0,kernel_size):
                        for j2 in range(0,kernel_size):
                            for inchannel in range(0,in_channel):               
                                sum+=kernel[i2,j2,outchannel]*image[(x_c-half_size+i2),(y_c-half_size+j2),inchannel]
                                num_operation+=1
                    out_image[i1,j1,outchannel]=sum
        return num_operation, out_image