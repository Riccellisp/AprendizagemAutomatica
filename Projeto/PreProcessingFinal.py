
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer 
import numpy as np
from sklearn.feature_extraction import FeatureHasher
from category_encoders.hashing import HashingEncoder
from os import listdir
from sklearn.preprocessing import OneHotEncoder
from imblearn.under_sampling import RandomUnderSampler

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

def leituraConcat(caminho,low_memoryBoolean):   
    """
      Busca os arquivos do dataset em uma pasta, concatena todos os arquivos e
      ajusta nomes das colunas para minúsculo
      Parameters: 
          caminho (string): pasta onde os arquivos do dataset estão
          low_memoryBoolean (boolean): True leitura consumindo menos memória, False c.c
      
      Returns: 
          DataFrame:dataframe concatenado com colunas padronizadas
      
    """
    lista_arquivos = [arq for arq in listdir(caminho)]
    for i in range(len(lista_arquivos)):
        if i==0:
            df = pd.read_csv(caminho + lista_arquivos[i],low_memory=low_memoryBoolean)
        else:
            df_tmp = pd.read_csv(caminho + lista_arquivos[i],low_memory=low_memoryBoolean)            
            df = pd.concat([df, df_tmp],ignore_index=True)
        #df.append(arquivo)    
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    return df

def removeInfinityNa(df):
    """
      Remove string Infinity e valores Na
      Parameters: 
          dfObj (DataFrame): coluna do dataframe      
      
      Returns: 
         df (DataFrame): DataFrame
      
    """
    listOfPositions = getIndexes(pd.DataFrame(df['flow_packets/s']), "Infinity")
    df = df.drop(index = listOfPositions, axis=0)
    df = df.dropna()
    return df

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

def salvarDataset(df,caminho,nome,extensao):
    df.to_csv (caminho+nome+extensao, index = None, header=True)
    
def binarizarLabel(df):
    df[df['label'] != 0] = 1
    return df

def RandomUnderSampling(df):
    #sizes = []
    #for i in len(categoriesCounts):
    #    size =  (categoriesCounts[i] * DesiredSize)/len(df)
    #    sizes.append(size)
    size0 = 80315
    size1 = 1956
    size2 = 5647
    size3 = 10293
    size4 = 5647
    size5 = 5499
    size6 = 5796
    size7 = 7935
    size8 = 11
    size9 = 36
    size10 = 5647
    size11 = 5897
    size12 = 1507
    size13 = 21
    size14 = 652
    allSizes = size0 + size1 + size2+ size3+ size4+ size5+ size6+ size7+ size8+ size9+ size10+ size11+ size12+ size13+ size14
    print(allSizes)
    ##allSizes =  size1 + size3+ size5+ size6+ size7+ size8+ size9+ size11+ size12+ size13+ size14

    strategy = {0:size0, 1:size1, 2:size2, 3:size3, 4:size4, 5:size5, 6:size6, 7:size7, 8:size8, 9:size9, 10:size10, 11:size11, 12:size12, 13:size13, 14:size14}
    ros = RandomUnderSampler( sampling_strategy=strategy, random_state=7)
    X_under, y_under = ros.fit_resample(df, df['label'])
    
    X_under.reset_index(drop=True, inplace=True)    
    y_under.reset_index(drop=True, inplace=True)    
    
    #df2 = pd.concat([X_under,y_under],axis=1)
    return X_under 

