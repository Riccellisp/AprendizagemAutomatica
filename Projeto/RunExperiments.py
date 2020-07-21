#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:42:24 2020

@author: riccelli
"""


import common
import PreProcessingFinal
import ClusterCentroids
import classifiersEval
import Allclassifiers
import gridSearchAlgorithms
import adaline
import os.path
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics


caminhoSalvar = '/home/riccelli/AprendizagemAutomatica/Projeto/CIC2017PreProc/'
nome = 'CIC2017PreProcBinaryTiny'
extensao = '.csv'
if not os.path.isfile(caminhoSalvar+nome+extensao):
    caminho = '/home/riccelli/MachineLearningCVE/'
    low_memoryBoolean = False
    df = PreProcessingFinal.leituraConcat(caminho,low_memoryBoolean)
    df = PreProcessingFinal.removeInfinityNa(df)
    df = PreProcessingFinal.removeInfinityNa(df)
    categorias = common.mostrarQuantitativoCategorias(df,"label")
    df = PreProcessingFinal.converterNumericalEnconding(df,"label")
    df = PreProcessingFinal.binarizarLabel(df)
    df = PreProcessingFinal.hashingFeatureEncoding(df,"destination_port",20)
    PreProcessingFinal.salvarDataset(df,caminhoSalvar,nome,extensao)
    
else:
    df = pd.read_csv(caminhoSalvar+nome+extensao,low_memory=False)
    min_max_scaler = preprocessing.MinMaxScaler()
    np_scaled = min_max_scaler.fit_transform(df)
    colunas = df.columns
    df = pd.DataFrame(np_scaled, columns = colunas)
    df = df.sample(frac = 0.2)
    X = np.array(df.iloc[:,0:97])
    Y = np.array(df.iloc[:,-1])
    #del df
    skf = StratifiedKFold(n_splits=10)
    #skf.get_n_splits(X, Y)
    print(skf) 
    val_perc = 0.5
    indexesPerFold = []
    f1Metrics = []
    for train_index, test_index in skf.split(X, Y):
        X_train, X_test = X[train_index,:], X[test_index,:]
        y_train, y_test = Y[train_index], Y[test_index]
        X_train, y_train = ClusterCentroids.ClusterCentroidsUndersampling(X_train, y_train,colunas)
    
        X_trainDivided, X_val, y_trainDivided, y_val = train_test_split(X_train, y_train, test_size = val_perc,stratify=y_train)
        #indexesPerFold.append(train_index)
        
        train = pd.DataFrame(np.column_stack((X_train,y_train)), columns = colunas)
        test = pd.DataFrame(np.column_stack((X_test,y_test)), columns = colunas)
        TrainDivided = pd.DataFrame(np.column_stack((X_trainDivided,y_trainDivided)), columns = colunas)
        validation = pd.DataFrame(np.column_stack((X_val,y_val)), columns = colunas)
        parametros = {'epochs':[100,200 ,300],'alpha':[0.001, 0.01, 0.1]}
        
        resultGrid = gridSearchAlgorithms.gridsearchAdaline(parametros, TrainDivided, validation)        
        
        attrs = train.columns.tolist()[:-1]        
        pesos_adaline = adaline.adaline_fit(train,attrs,resultGrid['epochs'],resultGrid['alpha'])
        yTeste, yPred =  adaline.adaline_predict(pesos_adaline,test)
        f1 = metrics.f1_score(yTeste, yPred,average='weighted')

        f1Metrics.append(f1)
        
        
