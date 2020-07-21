    #Results CIC2018 SVM Random
    accRandomSVM <- c(0.811913095539641,0.810730651438045,0.811003523153798,0.810097404840306,0.810437055288184,0.811156653694706,0.811715062058166,0.810814700531927,0.810493471803255,0.809832592626706)
    accRandomSVM = round(accRandomSVM, 3)
    
    f1RandomSVM <- c(0.798843323063073,0.798074573895639,0.798316061114699,0.796920396258479,0.797259219957399,0.798009441656055,0.799148219429761,0.798044788764396,0.797626799075582,0.796320964365735)
    f1RandomSVM = round(f1RandomSVM, 3)
    
    precisionRandomSVM <- c(0.843955740487579,0.841576280155723,0.841687663458994,0.841585048368238,0.842164517191440,0.842624793687135,0.843243152603648,0.842739455930962,0.841686215634470,0.842369147349385)
    precisionRandomSVM = round(precisionRandomSVM, 3)
    
    recallRandomSVM  <- c(0.811913095539641,0.810730651438045,0.811003523153798,0.810097404840306,0.810437055288184,0.811156653694706,0.811715062058166,0.810814700531927,0.810493471803255,0.809832592626706)
    recallRandomSVM = round(recallRandomSVM, 3)
    
    
    #Results CIC2018 SVM Cluster Centroids
    accClusterCentroidsSVM <- c(0.969396918967462,0.971112441568609,0.971918391783913,0.970260437055288,0.971100927994105,0.970156814884749,0.971054873696087,0.970398599949340,0.969949570543671,0.971008819398070)
    accClusterCentroidsSVM = round(accClusterCentroidsSVM, 3)
    
    f1ClusterCentroidsSVM <- c(0.968158861081169,0.970021083232801,0.970906759969250,0.969009226403854,0.969905432946306,0.968993336167312,0.969967810420753,0.969149931817169,0.968715988837992,0.969869147345591)
    f1ClusterCentroidsSVM = round(f1ClusterCentroidsSVM, 3)
    
    precisionClusterCentroidsSVM <- c(0.969364809794403,0.971453645530839,0.972101503835049,0.970518348358196,0.971371617376496,0.970309070368199,0.971404683641797,0.970518357685004,0.970090472253306,0.971339297654209)
    precisionClusterCentroidsSVM = round(precisionClusterCentroidsSVM, 3)
    
    recallClusterCentroidsSVM  <- c(0.969396918967462,0.971112441568609,0.971918391783913,0.970260437055288,0.971100927994105,0.970156814884749,0.971054873696087,0.970398599949340,0.969949570543671,0.971008819398070)
    recallClusterCentroidsSVM = round(recallClusterCentroidsSVM, 3)
    
    #Results CIC2018 SVM Cluster Centroids
    accNearMissSVM <- c(0.84754875999,0.84850438667,0.84773297718,0.84802081654,0.84703064914,0.84825108803,0.84855044097,0.84864254957,0.84947152693,0.84756027356)
    accNearMissSVM = round(accNearMissSVM, 3)
    
    f1NearMissSVM <-  c(0.81748106539,0.81853476190,0.81755434714,0.81811601981,0.81681559061,0.81834547690,0.81837495909,0.81889196520,0.81966871167,0.81741596578)
    f1NearMissSVM = round(f1NearMissSVM, 3)
    
    precisionNearMissSVM <- c(0.81636417077,0.81732065673,0.81634511748,0.81704596707,0.81563848877,0.81728593351,0.81684096460,0.81798970552,0.81832822611,0.81635244794) 
    precisionNearMissSVM = round(precisionNearMissSVM, 3)
    
    recallNearMissSVM  <- c(0.84754875999,0.84850438667,0.84773297718,0.84802081654,0.84703064914,0.84825108803,0.84855044097,0.84864254957,0.84947152693,0.84756027356)
    recallNearMissSVM = round(recallNearMissSVM, 3)
    
    
    # Computando os testes
    wilcox.test(accRandomSVM, accClusterCentroidsSVM, paired = TRUE,alternative = "l")
    wilcoxonTestSVMAccRC = wilcox.test(accRandomSVM, accClusterCentroidsSVM, paired = TRUE,alternative = "l")
    print(wilcoxonTestSVMAccRC$p.value)
    
    wilcox.test(precisionRandomSVM, precisionClusterCentroidsSVM, paired = TRUE,alternative = "l")
    wilcoxonTestSVMPrecisionRC = wilcox.test(precisionRandomSVM, precisionClusterCentroidsSVM, paired = TRUE,alternative = "l")
    print(wilcoxonTestSVMPrecisionRC$p.value)
    
    wilcox.test(f1RandomSVM, f1ClusterCentroidsSVM, paired = TRUE,alternative = "l")
    wilcoxonTestSVMF1RC = wilcox.test(f1RandomSVM, f1ClusterCentroidsSVM, paired = TRUE,alternative = "l")
    print(wilcoxonTestSVMF1RC$p.value)
    
    wilcox.test(recallRandomSVM, recallClusterCentroidsSVM, paired = TRUE,alternative = "l")
    wilcoxonTestSVMRecallRC = wilcox.test(recallRandomSVM, recallClusterCentroidsSVM, paired = TRUE,alternative = "l")
    print(wilcoxonTestSVMRecallRC$p.value)
    
    wilcox.test(accNearMissSVM, accClusterCentroidsSVM, paired = TRUE,alternative = "l")
    wilcoxonTestSVMAccNC = wilcox.test(accNearMissSVM, accClusterCentroidsSVM, paired = TRUE,alternative = "l")
    print(wilcoxonTestSVMAccNC$p.value)
    
    wilcox.test(precisionNearMissSVM, precisionClusterCentroidsSVM, paired = TRUE,alternative = "l")
    wilcoxonTestSVMPrecisionNC = wilcox.test(precisionNearMissSVM, precisionClusterCentroidsSVM, paired = TRUE,alternative = "l")
    print(wilcoxonTestSVMPrecisionNC$p.value)
    
    wilcox.test(f1NearMissSVM, f1ClusterCentroidsSVM, paired = TRUE,alternative = "l")
    wilcoxonTestSVMF1NC = wilcox.test(f1NearMissSVM, f1ClusterCentroidsSVM, paired = TRUE,alternative = "l")
    print(wilcoxonTestSVMF1NC$p.value)
    
    wilcox.test(recallNearMissSVM, recallClusterCentroidsSVM, paired = TRUE,alternative = "l")
    wilcoxonTestSVMRecallNC = wilcox.test(recallNearMissSVM, recallClusterCentroidsSVM, paired = TRUE,alternative = "l")
    print(wilcoxonTestSVMRecallNC$p.value)
    
    ################################
    pdf(file="accSVMCIC2018.pdf")
    par(cex.lab=1.5) # is for y-axis
    
    par(cex.axis=1.5) # is for x-axis
    par(mgp=c(2,1,0))
    par(mar=c(7,5,1,1)) 
    boxplot(accRandomSVM, accClusterCentroidsSVM, accNearMissSVM,
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
    
    pdf(file="f1SVMCIC2018.pdf")
    par(cex.lab=1.5) # is for y-axis
    
    par(cex.axis=1.5) # is for x-axis
    par(mgp=c(2,1,0))
    par(mar=c(7,5,1,1)) 
    boxplot(f1RandomSVM, f1ClusterCentroidsSVM, f1NearMissSVM,
            main = "",
            at = c(2,4,5),
            names = c( "Aleatória", "Centroides", "NearMiss"),
            las = 2,
            col = c("red","blue","green"),
            border = "red",
            horizontal = FALSE,
            notch = FALSE,
            ylim = c(0.7,1 ), yaxs = "i" , cex.main=1.5,
            cex.lab=1.0,
            font.main=20,las=0)
    dev.off()
    
    pdf(file="precisionSVMCIC2018.pdf")
    par(cex.lab=1.5) # is for y-axis
    
    par(cex.axis=1.5) # is for x-axis
    par(mgp=c(2,1,0))
    par(mar=c(7,5,1,1)) 
    boxplot( precisionRandomSVM, precisionClusterCentroidsSVM, precisionNearMissSVM,
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
    
    pdf(file="recallSVMCIC2018.pdf")
    par(cex.lab=1.5) # is for y-axis
    
    par(cex.axis=1.5) # is for x-axis
    par(mgp=c(2,1,0))
    par(mar=c(7,5,1,1)) 
    boxplot( recallRandomSVM, recallClusterCentroidsSVM, recallNearMissSVM,
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
