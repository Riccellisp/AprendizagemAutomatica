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
import knn
import bayes
import os.path
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics
import timeit



caminhoSalvar = './CIC2017PreProc/'
nome = 'CIC2017PreProcBinary'
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
    val_perc = 0.2
    indexesPerFold = []
    #f1Metrics = []
    accMetrics = {"ADALINE":[], "KNN":[], "BAYES": []}
    precisionMetrics = {"ADALINE":[], "KNN":[], "BAYES": []}
    recallMetrics = {"ADALINE":[], "KNN":[], "BAYES": []}
    f1Metrics = {"ADALINE":[], "KNN":[], "BAYES": []}
    timeMetrics = {"ADALINE":[], "KNN":[], "BAYES": []}
    results = {"ADALINE":[], "KNN":[], "BAYES": []}
    fold = 0
    for train_index, test_index in skf.split(X, Y):
        X_train, X_test = X[train_index,:], X[test_index,:]
        y_train, y_test = Y[train_index], Y[test_index]
        start = timeit.default_timer()
        X_train, y_train = ClusterCentroids.ClusterCentroidsUndersampling(X_train, y_train,colunas)
    
        X_trainDivided, X_val, y_trainDivided, y_val = train_test_split(X_train, y_train, test_size = val_perc,stratify=y_train)
        
        train = pd.DataFrame(np.column_stack((X_train,y_train)), columns = colunas)
        test = pd.DataFrame(np.column_stack((X_test,y_test)), columns = colunas)
        TrainDivided = pd.DataFrame(np.column_stack((X_trainDivided,y_trainDivided)), columns = colunas)
        validation = pd.DataFrame(np.column_stack((X_val,y_val)), columns = colunas)
        parametros = {'epochs':[30, 40, 50],'alpha':[0.001, 0.01, 0.1]}
        
        # ADALINE
        resultGrid = gridSearchAlgorithms.gridsearchAdaline(parametros, TrainDivided, validation)        
        
        attrs = train.columns.tolist()[:-1]        
        pesos_adaline = adaline.adaline_fit(train,attrs,resultGrid['epochs'],resultGrid['alpha'])
        yTeste, yPred =  adaline.adaline_predict(pesos_adaline,test)
        end = timeit.default_timer()
        print(end - start)
        
        accMetrics["ADALINE"].append(metrics.accuracy_score(yTeste, yPred))
        precisionMetrics["ADALINE"].append(metrics.precision_score(yTeste, yPred, average='weighted'))
        recallMetrics["ADALINE"].append(metrics.recall_score(yTeste, yPred, average='weighted'))
        f1Metrics["ADALINE"].append(metrics.f1_score(yTeste, yPred, average='weighted'))
        timeMetrics["ADALINE"].append(end-start)
        indexesPerFold.append([train_index,test_index,])
        # KNN
        # TODO: IMPLEMENTAR GRIDSEARCH (?)
        #yTeste, yPred = knn.knn_predict(train, test, 3)
        
        #accMetrics["KNN"].append(metrics.accuracy_score(yTeste, yPred))
        #precisionMetrics["KNN"].append(metrics.precision_score(yTeste, yPred, average='weighted'))
        #recallMetrics["KNN"].append(metrics.recall_score(yTeste, yPred, average='weighted'))
        ##f1Metrics["KNN"].append(metrics.f1_score(yTeste, yPred, average='weighted'))

        # NAIVE BAYES
        # TODO: IMPLEMENTAR GRIDSEARCH (?)
        ##ids_classes = pd.unique(train['label']).tolist()
        #attrs = train.columns.tolist()[:-1]

        #p, pp = bayes.naive_bayes_fit(train, ids_classes, attrs)
        #yTeste, yPred = bayes.naive_bayes_predict(test, ids_classes, p, pp)
        
        #accMetrics["BAYES"].append(metrics.accuracy_score(yTeste, yPred))
        #precisionMetrics["BAYES"].append(metrics.precision_score(yTeste, yPred, average='weighted'))
        #recallMetrics["BAYES"].append(metrics.recall_score(yTeste, yPred, average='weighted'))
        #f1Metrics["BAYES"].append(metrics.f1_score(yTeste, yPred, average='weighted'))
        print(fold)
        fold = fold + 1
    results["ADALINE"] = [np.mean(accMetrics["ADALINE"]),np.mean(precisionMetrics["ADALINE"]),np.mean(recallMetrics["ADALINE"]),np.mean(f1Metrics["ADALINE"]),np.mean(timeMetrics["ADALINE"])]    
    print(f1Metrics)
        
        
