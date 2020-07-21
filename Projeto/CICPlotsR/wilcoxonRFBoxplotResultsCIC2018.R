#Results CIC2018 RF All
accAllRF <- c(0.8320453104301480,0.8320790372229370,0.8323348526965940,0.8317894949210880,0.8321146391738450,0.8320097084707630,0.8319647325781260,0.8321596150848110,0.8321016782446890,0.8320226694015040)
accAllRF = round(accAllRF, 3)

f1AllRF <- c(0.7557666774587100,0.7558140343500910,0.7561732572994670,0.7554075026408900,0.7558640250149950,0.7557166883874630,0.7556535384605450,0.7559271793533620,0.7558458257633390,0.7557348868659540)
f1AllRF = round(f1AllRF, 3)

precisionAllRF <- c(0.6922993986088020,0.6923555241858500,0.6927813070134610,0.6918737638610780,0.6924147727274190,0.6922401549896040,0.6921653162537940,0.6924896249781010,0.6923932029376280,0.6922617223980050)
precisionAllRF = round(precisionAllRF, 3)

recallAllRF  <- c(0.8320453104301480,0.8320790372229370,0.8323348526965940,0.8317894949210880,0.8321146391738450,0.8320097084707630,0.8319647325781260,0.8321596150848110,0.8321016782446890,0.8320226694015040)
recallAllRF = round(recallAllRF, 3)

    
#Results CIC2018 RF Random
accRandomRF <- c(0.7394109655283570,0.7408190756902380,0.7442996292629000,0.7389746010546430,0.7359891311856670,0.7456236903309000,0.7464215810440500,0.7357761300573370,0.7402606673267780,0.7332753816749940)
accRandomRF = round(accRandomRF, 3)

f1RandomRF <- c(0.6852854826013830,0.6848878324622370,0.6912320961881320,0.6827385948738000,0.6782566651965930,0.6934250408763390,0.6944307853166560,0.6772870002766940,0.6843802924184340,0.6746771852278200)
f1RandomRF = round(f1RandomRF, 3)

precisionRandomRF <- c(0.7390940694852150,0.7369770879686780,0.7477720213517100,0.7343286126031900,0.7210431740172080,0.7521299737974410,0.7491221797597290,0.7233078054018390,0.7364818252579210,0.7267394693036140)
precisionRandomRF = round(precisionRandomRF, 3)

recallRandomRF  <- c(0.7394109655283570,0.7408190756902380,0.7442996292629000,0.7389746010546430,0.7359891311856670,0.7456236903309000,0.7464215810440500,0.7357761300573370,0.7402606673267780,0.7332753816749940)
recallRandomRF = round(recallRandomRF, 3)


#Results CIC2018 RF Cluster Centroids
accClusterCentroidsRF <- c(0.8503350450180760,0.8501278006769980,0.8514748888940060,0.8439910654661840,0.8434153867409670,0.8596495267920870,0.8508071015727540,0.8531213300481260,0.8524420291523700,0.8415617012457680)
accClusterCentroidsRF = round(accClusterCentroidsRF, 3)

f1ClusterCentroidsRF <- c(0.8072653579034350,0.8066143295027740,0.8084807130258280,0.7975004650959410,0.7969688159065510,0.8226631039687710,0.8076269562598390,0.8114578773142180,0.8099502464168140,0.7935191855823100)
f1ClusterCentroidsRF = round(f1ClusterCentroidsRF, 3)

precisionClusterCentroidsRF <- c(0.8218770144560870,0.8213392764127770,0.8225064839796230,0.8195198810185260,0.8202592102108330,0.8895107206315250,0.8231730327843620,0.8204754281937490,0.8219887267829460,0.8189456084982630)
precisionClusterCentroidsRF = round(precisionClusterCentroidsRF, 3)

recallClusterCentroidsRF  <- c(0.8503350450180760,0.8501278006769980,0.8514748888940060,0.8439910654661840,0.8434153867409670,0.8596495267920870,0.8508071015727540,0.8531213300481260,0.8524420291523700,0.8415617012457680)
recallClusterCentroidsRF = round(recallClusterCentroidsRF, 3)

#Results CIC2018 RF Cluster Centroids
accNearMissRF <- c(0.8340778778179470,0.8365993506343970,0.8556428028645770,0.8342045271374950,0.8500817463789800,0.8353789117369370,0.8355516153545020,0.8497363391438500,0.8513136988509450,0.8496096898243020)
accNearMissRF = round(accNearMissRF, 3)

