#Results CIC2017 KNN All
accAllKNN <- c(0.987181191820291,0.988263983286395,0.988498788490018,0.988301467249624,0.987075812376497,0.988325513565658,0.988382800377385,0.987158559993436,0.988334707745318,0.988300760005035)
accAllKNN = round(accAllKNN, 3)

f1AllKNN <- c(0.987178872485724,0.988259422943723,0.988495180782721,0.988308193664010,0.987083188449872,0.988319876257802,0.988378133659960,0.987167421413802,0.988347250650863,0.988292901306332)
f1AllKNN = round(f1AllKNN, 3)

precisionAllKNN <- c(0.987231573069693,0.988314078860596,0.988545322575768,0.988370985226039,0.987140362212318,0.988370336442077,0.988447367696026,0.987217675739833,0.988410414646990,0.988340222719647)
precisionAllKNN = round(precisionAllKNN, 3)

recallAllKNN  <- c(0.987181191820291,0.988263983286395,0.988498788490018,0.988301467249624,0.987075812376497,0.988325513565658,0.988382800377385,0.987158559993436,0.988334707745318,0.988300760005035)
recallAllKNN = round(recallAllKNN, 3)

    
#Results CIC2017 KNN Random
accRandomKNN <- c(0.986948136128571,0.987290092260782,0.987087451612918,0.987577931808979,0.987133506812370,0.987326935248478,0.987010309669509,0.986427720652054,0.987544543079224,0.987463947540694)
accRandomKNN = round(accRandomKNN, 3)
print(accRandomKNN)

f1RandomKNN <- c(0.986804578581223,0.987098212261534,0.986897752469421,0.987415050087591,0.986930435632632,0.987146910983729,0.986839873775662,0.986246729673055,0.987365054627993,0.987273829780005)
f1RandomKNN = round(f1RandomKNN, 3)
print(f1RandomKNN)

precisionRandomKNN <- c(0.986815764808902,0.987083999399726,0.986882939067518,0.987401614333133,0.986895597890795,0.987157825470048,0.986837320444823,0.986266943602634,0.987350479531556,0.987259936630554)
precisionRandomKNN = round(precisionRandomKNN, 3)

recallRandomKNN  <- c(0.986948136128571,0.987290092260782,0.987087451612918,0.987577931808979,0.987133506812370,0.987326935248478,0.987010309669509,0.986427720652054,0.987544543079224,0.987463947540694)
recallRandomKNN = round(recallRandomKNN, 3)


#Results CIC2017 KNN Cluster Centroids
accClusterCentroidsKNN <- c(0.994300780620351,0.994128009395184,0.994427429939899,0.994496448021369,0.994289267045847,0.994461906900164,0.994392889216386,0.994369797243618,0.994220185598820,0.994277687587072)
accClusterCentroidsKNN = round(accClusterCentroidsKNN, 3)

f1ClusterCentroidsKNN <- c(0.994173747741107,0.994006812706436,0.994306275470920,0.994286013995221,0.994230208425817,0.994294398637552,0.994277899280813,0.994189144329297,0.994042417914302,0.994044814507518)
f1ClusterCentroidsKNN = round(f1ClusterCentroidsKNN, 3)

precisionClusterCentroidsKNN <- c(0.994173069956796,0.993910231361747,0.994253263944773,0.994157364399303,0.994199223154655,0.994237079208083,0.994197893435176,0.994147915423019,0.993956951794227,0.993939385962880)
precisionClusterCentroidsKNN = round(precisionClusterCentroidsKNN, 3)

recallClusterCentroidsKNN  <- c(0.994300780620351,0.994128009395184,0.994427429939899,0.994496448021369,0.994289267045847,0.994461906900164,0.994392889216386,0.994369797243618,0.994220185598820,0.994277687587072)
recallClusterCentroidsKNN = round(recallClusterCentroidsKNN, 3)

#Results CIC2017 KNN Cluster Centroids
accNearMissKNN <- c(0.994335321343864,0.99408195456691,0.99417413130080,0.99438131095069,0.99408202270477,0.99407044085984,0.99401294125774,0.99395530378916,0.99392083266171,0.99394379008209)
accNearMissKNN = round(accNearMissKNN, 3)

f1NearMissKNN <- c(0.994077197757901,0.99401289386993,0.99407914191247,0.99417850920496,0.99393081817080,0.99380288071856,0.99384429274906,0.99379399646382,0.99378626503990,0.99372326145388)
f1NearMissKNN = round(f1NearMissKNN, 3)

precisionNearMissKNN <- c(0.994010161180831,0.99403489438474,0.99404421951811,0.99415659920706,0.99385417461253,0.99372177748848,0.99378868033039,0.99376132009303,0.99375230886924,0.99363087124206)
precisionNearMissKNN = round(precisionNearMissKNN, 3)

recallNearMissKNN  <- c(0.994335321343864,0.99408195456691,0.99417413130080,0.99438131095069,0.99408202270477,0.99407044085984,0.99401294125774,0.99395530378916,0.99392083266171,0.99394379008209)
recallNearMissKNN = round(recallNearMissKNN, 3)


