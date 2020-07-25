import sys
import pandas as pd
import numpy as np
import math
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import random
from sklearn import metrics

def nearest_centroid_fit(df_train, attrs):

    X = df_train.filter(attrs).values.tolist()
    Y = df_train["label"].values.tolist()
    
    dimension = df_train.shape[1]

    classes = list()
    for k in Y:
        classes.append(k)
        classes = list(set(classes))

    centroids = list()
    for class_idx in classes:
        data = df_train[df_train.label == class_idx].values.tolist()  

        i = 0
        mean = list()
        while i < dimension:
            attr = list()
            for k in data:
                attr.append(k[i])
            i += 1

            y = np.mean(attr)
            mean.append(y)

        centroids.append(mean)
        
    return centroids, classes


def nearest_centroid_predict(centroids, classes,test):
    yprevs = []
    y = []
    for val in test.values.tolist():
        x_test, y_obs = [1.0] + val[:-1], val[-1]
        min_dist = sys.maxsize
        class_idx = 0
        obs_class = -1

        for i in centroids:
            dist  = np.sqrt(np.dot(x_test, x_test) - 2 * np.dot(x_test, i) + np.dot(i, i))
            if dist < min_dist:
                min_dist = dist
                obs_class = class_idx
                class_idx +=1
        y_prev = classes[obs_class]

        y.append(y_obs)
        yprevs.append(y_prev)
    return yprevs,y