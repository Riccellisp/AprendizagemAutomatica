#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:35:01 2019

@author: riccelli
"""

import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler
from collections import Counter
from sklearn import preprocessing
import numpy as np
from math import sqrt

def CCMUT(X,f):
    # 1. finding cluster centroid....
    cluster_centroid = np.sum(X,axis=0)/X.shape[0]
    # 2. finding Euclidean Distance from cluster centroid to samples
    euclidean = [None]*X.shape[0]
    for i in range(0,X.shape[0]):
        euclidean[i] = sqrt(sum((cluster_centroid-X[i])**2))
    # 3. tracking indices of samples in descending order of distance
    indices = list(reversed(sorted(range(len(euclidean)), 
    key = lambda j: euclidean[j])))
    # 4. removing the instances or under-sampling order-wise....
    X_f = np.delete(X, indices[:int(f/100*X.shape[0])], axis=0)
    # 5. returning the under-sampled Majority Sample Matrix
    return X_f

# Read dataset
df = pd.read_csv('/home/riccelli/CIC2017PreProc/CIC2017PreProcBinaryTiny.csv')




#tamanho NSLKDD

classesCounts = df['label'].value_counts()
#normal
df0 = df[df['label'] == 0]
#bot
df1 = df[df['label'] == 1]

# 10293+7935+5897+5796+5499+1956+1507+652+36+21+11 = 39603

#33526 + 33526 + 33526 + 33526


f0=(1-(5000/len(df0)))*100
#X =df0.iloc[:,0:65] 
df0Under= pd.DataFrame(CCMUT(df0.values,f0),columns=df.columns)


clusterCentroidDatasetUnder = pd.concat([df0Under, df1, df2Under, df3, df4Under, df5, df6, df7, df8, df9, df10Under, df11, df12, df13, df14])
export_csv = clusterCentroidDatasetUnder.to_csv (r'/media/riccelli/1CBBB19519DBB1D2/Bruno/Dissertacao/CIC2017/csvs/MachineLearningCVE/CIC2017ClusterCentroidUnderSampled.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path