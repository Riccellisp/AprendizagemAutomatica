
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
from math import sqrt

def CCMUT(X,f):
    cluster_centroid = np.sum(X,axis=0)/X.shape[0]
    euclidean = [None]*X.shape[0]
    for i in range(0,X.shape[0]):
        euclidean[i] = sqrt(sum((cluster_centroid-X[i])**2))
    indices = list(reversed(sorted(range(len(euclidean)), 
    key = lambda j: euclidean[j])))
    X_f = np.delete(X, indices[:int(f/100*X.shape[0])], axis=0)
    return X_f

def ClusterCentroidsUndersampling(Xtrain,Ytrain,colunas):
    colunasx = list(colunas[0:97])
    colunasy = 'label'
    Xtrain = pd.DataFrame(Xtrain,columns=colunasx)
    Ytrain = pd.DataFrame(Ytrain,columns=[colunasy])
    df = pd.concat([Xtrain,Ytrain],axis=1)
    classesCounts = df['label'].value_counts()
    #normal
    df0 = df[df['label'] == 0]
    #ataques
    df1 = df[df['label'] == 1]
    f0=(1-(classesCounts[1]/len(df0)))*100
    #X =df0.iloc[:,0:65] 
    df0Under= pd.DataFrame(CCMUT(df0.values,f0))
    clusterCentroidDatasetUnder = pd.concat([df0Under,df1])
    return np.array(clusterCentroidDatasetUnder.iloc[0:97,:]), np.array(clusterCentroidDatasetUnder.iloc[:,-1])

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

'''
caminho = '/home/riccelli/CIC2017PreProc/CIC2017PreProcBinaryTiny.csv'
df = pd.read_csv(caminho,low_memory=True)

X = np.array(df.iloc[:,0:97])
Y = np.array(df.iloc[:,-1])
colunas = df.columns
del df
skf = StratifiedKFold(n_splits=10)
skf.get_n_splits(X, Y)
print(skf) 
val_perc = 0.5
indexesPerFold = []
f1Metric = []
for train_index, test_index in skf.split(X, Y):
    X_train, X_test = X[train_index,:], X[test_index,:]
    y_train, y_test = Y[train_index], Y[test_index]
    X_train, y_train = ClusterCentroidsUndersampling(X_train, y_train,colunas)

    X_trainDivided, X_val, y_trainDivided, y_val = train_test_split(X_train, y_train, test_size = val_perc,stratify=y_train)
    indexesPerFold.append(train_index)
    
    parametros = {'n_estimators':[1, 5, 10],'learning_rate':[0.1, 1, 2]}
    resultGrid =  gridsearchAdaBoost(parametros,X_trainDivided,y_trainDivided,X_val,y_val)
    clf = AdaBoostClassifier(n_estimators=resultGrid['n_estimators'],learning_rate=resultGrid['learning_rate'])
    clf.fit(X_train,y_train)
    
'''    