#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:06:26 2020

@author: riccelli
"""


import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.neighbors.nearest_centroid import NearestCentroid
import timeit
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split

caminho = '/home/riccelli/CIC2017PreProc/CIC2017PreProcBinary.csv'
df = pd.read_csv(caminho,low_memory=True)
X = np.array(df.iloc[:,0:97])
Y = np.array(df.iloc[:,-1])
del df
skf = StratifiedKFold(n_splits=10)
skf.get_n_splits(X, Y)
print(skf) 
val_perc = 0.2
for train_index, test_index in skf.split(X, Y):
    X_train, X_test = X[train_index,:], X[test_index,:]
    y_train, y_test = Y[train_index], Y[test_index]
    X_trainDivided, X_val, y_trainDivided, y_val = train_test_split(X_train, y_train, test_size = val_perc)
    