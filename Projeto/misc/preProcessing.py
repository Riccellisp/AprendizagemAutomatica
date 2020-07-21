# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:24:24 2019

@author: riccelli
"""

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

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer 
import numpy as np

# Lendo os arquivos do dataset
friday_afternoon = pd.read_csv('/home/riccelli/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv',low_memory=False)
friday_afternoon2 = pd.read_csv('/home/riccelli/MachineLearningCVE/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv',low_memory=False)
friday_morning = pd.read_csv('/home/riccelli/MachineLearningCVE/Friday-WorkingHours-Morning.pcap_ISCX.csv',low_memory=False)
monday = pd.read_csv('/home/riccelli/MachineLearningCVE/Monday-WorkingHours.pcap_ISCX.csv',low_memory=False)
thursday_afternoon = pd.read_csv('/home/riccelli/MachineLearningCVE/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv',low_memory=False)
thursday_morning = pd.read_csv('/home/riccelli/MachineLearningCVE/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv',low_memory=False)
tuesday = pd.read_csv('/home/riccelli/MachineLearningCVE/Tuesday-WorkingHours.pcap_ISCX.csv',low_memory=False)
wednesday = pd.read_csv('/home/riccelli/MachineLearningCVE/Wednesday-workingHours.pcap_ISCX.csv',low_memory=False)
# Concatenando arquivos lidos em um dataframe
df = pd.concat([friday_afternoon,friday_afternoon2,friday_morning,monday,thursday_afternoon,thursday_morning,tuesday,wednesday],ignore_index=True)
# Ajustando nomes de colunas para minúsculo
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
# Removendo Strings "Infinity" das colunas que contém essa string
#df.drop(df.loc[(df['flow_bytes/s']=="Infinity")| (df['flow_packets/s']=="Infinity")].index,inplace=True)
listOfPositions = getIndexes(pd.DataFrame(df['flow_bytes/s']), "Infinity")
df = df.drop(listOfPositions)
# Removendo missing values
df = df.dropna()
# Convertendo labels em números e convertendo em variável categorica
df.loc[:,df.columns != 'label'] = df.loc[:,df.columns != 'label'].astype('float64')
#Binarizando dataset
#[df['label'] != 0] = 1
print("Convertendo label em numero")
df['label'] = df['label'].astype('category')
# transformando categorical em numerical
df['label'] = df['label'].cat.codes
# Removendo features repletas de zeros e feature repetida ('fwd_header_length.1')
df = df.drop(['bwd_psh_flags', 'bwd_urg_flags', 'fwd_avg_bytes/bulk','fwd_avg_packets/bulk','fwd_avg_bulk_rate','bwd_avg_bytes/bulk','bwd_avg_packets/bulk','bwd_avg_bulk_rate', 'fwd_header_length.1'], axis=1)
del friday_afternoon,friday_afternoon2,friday_morning,monday,thursday_afternoon,thursday_morning,tuesday,wednesday
columnTransformer = ColumnTransformer([('encoder',
                                        OneHotEncoder(), 
                                        [0])], 
                                      remainder='passthrough') 
  
columnTransformer.fit_transform(df) 


    

destPorts = df['destination_port'].value_counts()
onehotencoder = OneHotEncoder(categories='auto')
dest= df['destination_port'].values
ababa= onehotencoder.fit_transform(dest.reshape(1,-1))
# Exportando arquivo CSV com dataset pré-processado
export_csv = df.to_csv (r'/home/riccelli/MachineLearningCVE/CICIDSFULLBinary.csv', index = None, header=True)

