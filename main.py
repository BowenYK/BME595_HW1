#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 01:39:47 2017

@author: Bowen Wei
"""
#%%
import numpy as np
from scipy import misc
from conv import Conv2D
import time
import matplotlib.pyplot as plt
#%%
input_image = misc.imread('small image.png')
#%%
conv2d = Conv2D(in_channel=3, o_channel=2, kernel_size=3, stride=1,mode='rand')
#%%
start=time.clock()
[num_operation,output_image] = conv2d.forward(input_image)
time_taken=time.clock()-start
#%%
misc.imsave('image2_task1.jpg',output_image[:,:,0])
#%%
num=np.zeros(5,dtype=np.int)
n=0
for k in [3,5,7,9,11]:
    conv2d = Conv2D(in_channel=3, o_channel=2, kernel_size=k, stride=1,mode='rand')
    [num_operation,output_image] = conv2d.forward(input_image)
    num[n]=num_operation
    n+=1
#%%
plt.plot([3,5,7,9,11],num)
plt.ylabel('number of operation')
plt.xlabel('kernel size')
plt.savefig('operation.jpg')
#%%
time_taken=np.zeros(12,dtype=np.int)
n=0
for k in np.power(2,range(0,12)):
    conv2d = Conv2D(in_channel=3, o_channel=k, kernel_size=1, stride=1,mode='rand')
    start=time.clock()
    [num_operation,output_image] = conv2d.forward(input_image)
    time_taken[n]=time.clock()-start
    n+=1
 #%%
plt.plot(range(0,12),time_taken)
plt.ylabel('time taken in seconds')
plt.xlabel('i')
plt.savefig('time_taken.jpg')