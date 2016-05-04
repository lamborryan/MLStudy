#!/bin/env python
# coding:utf-8
"""
@author:ruanchengfeng 
@email=:ruanchengfeng@xiaomei.com  
@date=16/5/3
@project=MachineLearning
"""

from setuptools import setup, find_packages

setup(name='ml_lambo',
      version='1.0',
      packages = find_packages('src'),
      package_dir = ({'':'src'}))