f1NearMissRF <- c(0.8036129841896050,0.8063709911133490,0.8249415453657800,0.8030460894691950,0.8191495765201810,0.8048080675024180,0.8052457050518880,0.8187688007040780,0.8208696643718570,0.8189833945648600)
f1NearMissRF = round(f1NearMissRF, 3)

precisionNearMissRF <- c(0.8457307309640310,0.8472871775066180,0.8677222125460910,0.8454464942232310,0.8619476302164360,0.8464236548058480,0.8461715121254370,0.8631896780524120,0.8636247405026350,0.8623716466718150)
precisionNearMissRF = round(precisionNearMissRF, 3)

recallNearMissRF  <- c(0.8340778778179470,0.8365993506343970,0.8556428028645770,0.8342045271374950,0.8500817463789800,0.8353789117369370,0.8355516153545020,0.8497363391438500,0.8513136988509450,0.8496096898243020)
recallNearMissRF = round(recallNearMissRF, 3)


# Computando os testes
wilcox.test(accRandomRF, accClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFAccRC = wilcox.test(accRandomRF, accClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFAccRC$p.value)

wilcox.test(precisionRandomRF, precisionClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFPrecisionRC = wilcox.test(precisionRandomRF, precisionClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFPrecisionRC$p.value)

wilcox.test(f1RandomRF, f1ClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFF1RC = wilcox.test(f1RandomRF, f1ClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFF1RC$p.value)

wilcox.test(recallRandomRF, recallClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFRecallRC = wilcox.test(recallRandomRF, recallClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFRecallRC$p.value)

wilcox.test(accNearMissRF, accClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFAccNC = wilcox.test(accNearMissRF, accClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFAccNC$p.value)

wilcox.test(precisionNearMissRF, precisionClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFPrecisionNC = wilcox.test(precisionNearMissRF, precisionClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFPrecisionNC$p.value)

wilcox.test(f1NearMissRF, f1ClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFF1NC = wilcox.test(f1NearMissRF, f1ClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFF1NC$p.value)

wilcox.test(recallNearMissRF, recallClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFRecallNC = wilcox.test(recallNearMissRF, recallClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFRecallNC$p.value)

################################
pdf(file="accRFCIC2018.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1)) 
  boxplot(accAllRF, accRandomRF, accClusterCentroidsRF, accNearMissRF,
          main = "",
          at = c(1,2,4,5),
          names = c("Completa", "Aleatória", "Centroides", "NearMiss"),
          las = 2,
          col = c("orange","red","blue","green"),
          border = "red",
          horizontal = FALSE,
          notch = FALSE,
          ylim = c(0.7,1 ), yaxs = "i" , cex.main=1.5,
          cex.lab=1.0,
          font.main=20,las=0)
  dev.off()

  pdf(file="f1RFCIC2018.pdf")
  par(cex.lab=1.5) # is for y-axis
  
  par(cex.axis=1.5) # is for x-axis
  par(mgp=c(2,1,0))
  par(mar=c(7,5,1,1)) 
boxplot(f1AllRF, f1RandomRF, f1ClusterCentroidsRF, f1NearMissRF,
        main = "",
        at = c(1,2,4,5),
        names = c("Completa", "Aleatória", "Centroides", "NearMiss"),
        las = 2,
        col = c("orange","red","blue","green"),
        border = "red",
        horizontal = FALSE,
        notch = FALSE,
        ylim = c(0.6,1 ), yaxs = "i" , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()

pdf(file="precisionRFCIC2018.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1)) 
boxplot(precisionAllRF, precisionRandomRF, precisionClusterCentroidsRF, precisionNearMissRF,
        main = "",
        at = c(1,2,4,5),
        names = c("Completa", "Aleatória", "Centroides", "NearMiss"),
        las = 2,
        col = c("orange","red","blue","green"),
        border = "red",
        horizontal = FALSE,
        notch = FALSE,
        ylim = c(0.6,1 ), yaxs = "i" , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()

pdf(file="recallRFCIC2018.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1)) 
boxplot(recallAllRF, recallRandomRF, recallClusterCentroidsRF, recallNearMissRF,
        main = "",
        at = c(1,2,4,5),
        names = c("Completa", "Aleatória", "Centroides", "NearMiss"),
        las = 2,
        col = c("orange","red","blue","green"),
        border = "red",
        horizontal = FALSE,
        notch = FALSE,
        ylim = c(0.7,1 ), yaxs = "i" , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()
