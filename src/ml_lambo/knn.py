#!/bin/env python
# coding:utf-8
"""
@author:ruanchengfeng 
@email=:ruanchengfeng@xiaomei.com  
@date=16/5/3
@project=MachineLearning
"""

from numpy import *
import operator

## KNN算法
def KNNClassify(inx,dataSet,labels,k):
    dist = (sum((dataSet - inx)**2,axis=1))**0.5
    sortedDistIndicies = dist.argsort()
    flagCount = {}
    for i in range(k):
        flag = labels[sortedDistIndicies[i]]
        flagCount[flag] = flagCount.get(flag,0) + 1
    sortFlags = sorted(flagCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortFlags[0][0]

