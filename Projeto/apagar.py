#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 00:21:06 2020

@author: riccelli
"""


import common
import PreProcessingFinal
import ClusterCentroids
import gridSearchAlgorithms
import adaline
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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

caminhoSalvar = './CIC2017PreProc/'
nome = 'BASE9_TODOS'
extensao = '.csv'
path = caminhoSalvar +nome + extensao
print(path)

df = pd.read_csv(caminhoSalvar+nome+extensao,low_memory=False)
df = df.iloc[:,1:26]
X = np.array(df.iloc[:,0:24])
Y = np.array(df.iloc[:,-1])
colunas = df.columns

#del df
skf = StratifiedKFold(n_splits=10)
print(skf) 
val_perc = 0.1
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

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    X_train, y_train = ClusterCentroids.ClusterCentroidsUndersampling(X_train, y_train,colunas)

    X_trainDivided, X_val, y_trainDivided, y_val = train_test_split(X_train, y_train, test_size = val_perc,stratify=y_train)

    train = pd.DataFrame(np.column_stack((X_train,y_train)), columns = colunas)
    test = pd.DataFrame(np.column_stack((X_test,y_test)), columns = colunas)

    TrainDivided = pd.DataFrame(np.column_stack((X_trainDivided,y_trainDivided)), columns = colunas)
    validation = pd.DataFrame(np.column_stack((X_val,y_val)), columns = colunas)


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
    print("Teempo SVM",end - start)
    

    print(fold)
    fold = fold + 1
    
    results["SVM"] = [np.mean(accMetrics["SVM"]),np.mean(precisionMetrics["SVM"]),np.mean(recallMetrics["SVM"]),np.mean(f1Metrics["SVM"]),np.mean(timeMetrics["SVM"])]      
    
    print(results)
# Criando planilha de resultados
nomeExcel = 'ReesultsSVM.xlsx'
excel = pd.ExcelWriter(nomeExcel, engine='xlsxwriter')        
Dados = pd.DataFrame(results)
Dados.to_excel(excel, sheet_name='Planilha de Reesults')
excel.save() 