#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:27:30 2020

@author: riccelli
"""
import numpy as np
import seaborn as sns
import pandas  as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


def PlotResultsBoxPlot(MetricAll,MetricRamdon,MetricClusterCentroids,MetricNearMiss,metricaStr,caminhoOut):
    """
      Salva boxplots de metricas de diferentes subamostragens
      Parameters: 
          MetricAll (Array): Metrica do dataset completo
          MetricRamdon (Array): Metrica da subamostragem aleatória
          MetricClusterCentroids (Array): Metrica da subamostragem cluster centroids
          MetricNearMiss (Array): Metrica da subamostragem NearMiss1
          metricaStr (string): nome da metrica
          caminhoOut (string): Caminho para salvar
      Returns: 
          plots
    """   
    
    MetricAll = np.round(MetricAll, 3)
    MetricRamdon = np.round(MetricRamdon, 3)
    MetricClusterCentroids = np.round(MetricClusterCentroids, 3)
    MetricNearMiss = np.round(MetricNearMiss, 3)
    Metrics = np.hstack((MetricAll,MetricRamdon,MetricClusterCentroids,MetricNearMiss))
    
    allStr = ['Full' for x in range(len(MetricAll))]
    RamdonStr = ['Random' for x in range(len(MetricAll))]
    ClusterCentroidsStr = ['Cluster Centroids' for x in range(len(MetricAll))] 
    NearMissStr = ['NearMiss1' for x in range(len(MetricAll))]
    
    strs = np.hstack((allStr,RamdonStr,ClusterCentroidsStr,NearMissStr))
    
    df = pd.DataFrame(np.transpose(np.vstack((strs,Metrics))),columns=[metricaStr,'Value'])
    
    df[metricaStr] = df[metricaStr].astype('category')
    df['Value'] = df['Value'].astype(float)
    
    fig, axs = plt.subplots()
    sns.set(style="whitegrid")
    ax = sns.boxplot(x=metricaStr, y="Value",data=df, orient='v',ax=axs,order=["Full", "Random","Cluster Centroids","NearMiss1"])
    plt.savefig(caminhoOut)
    
def PlotResultsBoxPlot2(MetricRamdon,MetricClusterCentroids,MetricNearMiss,metricaStr,caminhoOut):
    """
      Salva boxplots de metricas de diferentes subamostragens
      Parameters: 
          MetricAll (Array): Metrica do dataset completo
          MetricRamdon (Array): Metrica da subamostragem aleatória
          MetricClusterCentroids (Array): Metrica da subamostragem cluster centroids
          MetricNearMiss (Array): Metrica da subamostragem NearMiss1
          metricaStr (string): nome da metrica
          caminhoOut (string): Caminho para salvar
      Returns: 
          plots
    """   
    
    MetricRamdon = np.round(MetricRamdon, 3)
    MetricClusterCentroids = np.round(MetricClusterCentroids, 3)
    MetricNearMiss = np.round(MetricNearMiss, 3)
    Metrics = np.hstack((MetricRamdon,MetricClusterCentroids,MetricNearMiss))
    
    RamdonStr = ['Random' for x in range(len(MetricRamdon))]
    ClusterCentroidsStr = ['Cluster Centroids' for x in range(len(MetricRamdon))] 
    NearMissStr = ['NearMiss1' for x in range(len(MetricRamdon))]
    
    strs = np.hstack((RamdonStr,ClusterCentroidsStr,NearMissStr))
    
    df = pd.DataFrame(np.transpose(np.vstack((strs,Metrics))),columns=[metricaStr,'Value'])
    
    df[metricaStr] = df[metricaStr].astype('category')
    df['Value'] = df['Value'].astype(float)
    
    fig, axs = plt.subplots()
    sns.set(style="whitegrid")
    ax = sns.boxplot(x=metricaStr, y="Value",data=df, orient='v',ax=axs,order=["Random","Cluster Centroids","NearMiss1"])
    y_fmt = mtick.FormatStrFormatter('%0.2f')
    ax.yaxis.set_major_formatter(y_fmt)
    plt.savefig(caminhoOut)    
    
accAllNC = [0.2670472288922090,0.2667903661157250,0.2667614770861770,0.2670785634153270,0.2501267358780280,0.2668106634223580,0.2669056368548170,0.2669352595395810,0.2667925344069870,0.2847291501725570]
accAllNC = np.round(accAllNC, 3)
    
f1AllNC = [0.3582996144417310,0.3579484593775240,0.3580274110433150,0.3582253620389240,0.3435509082883750,0.3580026860076130,0.3580784269923630,0.3581746471928790,0.3579867634385190,0.3735914110526930]
f1AllNC = np.round(f1AllNC, 3)

precisionAllNC = [0.9074060140685790,0.9072151289177510,0.9075077329456940,0.9071154776135320,0.8931729497545500,0.9074778895095240,0.9071035317941470,0.9075229940977070,0.9072561405619640,0.9208868619565790]
precisionAllNC = np.round(precisionAllNC, 3)
    
recallAllNC =  [0.2670472288922090,0.2667903661157250,0.2667614770861770,0.2670785634153270,0.2501267358780280,0.2668106634223580,0.2669056368548170,0.2669352595395810,0.2667925344069870,0.2847291501725570]
recallAllNC = np.round(recallAllNC, 3)
    
#Results CIC2018 NC Random
accRandomNC = [0.4791212839938280,0.4686404771225270,0.4766769521265570,0.4834526907223610,0.4774414534736450,0.4778996937389180,0.4820917862159480,0.4779492021092860,0.4742510419784920,0.4911863587169270]
accRandomNC = np.round(accRandomNC, 3)
    
f1RandomNC = [0.4535829822066130,0.4436643622943630,0.4512801984271920,0.4588958718480180,0.4506790494793540,0.4514694779712110,0.4573036422465460,0.4526214042310620,0.4468870188379810,0.4687204141869350]
f1RandomNC = np.round(f1RandomNC, 3)
    
precisionRandomNC = [0.5432404865679740,0.5250859456197840,0.5458267015353290,0.5327561092313490,0.5263743013167810,0.5411451870600530,0.5721119055982440,0.5419548068921220,0.5282213856105300,0.6000904871587310]
precisionRandomNC = np.round(precisionRandomNC, 3)
    
recallRandomNC  = [0.4791212839938280,0.4686404771225270,0.4766769521265570,0.4834526907223610,0.4774414534736450,0.4778996937389180,0.4820917862159480,0.4779492021092860,0.4742510419784920,0.4911863587169270]
recallRandomNC  = np.round(recallRandomNC, 3)
    
#Results CIC2018 NC Cluster Centroids
accClusterCentroidsNC = [0.8799940129412570,0.8884680037764520,0.8835056531650810,0.8847376056370460,0.8839661961452550,0.8856586915973930,0.8892278996937380,0.8813526147327690,0.8875123770925920,0.8768277799525640]
accClusterCentroidsNC = np.round(accClusterCentroidsNC, 3)
    
f1ClusterCentroidsNC = [0.8739150346079610,0.8817469651110090,0.8802699031525520,0.8781783347125530,0.8778476398250090,0.8793227592663190,0.8825918950995680,0.8749915133709430,0.8808570843811670,0.8740589199405260]
f1ClusterCentroidsNC = np.round(f1ClusterCentroidsNC, 3)
    
precisionClusterCentroidsNC =[0.8833410418436790,0.8954786249768310,0.8972017082822910,0.8890990673258420,0.8932042047144000,0.8892546309058090,0.8953462496477510,0.8845042088684710,0.8933539181982650,0.8906166947528360]
precisionClusterCentroidsNC = np.round(precisionClusterCentroidsNC, 3)
    
recallClusterCentroidsNC  = [0.8799940129412570,0.8884680037764520,0.8835056531650810,0.8847376056370460,0.8839661961452550,0.8856586915973930,0.8892278996937380,0.8813526147327690,0.8875123770925920,0.8768277799525640]
recallClusterCentroidsNC  = np.round(recallClusterCentroidsNC, 3)
    
#Results CIC2018 NC NearMiss
accNearMissNC = [0.8650378796601190,0.8680083818822390,0.8671333502199090,0.8658898841734400,0.8661316692380310,0.8668915651553180,0.8666728072397350,0.8662352914085700,0.8672369723904480,0.8657977755774050]
accNearMissNC = np.round(accNearMissNC, 3)
    
f1NearMissNC =[0.8662282542149190,0.8692188946409150,0.8683182603054020,0.8671171323211630,0.8673558415289700,0.8680751985136170,0.8675121544204270,0.8675224196302290,0.8684546547629910,0.8669888686477370]
f1NearMissNC = np.round(f1NearMissNC, 3)
    
precisionNearMissNC = [0.8876340457410830,0.8898755282388160,0.8892627102819880,0.8882843324499250,0.8884190803719900,0.8890632281985430,0.8878791907881530,0.8888245106001110,0.8891049076410120,0.888421773245457]
precisionNearMissNC = np.round(precisionNearMissNC, 3)
    
recallNearMissNC  =[0.8650378796601190,0.8680083818822390,0.8671333502199090,0.8658898841734400,0.8661316692380310,0.8668915651553180,0.8666728072397350,0.8662352914085700,0.8672369723904480,0.8657977755774050]
recallNearMissNC  = np.round(recallNearMissNC, 3)
    
#Results CIC2018 NB All 
accAllNB = [0.8008066588852180,0.8007632276385730,0.8009119358663870,0.8006588065550510,0.8007814706644040,0.8007900054105770,0.8006461145457570,0.8009252392728420,0.8007639856373340,0.8008077349856480]
accAllNB = np.round(accAllNB, 3)

f1AllNB= [0.8160675358688300,0.8159852074765790,0.8162212323273800,0.8158332204342550,0.8160162063872270,0.8160397700892000,0.8158214164010460,0.8162343496155830,0.8160727629977160,0.8159836242783840]
f1AllNB = np.round(f1AllNB, 3)

precisionAllNB = [0.8651796656537000,0.8650096836774930,0.8653665713972260,0.8648122125655710,0.8650508586013920,0.8651373853513290,0.8649110988796750,0.8652791409792280,0.8652341527211710,0.8649477972509950]
precisionAllNB = np.round(precisionAllNB, 3)

recallAllNB  = [0.8008066588852180,0.8007632276385730,0.8009119358663870,0.8006588065550510,0.8007814706644040,0.8007900054105770,0.8006461145457570,0.8009252392728420,0.8007639856373340,0.8008077349856480]
recallAllNB = np.round(recallAllNB, 3)

#Results CIC2018 NB Random
accRandomNB = [0.7675109954636510,0.7692357289244010,0.7687245262164090,0.7659497547608630,0.7650033389366060,0.7697872291431590,0.7666163907246640,0.7664874386902150,0.7666670504524830,0.7656768830451100]
accRandomNB = np.round(accRandomNB, 3)

f1RandomNB = [0.7634270408671060,0.7740376163472300,0.7713646528459520,0.7619994289136930,0.7667946068113610,0.7752189163113510,0.7705664422256420,0.7641317484965720,0.7708108254288420,0.7662169307285120]
f1RandomNB = np.round(f1RandomNB, 3)

precisionRandomNB = [0.8646545179439530,0.8516677033299530,0.8581025711578600,0.8656342469983140,0.8492536398369280,0.8545418550296620,0.8584221321117120,0.8630067809628670,0.8574082510863860,0.8591455143973570]
precisionRandomNB = np.round(precisionRandomNB, 3)

recallRandomNB  = [0.7675109954636510,0.7692357289244010,0.7687245262164090,0.7659497547608630,0.7650033389366060,0.7697872291431590,0.7666163907246640,0.7664874386902150,0.7666670504524830,0.7656768830451100]
recallRandomNB = np.round(recallRandomNB, 3)


#Results CIC2018 NB Cluster Centroids
accClusterCentroidsNB = [0.9846524051857130,0.9701683284592530,0.9830405047551060,0.9815667672185500,0.9838579685449140,0.9850323531443570,0.9813249821539590,0.9849862988463390,0.9864370092338860,0.9718032560388690] 
accClusterCentroidsNB = np.round(accClusterCentroidsNB, 3)

f1ClusterCentroidsNB = [0.9861262225658000,0.9723426256238200,0.9852362830860180,0.9846967137088290,0.9859789981659270,0.9865704844856370,0.9845828102552540,0.9864525500513590,0.9873848656406980,0.9744278771603710]
f1ClusterCentroidsNB = np.round(f1ClusterCentroidsNB, 3)

precisionClusterCentroidsNB = [0.9880865838725420,0.9765994468902990,0.9881653546855110,0.9888053126013150,0.9888188534115390,0.9886095150654630,0.9889020088175290,0.9886249566919620,0.9887348214211300,0.9785073322667870]
precisionClusterCentroidsNB = np.round(precisionClusterCentroidsNB, 3)

recallClusterCentroidsNB  = [0.9846524051857130,0.9701683284592530,0.9830405047551060,0.9815667672185500,0.9838579685449140,0.9850323531443570,0.9813249821539590,0.9849862988463390,0.9864370092338860,0.9718032560388690]
recallClusterCentroidsNB = np.round(recallClusterCentroidsNB, 3)

 #Results CIC2018 NB NearMiss
accNearMissNB = [0.9131761346627670,0.9119902364888200,0.9119211550417940,0.9134179197273580,0.9048633338706330,0.9152485780735480,0.9118866143182810,0.9133142975568190,0.9150067930089570,0.9032284062910170]
accNearMissNB = np.round(accNearMissNB, 3)

f1NearMissNB = [0.9064828423465240,0.9052162879605360,0.9048130805766320,0.9070017029002850,0.8981476982674400,0.9084349602901340,0.9049600942641480,0.9067569886419890,0.9083243284388150,0.8964026279274330]
f1NearMissNB = np.round(f1NearMissNB, 3)

precisionNearMissNB = [0.9209227445757370,0.9215434408280080,0.9198346463367030,0.9228339652353970,0.9146529866928740,0.9241811587777770,0.9206647200866010,0.9217226436088520,0.9231406490953710,0.9140767925555940]
precisionNearMissNB = np.round(precisionNearMissNB, 3)

recallNearMissNB  = [0.9131761346627670,0.9119902364888200,0.9119211550417940,0.9134179197273580,0.9048633338706330,0.9152485780735480,0.9118866143182810,0.9133142975568190,0.9150067930089570,0.9032284062910170]
recallNearMissNB = np.round(recallNearMissNB, 3)

#Results CIC2018 RF All
accAllRF = [0.8320453104301480,0.8320790372229370,0.8323348526965940,0.8317894949210880,0.8321146391738450,0.8320097084707630,0.8319647325781260,0.8321596150848110,0.8321016782446890,0.8320226694015040]
accAllRF = np.round(accAllRF, 3)

f1AllRF = [0.7557666774587100,0.7558140343500910,0.7561732572994670,0.7554075026408900,0.7558640250149950,0.7557166883874630,0.7556535384605450,0.7559271793533620,0.7558458257633390,0.7557348868659540]
f1AllRF = np.round(f1AllRF, 3)

precisionAllRF = [0.6922993986088020,0.6923555241858500,0.6927813070134610,0.6918737638610780,0.6924147727274190,0.6922401549896040,0.6921653162537940,0.6924896249781010,0.6923932029376280,0.6922617223980050]
precisionAllRF = np.round(precisionAllRF, 3)

recallAllRF  = [0.8320453104301480,0.8320790372229370,0.8323348526965940,0.8317894949210880,0.8321146391738450,0.8320097084707630,0.8319647325781260,0.8321596150848110,0.8321016782446890,0.8320226694015040]
recallAllRF = np.round(recallAllRF, 3)


#Results CIC2018 RF Random
accRandomRF = [0.7394109655283570,0.7408190756902380,0.7442996292629000,0.7389746010546430,0.7359891311856670,0.7456236903309000,0.7464215810440500,0.7357761300573370,0.7402606673267780,0.7332753816749940]
accRandomRF = np.round(accRandomRF, 3)

f1RandomRF = [0.6852854826013830,0.6848878324622370,0.6912320961881320,0.6827385948738000,0.6782566651965930,0.6934250408763390,0.6944307853166560,0.6772870002766940,0.6843802924184340,0.6746771852278200]
f1RandomRF = np.round(f1RandomRF, 3)

precisionRandomRF = [0.7390940694852150,0.7369770879686780,0.7477720213517100,0.7343286126031900,0.7210431740172080,0.7521299737974410,0.7491221797597290,0.7233078054018390,0.7364818252579210,0.7267394693036140]
precisionRandomRF = np.round(precisionRandomRF, 3)

recallRandomRF  = [0.7394109655283570,0.7408190756902380,0.7442996292629000,0.7389746010546430,0.7359891311856670,0.7456236903309000,0.7464215810440500,0.7357761300573370,0.7402606673267780,0.7332753816749940]
recallRandomRF = np.round(recallRandomRF, 3)


#Results CIC2018 RF Cluster Centroids
accClusterCentroidsRF = [0.8503350450180760,0.8501278006769980,0.8514748888940060,0.8439910654661840,0.8434153867409670,0.8596495267920870,0.8508071015727540,0.8531213300481260,0.8524420291523700,0.8415617012457680]
accClusterCentroidsRF = np.round(accClusterCentroidsRF, 3)

f1ClusterCentroidsRF = [0.8072653579034350,0.8066143295027740,0.8084807130258280,0.7975004650959410,0.7969688159065510,0.8226631039687710,0.8076269562598390,0.8114578773142180,0.8099502464168140,0.7935191855823100]
f1ClusterCentroidsRF = np.round(f1ClusterCentroidsRF, 3)

precisioRFlusterCentroidsRF =[0.8218770144560870,0.8213392764127770,0.8225064839796230,0.8195198810185260,0.8202592102108330,0.8895107206315250,0.8231730327843620,0.8204754281937490,0.8219887267829460,0.8189456084982630]
precisioRFlusterCentroidsRF = np.round(precisioRFlusterCentroidsRF, 3)

recallClusterCentroidsRF  = [0.8503350450180760,0.8501278006769980,0.8514748888940060,0.8439910654661840,0.8434153867409670,0.8596495267920870,0.8508071015727540,0.8531213300481260,0.8524420291523700,0.8415617012457680]
recallClusterCentroidsRF = np.round(recallClusterCentroidsRF, 3)

#Results CIC2018 RF NearMiss
accNearMissRF = [0.8340778778179470,0.8365993506343970,0.8556428028645770,0.8342045271374950,0.8500817463789800,0.8353789117369370,0.8355516153545020,0.8497363391438500,0.8513136988509450,0.8496096898243020]
accNearMissRF = np.round(accNearMissRF, 3)

f1NearMissRF =[0.8036129841896050,0.8063709911133490,0.8249415453657800,0.8030460894691950,0.8191495765201810,0.8048080675024180,0.8052457050518880,0.8187688007040780,0.8208696643718570,0.8189833945648600]
f1NearMissRF = np.round(f1NearMissRF, 3)

precisionNearMissRF = [0.8457307309640310,0.8472871775066180,0.8677222125460910,0.8454464942232310,0.8619476302164360,0.8464236548058480,0.8461715121254370,0.8631896780524120,0.8636247405026350,0.8623716466718150]
precisionNearMissRF = np.round(precisionNearMissRF, 3)

recallNearMissRF  =[0.8340778778179470,0.8365993506343970,0.8556428028645770,0.8342045271374950,0.8500817463789800,0.8353789117369370,0.8355516153545020,0.8497363391438500,0.8513136988509450,0.8496096898243020]
recallNearMissRF = np.round(recallNearMissRF, 3)
    
#Results CIC2018 KNN Random
accRandomKNN = [0.8529670481497680,0.8533953531213290,0.8555645105579470,0.8578672254588150,0.8533297257466550,0.8590151288368980,0.8556900085200450,0.8528438529025720,0.8585292559928150,0.8529624427199660]
accRandomKNN = np.round(accRandomKNN, 3)

f1RandomKNN = [0.8222726705773910,0.8239268112051480,0.8274287189864540,0.8378484727398710,0.8226322681717800,0.8366307280359770,0.8272585277791030,0.8221456552326400,0.8323983097089190,0.8226292431807750]
f1RandomKNN = np.round(f1RandomKNN, 3)

precisionRandomKNN = [0.8421661731126970,0.8498556065481650,0.8376998783737170,0.8447374559369000,0.8363634758340550,0.8426869282813220,0.8211423655271090,0.8297023447885860,0.8443951835709900,0.8288186391873420]
precisionRandomKNN = np.round(precisionRandomKNN, 3)

recallRandomKNN  = [0.8529670481497680,0.8533953531213290,0.8555645105579470,0.8578672254588150,0.8533297257466550,0.8590151288368980,0.8556900085200450,0.8528438529025720,0.8585292559928150,0.8529624427199660]
recallRandomKNN = np.round(recallRandomKNN, 3)


#Results CIC2018 KNN Cluster Centroids
accClusterCentroidsKNN = [0.9962350611370800,0.9964883597761760,0.9964423054781580,0.9968107398622970,0.9963041425841060,0.9965804683722100,0.9964307919036540,0.9965574412232020,0.9965229004996890,0.9962350611370800]
accClusterCentroidsKNN = np.round(accClusterCentroidsKNN, 3)

f1ClusterCentroidsKNN = [0.9962242946793990,0.9964427335061070,0.9963989465244820,0.9968115996559010,0.9962601275098420,0.9965509327756220,0.9964133709195260,0.9965368087804630,0.9964716675889370,0.9962596054601260]
f1ClusterCentroidsKNN = np.round(f1ClusterCentroidsKNN, 3)

precisionClusterCentroidsKNN = [0.9962372070951660,0.9964456215820350,0.9964598165271800,0.9968278685327620,0.9962812739452520,0.9965826638104850,0.9964126204240210,0.9965466403240270,0.9965302626361040,0.9962981328596700]
precisionClusterCentroidsKNN = np.round(precisionClusterCentroidsKNN, 3)

recallClusterCentroidsKNN  = [0.9962350611370800,0.9964883597761760,0.9964423054781580,0.9968107398622970,0.9963041425841060,0.9965804683722100,0.9964307919036540,0.9965574412232020,0.9965229004996890,0.9962350611370800]
recallClusterCentroidsKNN = np.round(recallClusterCentroidsKNN, 3)

#Results CIC2018 KNN NearMiss
accNearMissKNN = [0.9385059985723160,0.9077302139222140,0.9041034379533470,0.9077992953692400,0.9048978745941460,0.9375733990374650,0.9059110691505280,0.9371128560572910,0.9439749464618780,0.9061643677896230]
accNearMissKNN = np.round(accNearMissKNN, 3)

f1NearMissKNN = [0.9368311148743250,0.8772556059310540,0.8810638567762950,0.8772621604696140,0.8738623718946540,0.9344053955175510,0.8751592491289260,0.9330585776079740,0.9424104186015840,0.8753161860165870]
f1NearMissKNN = np.round(f1NearMissKNN, 3)

precisionNearMissKNN = [0.9426826277851860,0.9453651958038790,0.8983472378771050,0.8618676431312130,0.8585403799337610,0.9440566130689060,0.9101788456439750,0.9466709560119710,0.9482695285752630,0.9295245144131850]
precisionNearMissKNN = np.round(precisionNearMissKNN, 3)

recallNearMissKNN  = [0.9385059985723160,0.9077302139222140,0.9041034379533470,0.9077992953692400,0.9048978745941460,0.9375733990374650,0.9059110691505280,0.9371128560572910,0.9439749464618780,0.9061643677896230]
recallNearMissKNN = np.round(recallNearMissKNN, 3)

#Results CIC2018 SVM Random
accRandomSVM = [0.811913095539641,0.810730651438045,0.811003523153798,0.810097404840306,0.810437055288184,0.811156653694706,0.811715062058166,0.810814700531927,0.810493471803255,0.809832592626706]
accRandomSVM = np.round(accRandomSVM, 3)

f1RandomSVM = [0.798843323063073,0.798074573895639,0.798316061114699,0.796920396258479,0.797259219957399,0.798009441656055,0.799148219429761,0.798044788764396,0.797626799075582,0.796320964365735]
f1RandomSVM = np.round(f1RandomSVM, 3)

precisionRandomSVM = [0.843955740487579,0.841576280155723,0.841687663458994,0.841585048368238,0.842164517191440,0.842624793687135,0.843243152603648,0.842739455930962,0.841686215634470,0.842369147349385]
precisionRandomSVM = np.round(precisionRandomSVM, 3)

recallRandomSVM  = [0.811913095539641,0.810730651438045,0.811003523153798,0.810097404840306,0.810437055288184,0.811156653694706,0.811715062058166,0.810814700531927,0.810493471803255,0.809832592626706]
recallRandomSVM  =np.round(recallRandomSVM, 3)

#Results CIC2018 SVM Cluster Centroids
accClusterCentroidsSVM = [0.969396918967462,0.971112441568609,0.971918391783913,0.970260437055288,0.971100927994105,0.970156814884749,0.971054873696087,0.970398599949340,0.969949570543671,0.971008819398070]
accClusterCentroidsSVM = np.round(accClusterCentroidsSVM, 3)

f1ClusterCentroidsSVM = [0.968158861081169,0.970021083232801,0.970906759969250,0.969009226403854,0.969905432946306,0.968993336167312,0.969967810420753,0.969149931817169,0.968715988837992,0.969869147345591]
f1ClusterCentroidsSVM =np.round(f1ClusterCentroidsSVM, 3)

precisioSVMlusterCentroidsSVM =[0.969364809794403,0.971453645530839,0.972101503835049,0.970518348358196,0.971371617376496,0.970309070368199,0.971404683641797,0.970518357685004,0.970090472253306,0.971339297654209]
precisioSVMlusterCentroidsSVM =np.round(precisioSVMlusterCentroidsSVM, 3)

recallClusterCentroidsSVM  = [0.969396918967462,0.971112441568609,0.971918391783913,0.970260437055288,0.971100927994105,0.970156814884749,0.971054873696087,0.970398599949340,0.969949570543671,0.971008819398070]
recallClusterCentroidsSVM  = np.round(recallClusterCentroidsSVM, 3)

#Results CIC2018 SVM NearMiss
accNearMissSVM = [0.84754875999,0.84850438667,0.84773297718,0.84802081654,0.84703064914,0.84825108803,0.84855044097,0.84864254957,0.84947152693,0.84756027356]
accNearMissSVM =np.round(accNearMissSVM, 3)

f1NearMissSVM =[0.81748106539,0.81853476190,0.81755434714,0.81811601981,0.81681559061,0.81834547690,0.81837495909,0.81889196520,0.81966871167,0.81741596578]
f1NearMissSVM =np.round(f1NearMissSVM, 3)

precisionNearMissSVM = [0.81636417077,0.81732065673,0.81634511748,0.81704596707,0.81563848877,0.81728593351,0.81684096460,0.81798970552,0.81832822611,0.81635244794]
precisionNearMissSVM = np.round(precisionNearMissSVM, 3)

recallNearMissSVM  = [0.84754875999,0.84850438667,0.84773297718,0.84802081654,0.84703064914,0.84825108803,0.84855044097,0.84864254957,0.84947152693,0.84756027356]
recallNearMissSVM = np.round(recallNearMissSVM, 3)

# RESULTADOS DE ACURACIA PARA CLASSIFICADOR NC
caminhoOut = '/home/riccelli/accNCCIC2018.pdf'
PlotResultsBoxPlot(accAllNC,accRandomNC,accClusterCentroidsNC,accNearMissNC,'Accuracy',caminhoOut)
mediasAccNC = [np.mean(accAllNC),np.mean(accRandomNC),np.mean(accClusterCentroidsNC),np.mean(accNearMissNC)]
stdsAccNC = [np.std(accAllNC),np.std(accRandomNC),np.std(accClusterCentroidsNC),np.std(accNearMissNC)]

# RESULTADOS DE F1 PARA CLASSIFICADOR NC
caminhoOut = '/home/riccelli/f1NCCIC2018.pdf'
PlotResultsBoxPlot(f1AllNC,f1RandomNC,f1ClusterCentroidsNC,f1NearMissNC,'F1',caminhoOut)
mediasF1NC = [np.mean(f1AllNC),np.mean(f1RandomNC),np.mean(f1ClusterCentroidsNC),np.mean(f1NearMissNC)]
stdsF1NC = [np.std(f1AllNC),np.std(f1RandomNC),np.std(f1ClusterCentroidsNC),np.std(f1NearMissNC)]

# RESULTADOS DE ACURACIA PARA CLASSIFICADOR NB
caminhoOut = '/home/riccelli/accNBCIC2018.pdf'
PlotResultsBoxPlot(accAllNB,accRandomNB,accClusterCentroidsNB,accNearMissNB,'Accuracy',caminhoOut)
mediasAccNB = [np.mean(accAllNB),np.mean(accRandomNB),np.mean(accClusterCentroidsNB),np.mean(accNearMissNB)]
stdsAccNB = [np.std(accAllNB),np.std(accRandomNB),np.std(accClusterCentroidsNB),np.std(accNearMissNB)]

# RESULTADOS DE F1 PARA CLASSIFICADOR NB
caminhoOut = '/home/riccelli/f1NBCIC2018.pdf'
PlotResultsBoxPlot(f1AllNB,f1RandomNB,f1ClusterCentroidsNB,f1NearMissNB,'F1',caminhoOut)
mediasF1NB = [np.mean(f1AllNB),np.mean(f1RandomNB),np.mean(f1ClusterCentroidsNB),np.mean(f1NearMissNB)]
stdsF1NC = [np.std(f1AllNB),np.std(f1RandomNB),np.std(f1ClusterCentroidsNB),np.std(f1NearMissNB)]

# RESULTADOS DE ACURACIA PARA CLASSIFICADOR RF
caminhoOut = '/home/riccelli/accRFCIC2018.pdf'
PlotResultsBoxPlot(accAllRF,accRandomRF,accClusterCentroidsRF,accNearMissRF,'Accuracy',caminhoOut)
mediasAccRF = [np.mean(accAllRF),np.mean(accRandomRF),np.mean(accClusterCentroidsRF),np.mean(accNearMissRF)]
stdsAccRF = [np.std(accAllRF),np.std(accRandomRF),np.std(accClusterCentroidsRF),np.std(accNearMissRF)]

# RESULTADOS DE F1 PARA CLASSIFICADOR RF
caminhoOut = '/home/riccelli/f1RFCIC2018.pdf'
PlotResultsBoxPlot(f1AllRF,f1RandomRF,f1ClusterCentroidsRF,f1NearMissRF,'F1',caminhoOut)
mediasF1RF = [np.mean(f1AllRF),np.mean(f1RandomRF),np.mean(f1ClusterCentroidsRF),np.mean(f1NearMissRF)]
stdsF1RF = [np.std(f1AllRF),np.std(f1RandomRF),np.std(f1ClusterCentroidsRF),np.std(f1NearMissRF)]

# RESULTADOS DE ACURACIA PARA CLASSIFICADOR KNN
caminhoOut = '/home/riccelli/accKNNCIC2018.pdf'
PlotResultsBoxPlot2(accRandomKNN,accClusterCentroidsKNN,accNearMissKNN,'Accuracy',caminhoOut)
mediasAccKNN = [np.mean(accRandomKNN),np.mean(accClusterCentroidsKNN),np.mean(accNearMissKNN)]
stdsAccKNN = [np.std(accRandomKNN),np.std(accClusterCentroidsKNN),np.std(accNearMissKNN)]

# RESULTADOS DE F1 PARA CLASSIFICADOR KNN
caminhoOut = '/home/riccelli/f1KNNCIC2018.pdf'
PlotResultsBoxPlot2(f1RandomKNN,f1ClusterCentroidsKNN,f1NearMissKNN,'F1',caminhoOut)
mediasF1KNN = [np.mean(f1RandomKNN),np.mean(f1ClusterCentroidsKNN),np.mean(f1NearMissKNN)]
stdsF1KNN = [np.std(f1RandomKNN),np.std(f1ClusterCentroidsKNN),np.std(f1NearMissKNN)]

# RESULTADOS DE ACURACIA PARA CLASSIFICADOR SVM
caminhoOut = '/home/riccelli/accSVMCIC2018.pdf'
PlotResultsBoxPlot2(accRandomSVM,accClusterCentroidsSVM,accNearMissSVM,'Accuracy',caminhoOut)
mediasAccSVM = [np.mean(accRandomSVM),np.mean(accClusterCentroidsSVM),np.mean(accNearMissSVM)]
stdsAccSVM = [np.std(accRandomSVM),np.std(accClusterCentroidsSVM),np.std(accNearMissSVM)]

# RESULTADOS DE F1 PARA CLASSIFICADOR SVM
caminhoOut = '/home/riccelli/f1SVMCIC2018.pdf'
PlotResultsBoxPlot2(f1RandomSVM,f1ClusterCentroidsSVM,f1NearMissSVM,'F1',caminhoOut)
mediasF1SVM = [np.mean(f1RandomSVM),np.mean(f1ClusterCentroidsSVM),np.mean(f1NearMissSVM)]
stdsF1SVM = [np.std(f1RandomSVM),np.std(f1ClusterCentroidsSVM),np.std(f1NearMissSVM)]