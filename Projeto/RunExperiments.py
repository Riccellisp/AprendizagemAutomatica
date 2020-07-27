#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:42:24 2020

@author: riccelli
"""


import common
import PreProcessingFinal
import ClusterCentroids
import gridSearchAlgorithms
import adaline
import knn
import bayes
import nearest_centroid
import os.path
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics
import timeit
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


caminhoSalvar = './CIC2017PreProc/'
nome = 'CIC2017PreProcBinaryTiny'
extensao = '.csv'
path = caminhoSalvar +nome + extensao
print(path)
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
    #df = df.sample(frac = 0.2)
    X = np.array(df.iloc[:,0:97])
    Y = np.array(df.iloc[:,-1])
    #del df
    skf = StratifiedKFold(n_splits=10)
    #skf.get_n_splits(X, Y)
    print(skf) 
    val_perc = 0.2
    indexesPerFold = []
    accMetrics = {"ADALINE":[], "KNN":[], "BAYES": [], "NC": [], "RF": [], "SVM": [], "ADA": []}
    precisionMetrics = {"ADALINE":[], "KNN":[], "BAYES": [], "NC": [], "RF": [], "SVM": [], "ADA": []}
    recallMetrics = {"ADALINE":[], "KNN":[], "BAYES": [], "NC": [], "RF": [], "SVM": [], "ADA": []}
    f1Metrics = {"ADALINE":[], "KNN":[], "BAYES": [], "NC": [], "RF": [], "SVM": [], "ADA": []}
    timeMetrics = {"ADALINE":[], "KNN":[], "BAYES": [], "NC": [], "RF": [], "SVM": [], "ADA": []}
    results = {"ADALINE":[], "KNN":[], "BAYES": [], "NC": [], "RF": [], "SVM": [], "ADA": []}
    fold = 0
    for train_index, test_index in skf.split(X, Y):
        X_train, X_test = X[train_index,:], X[test_index,:]
        y_train, y_test = Y[train_index], Y[test_index]
        
        X_train, y_train = ClusterCentroids.ClusterCentroidsUndersampling(X_train, y_train,colunas)
    
        X_trainDivided, X_val, y_trainDivided, y_val = train_test_split(X_train, y_train, test_size = val_perc,stratify=y_train)
        
        train = pd.DataFrame(np.column_stack((X_train,y_train)), columns = colunas)
        test = pd.DataFrame(np.column_stack((X_test,y_test)), columns = colunas)
        
        TrainDivided = pd.DataFrame(np.column_stack((X_trainDivided,y_trainDivided)), columns = colunas)
        validation = pd.DataFrame(np.column_stack((X_val,y_val)), columns = colunas)
        
        # ADALINE GridSearch
        parametros = {'epochs':[30, 40, 50],'alpha':[0.001, 0.01, 0.1]}
        resultGrid = gridSearchAlgorithms.gridsearchAdaline(parametros, TrainDivided, validation)        
        #Utilizando os parametros eencontrados no conjunto de validação
        attrs = train.columns.tolist()[:-1]      
        start = timeit.default_timer()
        pesos_adaline = adaline.adaline_fit(train,attrs,resultGrid['epochs'],resultGrid['alpha'])
        yTeste, yPred =  adaline.adaline_predict(pesos_adaline,test)
        end = timeit.default_timer()
        print(end - start)
        
        # Salvando metricas
        accMetrics["ADALINE"].append(metrics.accuracy_score(yTeste, yPred))
        precisionMetrics["ADALINE"].append(metrics.precision_score(yTeste, yPred, average='weighted'))
        recallMetrics["ADALINE"].append(metrics.recall_score(yTeste, yPred, average='weighted'))
        f1Metrics["ADALINE"].append(metrics.f1_score(yTeste, yPred, average='weighted'))
        timeMetrics["ADALINE"].append(end-start)
        
        
        # NEAREST CENTROID
        attrs = train.columns.tolist()[:-1]
        start = timeit.default_timer()
        centroids, classes = nearest_centroid.nearest_centroid_fit(train, test)
        yTeste, yPred =  nearest_centroid.nearest_centroid_predict(centroids, classes,test)
        end = timeit.default_timer()
        print(end - start)
        
        accMetrics["NC"].append(metrics.accuracy_score(yTeste, yPred))
        precisionMetrics["NC"].append(metrics.precision_score(yTeste, yPred, average='weighted'))
        recallMetrics["NC"].append(metrics.recall_score(yTeste, yPred, average='weighted'))
        f1Metrics["NC"].append(metrics.f1_score(yTeste, yPred, average='weighted'))
        timeMetrics["NC"].append(end-start)
        
        # KNN
        # TODO: IMPLEMENTAR GRIDSEARCH (?)
        parametros = {'k':[3, 5, 7],'distance':['euclidean','manhatthan']}
        resultGrid = gridSearchAlgorithms.gridsearchKnn(parametros, TrainDivided, validation)
        
        start = timeit.default_timer()
        yTeste, yPred = knn.knn_predict(train, test, resultGrid)
        end = timeit.default_timer()
        print(end - start)
        
        accMetrics["KNN"].append(metrics.accuracy_score(yTeste, yPred))
        precisionMetrics["KNN"].append(metrics.precision_score(yTeste, yPred, average='weighted'))
        recallMetrics["KNN"].append(metrics.recall_score(yTeste, yPred, average='weighted'))
        f1Metrics["KNN"].append(metrics.f1_score(yTeste, yPred, average='weighted'))
        timeMetrics["KNN"].append(end-start)
        
        
        # NAIVE BAYES
        # TODO: IMPLEMENTAR GRIDSEARCH (?)
        ids_classes = pd.unique(train['label']).tolist()
        attrs = train.columns.tolist()[:-1]
        start = timeit.default_timer()
        p, pp = bayes.naive_bayes_fit(train, ids_classes, attrs)
        yTeste, yPred = bayes.naive_bayes_predict(test, ids_classes, p, pp)
        end = timeit.default_timer()
        print(end - start)
        
        accMetrics["BAYES"].append(metrics.accuracy_score(yTeste, yPred))
        precisionMetrics["BAYES"].append(metrics.precision_score(yTeste, yPred, average='weighted'))
        recallMetrics["BAYES"].append(metrics.recall_score(yTeste, yPred, average='weighted'))
        f1Metrics["BAYES"].append(metrics.f1_score(yTeste, yPred, average='weighted'))
        timeMetrics["BAYES"].append(end-start)
        
        # RANDOM FOREST
        parametros = {'n_estimators':[30, 40, 50],'criterion':['gini', 'entropy']}
        resultGrid = gridSearchAlgorithms.gridsearchRF(parametros, X_trainDivided,y_trainDivided,X_val, y_val) 
        rf = RandomForestClassifier(n_estimators=resultGrid['n_estimators'], criterion=resultGrid['criterion'])
        start = timeit.default_timer()
        rf.fit(X_train, y_train)
        yPred = rf.predict(X_test)
        end = timeit.default_timer()
        print(end - start)
       
        accMetrics["RF"].append(metrics.accuracy_score(y_test, yPred))
        precisionMetrics["RF"].append(metrics.precision_score(y_test, yPred, average='weighted'))
        recallMetrics["RF"].append(metrics.recall_score(y_test, yPred, average='weighted'))
        f1Metrics["RF"].append(metrics.f1_score(y_test, yPred, average='weighted'))
        timeMetrics["RF"].append(end-start)
        
        #Adaboost
        parametros = {'n_estimators':[1, 5, 10],'learning_rate':[0.1, 1, 2]}
        resultGrid =  gridSearchAlgorithms.gridsearchAdaBoost(parametros,X_trainDivided,y_trainDivided,X_val,y_val)
        clf = AdaBoostClassifier(n_estimators=resultGrid['n_estimators'],learning_rate=resultGrid['learning_rate'])
        start = timeit.default_timer()
        clf.fit(X_train,y_train)
        yPred = clf.predict(X_test)
        end = timeit.default_timer()
        print(end - start)
        
        accMetrics["ADA"].append(metrics.accuracy_score(y_test, yPred))
        precisionMetrics["ADA"].append(metrics.precision_score(y_test, yPred, average='weighted'))
        recallMetrics["ADA"].append(metrics.recall_score(y_test, yPred, average='weighted'))
        f1Metrics["ADA"].append(metrics.f1_score(y_test, yPred, average='weighted'))
        timeMetrics["ADA"].append(end-start)
        
        # SVM
        parametros = {'C':[1, 10, 20],'kernel':['rbf', 'poly','sigmoid']}
        resultGrid = gridSearchAlgorithms.gridsearchSVM(parametros, X_trainDivided,y_trainDivided,X_val, y_val) 
        svm = SVC(kernel=resultGrid['kernel'], C=resultGrid['C'])
        start = timeit.default_timer()
        svm.fit(X_train, y_train)
        y_pred = svm.predict(X_test)
        end = timeit.default_timer()
        
        accMetrics["SVM"].append(metrics.accuracy_score(y_test, y_pred))
        precisionMetrics["SVM"].append(metrics.precision_score(y_test, y_pred, average='weighted'))
        recallMetrics["SVM"].append(metrics.recall_score(y_test, y_pred, average='weighted'))
        f1Metrics["SVM"].append(metrics.f1_score(y_test, y_pred, average='weighted'))
        timeMetrics["SVM"].append(end-start)
        
        print(fold)
        fold = fold + 1
        
    results["ADALINE"] = [np.mean(accMetrics["ADALINE"]),np.mean(precisionMetrics["ADALINE"]),np.mean(recallMetrics["ADALINE"]),np.mean(f1Metrics["ADALINE"]),np.mean(timeMetrics["ADALINE"])]
    results["NC"] = [np.mean(accMetrics["NC"]),np.mean(precisionMetrics["NC"]),np.mean(recallMetrics["NC"]),np.mean(f1Metrics["NC"]),np.mean(timeMetrics["NC"])]      
    results["BAYES"] = [np.mean(accMetrics["BAYES"]),np.mean(precisionMetrics["BAYES"]),np.mean(recallMetrics["BAYES"]),np.mean(f1Metrics["BAYES"]),np.mean(timeMetrics["BAYES"])]      
    results["KNN"] = [np.mean(accMetrics["KNN"]),np.mean(precisionMetrics["KNN"]),np.mean(recallMetrics["KNN"]),np.mean(f1Metrics["KNN"]),np.mean(timeMetrics["KNN"])]      
    results["RF"] = [np.mean(accMetrics["RF"]),np.mean(precisionMetrics["RF"]),np.mean(recallMetrics["RF"]),np.mean(f1Metrics["RF"]),np.mean(timeMetrics["RF"])]      
    results["SVM"] = [np.mean(accMetrics["SVM"]),np.mean(precisionMetrics["SVM"]),np.mean(recallMetrics["SVM"]),np.mean(f1Metrics["SVM"]),np.mean(timeMetrics["SVM"])]      
    results["ADA"] = [np.mean(accMetrics["ADA"]),np.mean(precisionMetrics["ADA"]),np.mean(recallMetrics["ADA"]),np.mean(f1Metrics["ADA"]),np.mean(timeMetrics["ADA"])]      

    print(results)
    
        
        
