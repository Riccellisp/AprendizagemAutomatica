#Results CIC2017 RF All
accAllRF <- c(0.885789193019778,0.886507046277842,0.886132206645553,0.886168983364192,0.885997122929011,0.886299823613199,0.886240415067704,0.886056531474505,0.886268704851273,0.886026119957169)
accAllRF = round(accAllRF, 3)

f1AllRF <- c(0.849747555019560,0.850693763796811,0.850179498990182,0.850266210033194,0.850046935131857,0.850394580631294,0.850381363148971,0.850059858445744,0.850436271593648,0.850003412315856)
f1AllRF = round(f1AllRF, 3)

precisionAllRF <- c(0.828296581897309,0.829294289178775,0.828722845143853,0.828879377380988,0.828671369121515,0.828925960567079,0.829095306990849,0.828499744511337,0.829153632573900,0.828436198185719)
precisionAllRF = round(precisionAllRF, 3)

recallAllRF  <- c(0.885789193019778,0.886507046277842,0.886132206645553,0.886168983364192,0.885997122929011,0.886299823613199,0.886240415067704,0.886056531474505,0.886268704851273,0.886026119957169)
recallAllRF = round(recallAllRF, 3)


#Results CIC2017 RF Random
        accRandomRF <- c(0.702692479880914,0.698180270899792,0.702805303048301,0.700866391357855,0.700256167879182,0.701170368813975,0.716538768528671,0.713625814824740,0.698027136501274,0.698889503099086)
        accRandomRF = round(accRandomRF, 3)
        
        f1RandomRF <- c(0.614212678378657,0.610831611693009,0.613791771396504,0.612399318003905,0.611917867711621,0.612414226818948,0.625397902474027,0.622667261133403,0.609926169910143,0.609724363511895)
        f1RandomRF = round(f1RandomRF, 3)
        
        precisionRandomRF <- c(0.556407466918209,0.554169793033073,0.552533601165639,0.553773347448921,0.550553649724810,0.551849996432241,0.557493712294743,0.554985589078573,0.550206821063787,0.552145636370485)
        precisionRandomRF = round(precisionRandomRF, 3)
        
        recallRandomRF  <- c(0.702692479880914,0.698180270899792,0.702805303048301,0.700866391357855,0.700256167879182,0.701170368813975,0.716538768528671,0.713625814824740,0.698027136501274,0.698889503099086)
        recallRandomRF = round(recallRandomRF, 3)


#Results CIC2017 RF Cluster Centroids
accClusterCentroidsRF <- c(0.761196951205471,0.762264976454469,0.762141064314827,0.761228742818325,0.761715062058166,0.769115632160086,0.761553872015105,0.761746859636397,0.763361503212287,0.759996776162020)
accClusterCentroidsRF = round(accClusterCentroidsRF, 3)

f1ClusterCentroidsRF <- c(0.667168378484462,0.668476330847215,0.668027212817093,0.667731248323619,0.667666644769605,0.684101612411375,0.669783141156073,0.667910262387205,0.670109815692988,0.665671720805188)
f1ClusterCentroidsRF = round(f1ClusterCentroidsRF, 3)

precisioRFlusterCentroidsRF <-c(0.597901545499339,0.599431404187562,0.598742683439368,0.599059432831588,0.598493684409541,0.649992554693394,0.604344822337132,0.598648886233459,0.601532499418260,0.596354583149019)
precisioRFlusterCentroidsRF = round(precisioRFlusterCentroidsRF, 3)

recallClusterCentroidsRF  <- c(0.761196951205471,0.762264976454469,0.762141064314827,0.761228742818325,0.761715062058166,0.769115632160086,0.761553872015105,0.761746859636397,0.763361503212287,0.759996776162020)
recallClusterCentroidsRF = round(recallClusterCentroidsRF, 3)

#Results CIC2017 RF NearMiss
accNearMissRF <- c(0.777454118405600,0.77846476229952,0.77819098717388,0.77764728909767,0.77792617496028,0.78036452396578,0.77762682202317,0.78790600209549,0.77958412968890,0.78621348715646)
accNearMissRF = round(accNearMissRF, 3)

