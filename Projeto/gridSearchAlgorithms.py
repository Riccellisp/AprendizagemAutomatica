#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:40:46 2020

@author: riccelli
"""
from sklearn.model_selection import ParameterGrid
from sklearn import metrics
import adaline

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