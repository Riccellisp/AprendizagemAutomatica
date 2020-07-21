#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:36:03 2020

@author: riccelli
"""

import pandas as pd
from sklearn.feature_extraction import FeatureHasher
from sklearn.preprocessing import OneHotEncoder

def getIndexes(dfObj, value):
    
    """
      Encontra valores dentro de colunas de um dataframe

      Parameters: 
          dfObj (DataFrame): dataframe com a coluna desejada
          value (string): string a ser encontrada na feature
      
      Returns: 
          List: Lista das posições encontradas
      
    """
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

def converterNumericalEnconding(df,column):
    """
      Converte feature categórica em números
      Parameters: 
          dfObj (DataFrame): dataframe      
          column (string): nome da coluna
      Returns: 
         df (DataFrame): DataFrame
      
    """
    df[column] = df[column].astype('category')
    df[column] = df[column].cat.codes
    return df

def mostrarQuantitativoCategorias(df,column):
    """
      Retorna numero de categorias de uma feature
      Parameters: 
          df (DataFrame): dataframe      
          column (string): nome da coluna
      Returns: 
         categorias (list): List
    """
    categorias = df[column].value_counts()
    return categorias

def hashingFeatureEncoding(df,column,n_features_out):
    """
      Retorna dataframe com feature categorica codificada
      Parameters: 
          df (DataFrame): dataframe      
          column (string): nome da coluna
          n_features_out (int): numero de features na saida
      Returns: 
          df (DataFrame): DataFrame
    """    
    df[column] = pd.DataFrame(df[column]).applymap(str)
    hasher = FeatureHasher(n_features=n_features_out, input_type="string")
    feature = hasher.transform(df[column])
    HashedFeatures = pd.DataFrame(feature.toarray(),columns=['column_0','column_1','column_2','column_3','column_4','column_5','column_6','column_7','column_8','column_9','column_10','column_11','column_12','column_13','column_14','column_15','column_16','column_17','column_18','column_19'])
    HashedFeatures.reset_index(drop=True, inplace=True)
    df.reset_index(drop=True, inplace=True)    
    print('tamanhoHashed',HashedFeatures.shape)
    df = HashedFeatures.join(df)    
    df = df.drop([column],axis=1)
    print('tamanho df dropando  destt_port',df.shape)
    return df

def oneHotEncoding(df,column):
    enc = OneHotEncoder(handle_unknown='ignore')
    df_enc = pd.DataFrame(enc.fit_transform(df[[column]]).toarray(),columns=['label_0','label_1','label_2','label_3','label_4','label_5','label_6','label_7','label_8','label_9','label_10','label_11','label_12','label_13','label_14'])
    df = df.join(df_enc)
    df.drop([column],axis=1,inplace=True) 
    return df

def salvarDataset(df,caminho,nome):
    df.to_csv (caminho+nome+'.csv', index = None, header=True)
    
def binarizarLabel(df):
    df[df['label'] != 0] = 1
    return df