f1NearMissRF <-c(0.697081745461416,0.69824893470713,0.69807820928816,0.69687878520302,0.69734429076889,0.70284058879295,0.69689280624872,0.71661424558365,0.69970621617393,0.71424195505468)
f1NearMissRF = round(f1NearMissRF, 3)

precisionNearMissRF <- c(0.646613744968282,0.64713739714203,0.64775515028270,0.64537997093246,0.64600527859977,0.65674792548568,0.64619230153545,0.68545344051353,0.64898623699540,0.68275492786796)
precisionNearMissRF = round(precisionNearMissRF, 3)

recallNearMissRF  <-c(0.777454118405600,0.77846476229952,0.77819098717388,0.77764728909767,0.77792617496028,0.78036452396578,0.77762682202317,0.78790600209549,0.77958412968890,0.78621348715646)
recallNearMissRF = round(recallNearMissRF, 3)


# Computando os testes
wilcox.test(accRandomRF, accClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFAccRC = wilcox.test(accRandomRF, accClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFAccRC$p.value)

wilcox.test(precisionRandomRF, precisioRFlusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFPrecisionRC = wilcox.test(precisionRandomRF, precisioRFlusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFPrecisionRC$p.value)

wilcox.test(f1RandomRF, f1ClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFF1RC = wilcox.test(f1RandomRF, f1ClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFF1RC$p.value)

wilcox.test(recallRandomRF, recallClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFRecallRC = wilcox.test(recallRandomRF, recallClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFRecallRC$p.value)

wilcox.test(accNearMissRF, accClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFAccRF = wilcox.test(accNearMissRF, accClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFAccRF$p.value)

wilcox.test(precisionNearMissRF, precisioRFlusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFPrecisionRF = wilcox.test(precisionNearMissRF, precisioRFlusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFPrecisionRF$p.value)

wilcox.test(f1NearMissRF, f1ClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFF1RF = wilcox.test(f1NearMissRF, f1ClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFF1RF$p.value)

wilcox.test(recallNearMissRF, recallClusterCentroidsRF, paired = TRUE,alternative = "l")
wilcoxonTestRFRecallRF = wilcox.test(recallNearMissRF, recallClusterCentroidsRF, paired = TRUE,alternative = "l")
print(wilcoxonTestRFRecallRF$p.value)

################################
pdf(file="accRFCIC2017.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1)) 
boxplot(accAllRF, accRandomRF, accClusterCentroidsRF, accNearMissRF,
        main = "",
        at = c(1,2,4,5),
        names = c("Completo", "Aleatória", "Centroides", "NearMiss"),
        las = 2,
        col = c("orange","red","blue","green"),
        border = "red",
        horizontal = FALSE,
        notch = FALSE,
        ylim = c(0.6,1 ), yaxs = "i" , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()

pdf(file="f1RFCIC2017.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1)) 
boxplot(f1AllRF, f1RandomRF, f1ClusterCentroidsRF, f1NearMissRF,
        main = "",
        at = c(1,2,4,5),
        names = c("Completo", "Aleatória", "Centroides", "NearMiss"),
        las = 2,
        col = c("orange","red","blue","green"),
        border = "red",
        horizontal = FALSE,
        notch = FALSE,
        ylim = c(0.6,1 ), yaxs = "i" , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()

pdf(file="precisionRFCIC2017.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1)) 
boxplot(precisionAllRF, precisionRandomRF, precisioRFlusterCentroidsRF, precisionNearMissRF,
        main = "",
        at = c(1,2,4,5),
        names = c("Completo", "Aleatória", "Centroides", "NearMiss"),
        las = 2,
        col = c("orange","red","blue","green"),
        border = "red",
        horizontal = FALSE,
        notch = FALSE,
        ylim = c(0.5,1 ), yaxs = "i" , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()

pdf(file="recallRFCIC2017.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1)) 
boxplot(recallAllRF, recallRandomRF, recallClusterCentroidsRF, recallNearMissRF,
        main = "",
        at = c(1,2,4,5),
        names = c("Completo", "Aleatória", "Centroides", "NearMiss"),
        las = 2,
        col = c("orange","red","blue","green"),
        border = "red",
        horizontal = FALSE,
        notch = FALSE,
        ylim = c(0.6,1 ), yaxs = "i" , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()
