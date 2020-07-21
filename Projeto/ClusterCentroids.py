#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 03:20:32 2020

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
    cluster_centroid = np.sum(X,axis=0)/X.shape[0]
    euclidean = [None]*X.shape[0]
    for i in range(0,X.shape[0]):
        euclidean[i] = sqrt(sum((cluster_centroid-X[i])**2))
    indices = list(reversed(sorted(range(len(euclidean)), 
    key = lambda j: euclidean[j])))
    X_f = np.delete(X, indices[:int(f/100*X.shape[0])], axis=0)
    return X_f

def ClusterCentroidsUndersampling(Xtrain,Ytrain,colunas):
    colunasx = list(colunas[0:97])
    colunasy = 'label'
    Xtrain = pd.DataFrame(Xtrain,columns=colunasx)
    Ytrain = pd.DataFrame(Ytrain,columns=[colunasy])
    df = pd.concat([Xtrain,Ytrain],axis=1)
    classesCounts = df['label'].value_counts()
    #normal
    df0 = df[df['label'] == 0]
    #ataques
    df1 = df[df['label'] == 1]
    f0=(1-(classesCounts[1]/len(df0)))*100
    #X =df0.iloc[:,0:65] 
    df0Under= pd.DataFrame(CCMUT(df0.values,f0))
    clusterCentroidDatasetUnder = pd.concat([df0Under,df1])
    return np.array(clusterCentroidDatasetUnder.iloc[0:97,:]), np.array(clusterCentroidDatasetUnder.iloc[:,-1])

def salvarDataset(df,caminho,nome):
    df.to_csv (caminho+nome+'.csv', index = None, header=True)
    