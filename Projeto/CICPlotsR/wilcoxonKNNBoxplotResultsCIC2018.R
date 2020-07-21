#Results CIC2018 KNN Random
accRandomKNN <- c(0.8529670481497680,0.8533953531213290,0.8555645105579470,0.8578672254588150,0.8533297257466550,0.8590151288368980,0.8556900085200450,0.8528438529025720,0.8585292559928150,0.8529624427199660)
accRandomKNN = round(accRandomKNN, 3)

f1RandomKNN <- c(0.8222726705773910,0.8239268112051480,0.8274287189864540,0.8378484727398710,0.8226322681717800,0.8366307280359770,0.8272585277791030,0.8221456552326400,0.8323983097089190,0.8226292431807750)
f1RandomKNN = round(f1RandomKNN, 3)

precisionRandomKNN <- c(0.8421661731126970,0.8498556065481650,0.8376998783737170,0.8447374559369000,0.8363634758340550,0.8426869282813220,0.8211423655271090,0.8297023447885860,0.8443951835709900,0.8288186391873420)
precisionRandomKNN = round(precisionRandomKNN, 3)

recallRandomKNN  <- c(0.8529670481497680,0.8533953531213290,0.8555645105579470,0.8578672254588150,0.8533297257466550,0.8590151288368980,0.8556900085200450,0.8528438529025720,0.8585292559928150,0.8529624427199660)
recallRandomKNN = round(recallRandomKNN, 3)


#Results CIC2018 KNN Cluster Centroids
accClusterCentroidsKNN <- c(0.9962350611370800,0.9964883597761760,0.9964423054781580,0.9968107398622970,0.9963041425841060,0.9965804683722100,0.9964307919036540,0.9965574412232020,0.9965229004996890,0.9962350611370800)
accClusterCentroidsKNN = round(accClusterCentroidsKNN, 3)

f1ClusterCentroidsKNN <- c(0.9962242946793990,0.9964427335061070,0.9963989465244820,0.9968115996559010,0.9962601275098420,0.9965509327756220,0.9964133709195260,0.9965368087804630,0.9964716675889370,0.9962596054601260)
f1ClusterCentroidsKNN = round(f1ClusterCentroidsKNN, 3)

precisionClusterCentroidsKNN <-c(0.9962372070951660,0.9964456215820350,0.9964598165271800,0.9968278685327620,0.9962812739452520,0.9965826638104850,0.9964126204240210,0.9965466403240270,0.9965302626361040,0.9962981328596700)
precisionClusterCentroidsKNN = round(precisionClusterCentroidsKNN, 3)

recallClusterCentroidsKNN  <- c(0.9962350611370800,0.9964883597761760,0.9964423054781580,0.9968107398622970,0.9963041425841060,0.9965804683722100,0.9964307919036540,0.9965574412232020,0.9965229004996890,0.9962350611370800)
recallClusterCentroidsKNN = round(recallClusterCentroidsKNN, 3)

#Results CIC2018 KNN Cluster Centroids
accNearMissKNN <- c(0.9385059985723160,0.9077302139222140,0.9041034379533470,0.9077992953692400,0.9048978745941460,0.9375733990374650,0.9059110691505280,0.9371128560572910,0.9439749464618780,0.9061643677896230)
accNearMissKNN = round(accNearMissKNN, 3)

f1NearMissKNN <- c(0.9368311148743250,0.8772556059310540,0.8810638567762950,0.8772621604696140,0.8738623718946540,0.9344053955175510,0.8751592491289260,0.9330585776079740,0.9424104186015840,0.8753161860165870)
f1NearMissKNN = round(f1NearMissKNN, 3)

precisionNearMissKNN <- c(0.9426826277851860,0.9453651958038790,0.8983472378771050,0.8618676431312130,0.8585403799337610,0.9440566130689060,0.9101788456439750,0.9466709560119710,0.9482695285752630,0.9295245144131850)
precisionNearMissKNN = round(precisionNearMissKNN, 3)

recallNearMissKNN  <- c(0.9385059985723160,0.9077302139222140,0.9041034379533470,0.9077992953692400,0.9048978745941460,0.9375733990374650,0.9059110691505280,0.9371128560572910,0.9439749464618780,0.9061643677896230)
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
pdf(file="accKNNCIC2018.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1)) 
boxplot(accRandomKNN, accClusterCentroidsKNN, accNearMissKNN,
        main = "",
        at = c(2,4,5),
        names = c( "Aleatória", "Centroides", "NearMiss"),
        las = 2,
        col = c("red","blue","green"),
        border = "red",
        horizontal = FALSE,
        notch = FALSE,
        ylim = c(0.8,1 ), yaxs = "i", cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()

pdf(file="f1KNNCIC2018.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1)) 
boxplot(f1RandomKNN, f1ClusterCentroidsKNN, f1NearMissKNN,
        main = "",
        at = c(2,4,5),
        names = c( "Aleatória", "Centroides", "NearMiss"),
        las = 2,
        col = c("red","blue","green"),
        border = "red",
        horizontal = FALSE,
        notch = FALSE,
        ylim = c(0.8,1 ), yaxs = "i" , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()

pdf(file="precisionKNNCIC2018.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1)) 
boxplot( precisionRandomKNN, precisionClusterCentroidsKNN, precisionNearMissKNN,
         main = "",
         at = c(2,4,5),
         names = c( "Aleatória", "Centroides", "NearMiss"),
         las = 2,
         col = c("red","blue","green"),
         border = "red",
         horizontal = FALSE,
         notch = FALSE,
         ylim = c(0.8,1 ), yaxs = "i" , cex.main=1.5,
         cex.lab=1.0,
         font.main=20,las=0)
dev.off()

pdf(file="recallKNNCIC2018.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1)) 
boxplot( recallRandomKNN, recallClusterCentroidsKNN, recallNearMissKNN,
         main = "",
         at = c(2,4,5),
         names = c( "Aleatória", "Centroides", "NearMiss"),
         las = 2,
         col = c("red","blue","green"),
         border = "red",
         horizontal = FALSE,
         notch = FALSE,
         ylim = c(0.8,1 ), yaxs = "i" , cex.main=1.5,
         cex.lab=1.0,
         font.main=20,las=0)
dev.off()
