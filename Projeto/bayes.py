#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import math

def naive_bayes_fit(df_train, ids_classes, attrs):
  p, pp = [], [[], []]
  
  for id in ids_classes:
    p.append(len(df_train[df_train['label'] == id]) / len(df_train))

  for id in ids_classes:
    data = df_train[df_train['label'] == id]  

    attrs_means, attrs_ests  = [], []
    for attr in attrs:
      x = data[attr].values.tolist()

      # Calculando a média (µk)
      y = np.mean(x)

      # Calculando a Estimador da Matriz de Covariância (Σk)
      estimator = np.dot(np.array(x - y), np.array(x - y).T) / (len(x) - 1)

      attrs_means.append(y)
      attrs_ests.append(estimator)
      
    pp[0].append(attrs_means)
    pp[1].append(attrs_ests)
  
  return p, pp

def naive_bayes_predict(df_test, ids_classes, p, pp):
  D = df_test.shape[1] - 1

  yobss, yprevs = [], []
  total, correct = 0.0, 0.0
  for row in df_test.values.tolist():
    y_obs, y_prev = row[-1], ""

    most_prob = float('-inf')
    # Analisando cada classe
    for k, cand_class in enumerate(ids_classes):
      #x, y = np.matrix(row[0:-1]), np.matrix(pp[0][k])
      x, y = row[0:-1], pp[0][k]

      for d_ in range(D):
        prob = 0.0

        # Calculando o Termo 1
        prob += (math.log(p[k]))

        # Calculando o Termo 2
        if (pp[1][k][d_] != 0):
          prob -= ((D / 2.0) * np.log(2.0 * np.pi * pp[1][k][d_]))

        # Calculando o Termo 3
        sum_d = 0.0
        for d in range(D):
          if (pp[1][k][d] != 0):
            sum_d += (x[d] - y[d])**2 / pp[1][k][d]
        prob -= (0.5 * sum_d)

        if (prob > most_prob):
          y_prev = cand_class
          most_prob = prob

    yobss.append(y_obs)
    yprevs.append(y_prev)

  return yobss, yprevs


"""
    Para usar, basta usar as linhas abaixo no codigo

    p, pp = naive_bayes_fit(train, ids_classes, attrs)
    yTeste, yPred = naive_bayes_predict(test, ids_classes, p, pp)

    Lembrando que os valores de ids_classes são os identificadores das possíveis classes e attrs é a lista com o label de todos os atributos, com exececao daquele daquele relacionado ao Y. Eu faço assim para pegar esses valores:
    ids_classes = pd.unique(train['label']).tolist()
    attrs = train.columns.tolist()[:-1]
"""
