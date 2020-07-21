#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 02:08:53 2020

@author: riccelli
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import random
from sklearn import metrics

"""Passo 2.1: Definir as funções signal (sign) e de embaralhamento (my_shuffle)"""

# Função sigmoide
sign = lambda x: 0 if x < 0 else 1

# Função de embaralhamento
def my_shuffle(X, Y):
  shuffled = random.sample([X[i] + [Y[i]] for i in range(len(X))], len(X))
  return [i[:-1] for i in shuffled], [i[-1] for i in shuffled]

def adaline(df_train, attrs, epoch, alpha):
  X = df_train.filter(attrs).values.tolist()
  Y = df_train["label"].values.tolist()
  w = np.zeros(len(X[0]) + 1)

  loss_history = []

  for _ in range(epoch):
    X, Y = my_shuffle(X, Y)
    for i in range(len(X)):
      xi, yi = np.array([1.0] + X[i]), np.array(Y[i])

      # Passo 1: Calcule a saı́da do modelo
      yi_ = np.dot(w.T, xi)

      # Passo 2: Calcule o erro obtido
      ei = yi - yi_

      # Passo 2: Atualize os pesos pelo algoritmo LMS
      w += (alpha * ei * xi)

    # Obrigado Prof Cesar Lincoln pelo codigo! 
    x_matrix = np.hstack((np.ones((np.array(X).shape[0], 1)), X))
    loss_history.append(np.sum(np.maximum(0, -(np.array(Y) * np.sign(x_matrix @ w)))))

  plt.plot(loss_history)
  return list(w)

data_comp = pd.read_csv("/home/riccelli/AprendizagemAutomatica/Projeto/CIC2017PreProc/CIC2017PreProcBinaryTiny.csv")
data = data_comp.sample(frac = 0.2)
data.head()

min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(data)
data = pd.DataFrame(np_scaled, columns = data.columns)

X = data.filter(data.columns[:-1]).values.tolist()
y = data['label'].values.tolist()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

train = pd.DataFrame([X_train[i] + [y_train[i]] for i in range(len(X_train))] , columns = data.columns)
test = pd.DataFrame([X_test[i] + [y_test[i]] for i in range(len(X_test))] , columns = data.columns)

attrs = train.columns.tolist()[:-1]

x_train = train.filter(attrs).values.tolist()
y_train = train["label"].values.tolist()

#w = adaline(x_train, y_train, 10, 0.01)
w = adaline(train, attrs, 10, 0.01)
print(w)

yprevs = []
y = []
for val in test.values.tolist():
  x_test, y_obs = [1.0] + val[:-1], val[-1]
  y_prev = sign(np.dot(np.array(x_test), np.array(w)))
  y.append(y_obs)
  yprevs.append(y_prev)

f1 = metrics.f1_score(y, yprevs,average='weighted')  
