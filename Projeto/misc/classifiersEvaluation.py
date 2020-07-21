import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import classification_report
from sklearn import metrics
import timeit
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import RepeatedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

###############################################################################
#                          SCRIPT  DE INICIALIZAÇÃO
###############################################################################
numberOfFolds = 2
numberOfRepeats = 5
random_state = 2
classifier = 'SVM'
normalization = 'MinMax'
metricAverage = 'weighted'

##############################################################################
#                          Parâmetros dos classificadores
##############################################################################

# Definindo qual método de normalização será utilizado
if normalization == 'MinMax':
    scaler = MinMaxScaler(feature_range=(0, 1))
elif normalization == 'StandardScaler':
    scaler = StandardScaler()
else:
    print("Erro")


# Definindo classificadores e planilhas para salvar os resultados
if classifier == 'KNN':
    model = KNeighborsClassifier(n_neighbors=3)
    nomeExcel = 'KNN.xlsx'
elif(classifier == 'NC'):
    model = NearestCentroid()
    nomeExcel = 'NearestCentroid.xlsx'
elif(classifier == 'NB'):
    model = GaussianNB()
    nomeExcel = 'NaiveBayes.xlsx'
elif(classifier == 'RF'):
    model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=random_state)
    nomeExcel = 'RandomForest.xlsx'
elif(classifier == 'SVM'):
    model = svm = SVC(kernel='rbf', C=1.0, random_state=random_state)
    nomeExcel = 'SVM.xlsx'
else:
    print("ERRO")
# Criando planilha de resultados
excel = pd.ExcelWriter(nomeExcel, engine='xlsxwriter')


print("LENDO DATASET PREPROCESSADO")
df = pd.read_csv('/media/riccelli/1CBBB19519DBB1D2/Bruno/Doutorado/CIC2017/csvs/MachineLearningCVE/CICIDSFULL.csv')
colunasTotais = df.columns
colunasFeatures  = colunasTotais.drop(['label'])
colunasToScale  = colunasTotais.drop(['destination_port','label'])

# Transformando variável categórica em categorias (nodificar)
label_encoder = preprocessing.LabelEncoder()
label_encoder.fit(df['destination_port'])
# View the label {France,China,...}
list(label_encoder.classes_)
# Transform Column to Numerical Var
df['destination_port'] = label_encoder.transform(df['destination_port']) 

label_encoder = preprocessing.LabelEncoder()
label_encoder.fit(df['label'])
# View the label {France,China,...}
list(label_encoder.classes_)
# Transform Column to Numerical Var
df['label'] = label_encoder.transform(df['label']) 

# Separando porção das features para realizar a normalização e separando labels
XToScale = df.iloc[:,0:69]
Y = df.iloc[:,69] 
del df

XToScale =  pd.DataFrame(scaler.fit_transform(XToScale),columns=colunasFeatures)

X = XToScale

X['destination_port'] = X['destination_port'].astype('category')
Y= Y.astype('category')
del XToScale

rkf = RepeatedKFold(n_splits=numberOfFolds, n_repeats=numberOfRepeats, random_state=2652124)

rkf.get_n_splits(X, Y)
print(rkf)  
acc = np.zeros((1,numberOfFolds*numberOfRepeats))
f1 = np.zeros((1,numberOfFolds*numberOfRepeats))
pr = np.zeros((1,numberOfFolds*numberOfRepeats))
rc = np.zeros((1,numberOfFolds*numberOfRepeats))
tim = np.zeros((1,numberOfFolds*numberOfRepeats))
rod = 0;
models = []
classReports = []

for train_index, test_index in rkf.split(X, Y):
    X_train, X_test = X.iloc[train_index,:], X.iloc[test_index,:]
    y_train, y_test = Y[train_index], Y[test_index]
    print("classes de treinamento",set(y_train))
    print("classes de teste",set(y_test))
    print("iniciando o treinamento")
    start = timeit.default_timer()
    # Treinamento
    model.fit(X_train, y_train)
    # Teste
    y_pred = model.predict(X_test)
    end = timeit.default_timer()
    print(end - start)
    print("segundos")    
    classReport = classification_report(y_test,y_pred)
    print(classReport)
    acc[:,rod] = metrics.accuracy_score(y_test, y_pred)
    f1[:,rod] = metrics.f1_score(y_test, y_pred,average=metricAverage)
    pr[:,rod] = metrics.precision_score(y_test, y_pred,average=metricAverage)
    rc[:,rod] = metrics.recall_score(y_test, y_pred,average=metricAverage)
    tim[:,rod] = end - start        
    rod = rod + 1
    #models.append(model)
    classReports.append(classReport)
results = [acc,f1,pr,rc,tim]


print("acc", np.mean(acc))
print("precision", np.mean(pr))
print("f1", np.mean(f1))
print("recall", np.mean(rc))
print("mean time", np.mean(tim))

print("std acc", np.std(acc))
print("std precision", np.std(pr))
print("std f1", np.std(f1))
print("std recall", np.std(rc))
print("std time", np.std(tim))

# Salvando Métricas no arquivo xlsx
metrics = {'Tempo':[tim], 
            'Accuracy':[acc],
            'F1':[f1],
            'Precision':[pr],
            'Recal':[rc]}
Dados = pd.DataFrame(metrics)
Dados.to_excel(excel, sheet_name='Planilha de Dados')
excel.save()
