#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 01:35:51 2020

@author: riccelli
"""


import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer 
import numpy as np
from sklearn.feature_extraction import FeatureHasher
from category_encoders.hashing import HashingEncoder


def getIndexes(dfObj, value):
    ''' Get index positions of value in dataframe i.e. dfObj.'''
    listOfPos = list()
    # Get bool dataframe with True at positions where the given value exists
    result = dfObj.isin([value])
    # Get list of columns that contains the value
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    # Iterate over list of columns and fetch the rows indexes where value exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            listOfPos.append((row))
    # Return a list of tuples indicating the positions of value in the dataframe
    return listOfPos

# Lendo os arquivos do dataset
friday_afternoon = pd.read_csv('/home/riccelli/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv',low_memory=False)
friday_afternoon2 = pd.read_csv('/home/riccelli/MachineLearningCVE/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv',low_memory=False)
friday_morning = pd.read_csv('/home/riccelli/MachineLearningCVE/Friday-WorkingHours-Morning.pcap_ISCX.csv',low_memory=False)
monday = pd.read_csv('/home/riccelli/MachineLearningCVE/Monday-WorkingHours.pcap_ISCX.csv',low_memory=False)
thursday_afternoon = pd.read_csv('/home/riccelli/MachineLearningCVE/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv',low_memory=False)
thursday_morning = pd.read_csv('/home/riccelli/MachineLearningCVE/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv',low_memory=False)
tuesday = pd.read_csv('/home/riccelli/MachineLearningCVE/Tuesday-WorkingHours.pcap_ISCX.csv',low_memory=False)
wednesday = pd.read_csv('/home/riccelli/MachineLearningCVE/Wednesday-workingHours.pcap_ISCX.csv',low_memory=False)

df = pd.concat([friday_afternoon,friday_afternoon2,friday_morning,monday,thursday_afternoon,thursday_morning,tuesday,wednesday],ignore_index=True)
del friday_afternoon,friday_afternoon2,friday_morning,monday,thursday_afternoon,thursday_morning,tuesday,wednesday

dfReduced = df.iloc[0:1000,:]
del df
dfReduced.columns = dfReduced.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
# Removendo Strings "Infinity" das colunas que contém essa string
#df.drop(df.loc[(df['flow_bytes/s']=="Infinity")| (df['flow_packets/s']=="Infinity")].index,inplace=True)
listOfPositions = getIndexes(pd.DataFrame(dfReduced['flow_bytes/s']), "Infinity")
dfReduced = dfReduced.drop(listOfPositions)
# Removendo missing values
dfReduced = dfReduced.dropna()

dfReduced['destination_port'] = dfReduced['destination_port'].astype('category')
# transformando categorical em numerical
dfReduced['destination_port'] = dfReduced['destination_port'].cat.codes
destPorts = dfReduced['destination_port'].value_counts()

dfReduced['destination_port'] = pd.DataFrame(dfReduced['destination_port']).applymap(str)
h = FeatureHasher(n_features=20, input_type="string")
f = h.transform(dfReduced['destination_port'])
a = f.toarray()


X = dfReduced.iloc[:,0:78]
y = dfReduced.iloc[:,-1] 

he = HashingEncoder(cols=["destination_port"]).fit(X, y)
data = he.transform(X)
print(data.info())
