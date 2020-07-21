import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.neighbors.nearest_centroid import NearestCentroid
import timeit
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import ParameterGrid
from sklearn import metrics

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
    return dict([par,f1Metric])
        
caminho = '/media/riccelli/1CBBB19519DBB1D2/Bruno/Doutorado/Disciplinas/Aprendizagem Automatica/CIC2017PreProcBinary.csv'
df = pd.read_csv(caminho,low_memory=True)
X = np.array(df.iloc[:,0:97])
Y = np.array(df.iloc[:,-1])
del df

skf = StratifiedKFold(n_splits=10)
skf.get_n_splits(X, Y)
print(skf) 
val_perc = 0.2
indexesPerFold = []

for train_index, test_index in skf.split(X, Y):
    X_train, X_test = X[train_index,:], X[test_index,:]
    y_train, y_test = Y[train_index], Y[test_index]
    X_trainDivided, X_val, y_trainDivided, y_val = train_test_split(X_train, y_train, test_size = val_perc,stratify=y_train)
    indexesPerFold.append(train_index)
    parametros = {'n_estimators':[1, 5, 10],'learning_rate':[0.1, 1, 2]}
    resultGrid =  gridsearchAdaBoost(parametros,X_trainDivided,y_trainDivided,X_val,y_val)
    #for params in ParameterGrid(parametros):
     #   clf = AdaBoostClassifier(n_estimators=params['n_estimators'],learning_rate=params['learning_rate'])
     #   clf.fit(X_trainDivided,y_trainDivided)
      #  pred = clf.predict(X_val)
       # f1 = metrics.f1_score(y_val, pred,average='weighted')
        #f1Metric.append(f1)

