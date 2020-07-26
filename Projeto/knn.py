#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import math

# Euclidean Distance
#distance = lambda a, b: np.sqrt(sum((a - b)**2))

# Manhattan Distance:
#distance = lambda a, b: sum(np.abs(a - b))

# Minkowski Distance:
#distance = lambda a, b, p: math.pow(sum(np.abs(np.array(a))), (1.0/p))

def __knn_model(df_train, X, k,distanceMetric):
    
  if distanceMetric == 'euclidean':
      distance = lambda a, b: np.sqrt(sum((a - b)**2))
  elif distanceMetric == 'manhatthan':
      distance = lambda a, b: sum(np.abs(a - b))

  aux, votes = [], {}
  values = df_train.values.tolist()

  # Calculate distances and sort it
  for val in values:
    attrs, classe = val[:-1], val[-1]

    aux.append((classe, distance(np.array(attrs), X)))
  aux.sort(key = lambda x: x[1])

  # Compute votes and sort it in reverse mode
  for i in range(k):
    classe = aux[i][0]
    if classe not in votes.keys():
      votes[classe] = 0
    votes[classe] += 1
  check_votes = list(votes.items())
  check_votes.sort(key = lambda x: x[1], reverse=True)

  return check_votes[0][0]

def knn_predict(df_train, df_test, params):
  y, yprevs = [], []
  # Pergunta ao classificador as classes das amostras de teste
  for entry in df_test.values.tolist():
    attrs, y_obs = entry[:-1], entry[-1]
    y_prev = __knn_model(df_train, attrs, params['k'], params['distance'])
    y.append(y_obs)
    yprevs.append(y_prev)
  return y, yprevs

"""
    Para usar, basta usar a linha abaixo no codigo
    yTeste, yPred = knn_predict(train, test, k)

    Lembrando que o valor de k é o numero de vizinhos e ele deve ser um hiperparametro
"""