# Computando os testes
wilcox.test(accRandomKNN, accClusterCentroidsKNN, paired = TRUE,alternative = "l")
wilcoxonTestKNNAccRC = wilcox.test(accRandomKNN, accClusterCentroidsKNN, paired = TRUE,alternative = "l")
print(wilcoxonTestKNNAccRC$p.value)

wilcox.test(precisionRandomKNN, precisionClusterCentroidsKNN, paired = TRUE,alternative = "l")
wilcoxonTestKNNPrecisionRC = wilcox.test(precisionRandomKNN, precisionClusterCentroidsKNN, paired = TRUE,alternative = "l")
print(wilcoxonTestKNNPrecisionRC$p.value)

wilcox.test(f1RandomKNN, f1ClusterCentroidsKNN, paired = TRUE,alternative = "l")
wilcoxonTestKNNF1RC = wilcox.test(f1RandomKNN, f1ClusterCentroidsKNN, paired = TRUE,alternative = "l")
print(wilcoxonTestKNNF1RC$p.value)

wilcox.test(recallRandomKNN, recallClusterCentroidsKNN, paired = TRUE,alternative = "l")
wilcoxonTestKNNRecallRC = wilcox.test(recallRandomKNN, recallClusterCentroidsKNN, paired = TRUE,alternative = "l")
print(wilcoxonTestKNNRecallRC$p.value)

wilcox.test(accNearMissKNN, accClusterCentroidsKNN, paired = TRUE,alternative = "l")
wilcoxonTestKNNAccNC = wilcox.test(accNearMissKNN, accClusterCentroidsKNN, paired = TRUE,alternative = "l")
print(wilcoxonTestKNNAccNC$p.value)

wilcox.test(precisionNearMissKNN, precisionClusterCentroidsKNN, paired = TRUE,alternative = "l")
wilcoxonTestKNNPrecisionNC = wilcox.test(precisionNearMissKNN, precisionClusterCentroidsKNN, paired = TRUE,alternative = "l")
print(wilcoxonTestKNNPrecisionNC$p.value)

wilcox.test(f1NearMissKNN, f1ClusterCentroidsKNN, paired = TRUE,alternative = "l")
wilcoxonTestKNNF1NC = wilcox.test(f1NearMissKNN, f1ClusterCentroidsKNN, paired = TRUE,alternative = "l")
print(wilcoxonTestKNNF1NC$p.value)

wilcox.test(recallNearMissKNN, recallClusterCentroidsKNN, paired = TRUE,alternative = "l")
wilcoxonTestKNNRecallNC = wilcox.test(recallNearMissKNN, recallClusterCentroidsKNN, paired = TRUE,alternative = "l")
print(wilcoxonTestKNNRecallNC$p.value)

################################

pdf(file="accKNNCIC2017.pdf")
par(mfrow=c(1,2))
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1))
  boxplot(accAllKNN, accRandomKNN, accClusterCentroidsKNN, accNearMissKNN,
          main = "",
          at = c(1,2,4,5),
          names = c("Completa", "Aleatória", "Centroides", "NearMiss"),
          las = 2,
          col = c("orange","red","blue","green"),
          border = "red",
          horizontal = FALSE,
          notch = FALSE,
          ylim = c(0.95,1 ), yaxs = "i",xaxs = "i", cex.main=1.5,
          cex.lab=1.0,
          font.main=20,las=0)
  box(lwd=3)
  
  
  
  dev.off()

  pdf(file="f1KNNCIC2017.pdf")
  
  par(cex.lab=1.5) # is for y-axis
  
  par(cex.axis=1.5) # is for x-axis
  par(mgp=c(2,1,0))
  par(mar=c(7,5,1,1))  
boxplot(f1AllKNN, f1RandomKNN, f1ClusterCentroidsKNN, f1NearMissKNN,
        main = "",
        at = c(1,2,4,5),
        names = c("Completa", "Aleatória", "Centroides", "NearMiss"),
        las = 2,
        col = c("orange","red","blue","green"),
        border = "red",
        horizontal = FALSE,
        notch = FALSE,
        ylim = c(0.95,1 ), yaxs = "i", cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()

pdf(file="precisionKNNCIC2017.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1))  
boxplot(precisionAllKNN, precisionRandomKNN, precisionClusterCentroidsKNN, precisionNearMissKNN,
        main = "",
        at = c(1,2,4,5),
        names = c("Completa", "Aleatória", "Centroides", "NearMiss"),
        las = 2,
        col = c("orange","red","blue","green"),
        border = "red",
        horizontal = FALSE,
        notch = FALSE,
        ylim = c(0.9,1 ), yaxs = "i" , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()

pdf(file="recallKNNCIC2017.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1))  
boxplot(recallAllKNN, recallRandomKNN, recallClusterCentroidsKNN, recallNearMissKNN,
        main = "",
        at = c(1,2,4,5),
        names = c("Completa", "Aleatória", "Centroides", "NearMiss"),
        las = 2,
        col = c("orange","red","blue","green"),
        border = "red",
        horizontal = FALSE,
        notch = FALSE,
        ylim = c(0.9,1 ), yaxs = "i" , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()
