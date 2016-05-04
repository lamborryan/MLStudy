#!/bin/env python
# coding:utf-8
"""
@author:ruanchengfeng 
@email=:ruanchengfeng@xiaomei.com  
@date=16/5/3
@project=MachineLearning
"""

## 归一化

from numpy import *

def norm(data):
    minData = data.min(0)
    maxData = data.max(0)
    normSet = (data - minData)/(maxData - minData)
    return normSet
