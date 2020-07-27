#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:40:46 2020

@author: riccelli
"""
from sklearn.model_selection import ParameterGrid
from sklearn import metrics
import adaline
import knn
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier


def gridsearchAdaline(parametros,trainDivided,validation):
    f1Metric = []
    par = []
    attrs = trainDivided.columns.tolist()[:-1]
    for params in ParameterGrid(parametros):        
        pesos_adaline = adaline.adaline_fit(trainDivided,attrs,params['epochs'],params['alpha'])
        yTeste, yPred =  adaline.adaline_predict(pesos_adaline,validation)
        f1 = metrics.f1_score(yTeste, yPred,average='weighted')
        print(f1)
        f1Metric.append(f1)
        par.append(params)
    return par[f1Metric.index(max(f1Metric))]

def gridsearchKnn(parametros,trainDivided,validation):
    f1Metric = []
    par = []
    for params in ParameterGrid(parametros):        
        yTeste, yPred =  knn.knn_predict(trainDivided,validation,params)
        f1 = metrics.f1_score(yTeste, yPred,average='weighted')
        print(f1)
        f1Metric.append(f1)
        par.append(params)
    return par[f1Metric.index(max(f1Metric))]

def gridsearchRF(parametros,xTrain,yTrain,Xval,yVal):
    f1Metric = []
    par = []
    for params in ParameterGrid(parametros):
        rf = RandomForestClassifier(n_estimators=params['n_estimators'], criterion=params['criterion'])
        rf.fit(xTrain,yTrain)
        pred = rf.predict(Xval)
        f1 = metrics.f1_score(yVal, pred,average='weighted')
        print(f1)
        f1Metric.append(f1)
        par.append(params)
    return par[f1Metric.index(max(f1Metric))]

def gridsearchSVM(parametros,xTrain,yTrain,Xval,yVal):
    f1Metric = []
    par = []
    for params in ParameterGrid(parametros):
        svm = SVC(kernel=params['kernel'], C=params['C'])
        svm.fit(xTrain, yTrain)
        y_pred = svm.predict(Xval)
        f1 = metrics.f1_score(yVal, y_pred,average='weighted')
        print(f1)
        f1Metric.append(f1)
        par.append(params)
    return par[f1Metric.index(max(f1Metric))]

def gridsearchAdaBoost(parametros,xTrain,yTrain,Xval,yVal):
    f1Metric = []
    par = []
    for params in ParameterGrid(parametros):
        clf = AdaBoostClassifier(n_estimators=params['n_estimators'],learning_rate=params['learning_rate'])
        clf.fit(xTrain,yTrain)
        pred = clf.predict(Xval)
        f1 = metrics.f1_score(yVal, pred,average='weighted')
        print(f1)
        f1Metric.append(f1)
        par.append(params)
    return par[f1Metric.index(max(f1Metric))]