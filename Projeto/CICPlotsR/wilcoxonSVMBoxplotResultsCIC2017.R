#Results CIC2017 SVM Random
accRandomSVM <- c(0.888704542120002,0.889487470051393,0.887912401658702,0.890217432663427,0.887877862287341,0.888519173345123,0.843818617630711,0.843042599355251,0.890139140502618,0.889215745106379)
accRandomSVM = round(accRandomSVM, 3)

f1RandomSVM <- c(0.875271364708018,0.876101797549643,0.874577846566289,0.876848784733049,0.874550974070865,0.875199852406643,0.830598474616368,0.829959055965587,0.876750268784910,0.875861147337085)
f1RandomSVM = round(f1RandomSVM, 3)

precisionRandomSVM <- c(0.871609707597305,0.872538318039665,0.871267462988490,0.873211072025304,0.870845470052873,0.871465820622073,0.828105940031282,0.827671790192630,0.872996775654953,0.872200549973611)
precisionRandomSVM = round(precisionRandomSVM, 3)

recallRandomSVM  <- c(0.888704542120002,0.889487470051393,0.887912401658702,0.890217432663427,0.887877862287341,0.888519173345123,0.843818617630711,0.843042599355251,0.890139140502618,0.889215745106379)
recallRandomSVM = round(recallRandomSVM, 3)


#Results CIC2017 SVM Cluster Centroids
accClusterCentroidsSVM <- c(0.934591383240840,0.942799903284860,0.943491376332696,0.934233705226071,0.933819973749050,0.934751822044143,0.943272618417113,0.934521547902778,0.945183871784834,0.932230320196193)
accClusterCentroidsSVM = round(accClusterCentroidsSVM, 3)

f1ClusterCentroidsSVM <- c(0.924258974167373,0.934362698128778,0.935300309398156,0.923669458650716,0.923486917688711,0.924336266032132,0.934695468306700,0.924285416937533,0.936954639459301,0.921667067515571)
f1ClusterCentroidsSVM = round(f1ClusterCentroidsSVM, 3)

precisioSVMlusterCentroidsSVM <-c(0.928976508930575,0.937664819807368,0.938284668328835,0.928871964674343,0.928635851968210,0.929552093711860,0.937526930210774,0.929744091410251,0.939406459963136,0.927114703535917)
precisioSVMlusterCentroidsSVM = round(precisioSVMlusterCentroidsSVM, 3)

recallClusterCentroidsSVM  <- c(0.934591383240840,0.942799903284860,0.943491376332696,0.934233705226071,0.933819973749050,0.934751822044143,0.943272618417113,0.934521547902778,0.945183871784834,0.932230320196193)
recallClusterCentroidsSVM = round(recallClusterCentroidsSVM, 3)

#Results CIC2017 SVM Cluster Centroids
accNearMissSVM <- c(0.93376240588,0.93393434884,0.93490224975,0.93065294233,0.93131001451,0.93451003420,0.93363575656,0.93135527846,0.93401570452,0.93186188157)
accNearMissSVM = round(accNearMissSVM, 3)

f1NearMissSVM <-c(0.92796220154,0.92798339956,0.92916825031,0.92541352799,0.92616350886,0.92869094431,0.92756267973,0.92632597535,0.92891819022,0.92575666723)
f1NearMissSVM = round(f1NearMissSVM, 3)

precisionNearMissSVM <- c(0.93640220202,0.93578098812,0.93722415702,0.93461120448,0.93580163700,0.93596633061,0.93509987890,0.93584168572,0.93804726644,0.93362484543)
precisionNearMissSVM = round(precisionNearMissSVM, 3)

recallNearMissSVM  <-c(0.93376240588,0.93393434884,0.93490224975,0.93065294233,0.93131001451,0.93451003420,0.93363575656,0.93135527846,0.93401570452,0.93186188157)
recallNearMissSVM = round(recallNearMissSVM, 3)


# Computando os testes
wilcox.test(accRandomSVM, accClusterCentroidsSVM, paired = TRUE,alternative = "l")
wilcoxonTestSVMAccRC = wilcox.test(accRandomSVM, accClusterCentroidsSVM, paired = TRUE,alternative = "l")
print(wilcoxonTestSVMAccRC$p.value)

wilcox.test(precisionRandomSVM, precisioSVMlusterCentroidsSVM, paired = TRUE,alternative = "l")
wilcoxonTestSVMPrecisionRC = wilcox.test(precisionRandomSVM, precisioSVMlusterCentroidsSVM, paired = TRUE,alternative = "l")
print(wilcoxonTestSVMPrecisionRC$p.value)

wilcox.test(f1RandomSVM, f1ClusterCentroidsSVM, paired = TRUE,alternative = "l")
wilcoxonTestSVMF1RC = wilcox.test(f1RandomSVM, f1ClusterCentroidsSVM, paired = TRUE,alternative = "l")
print(wilcoxonTestSVMF1RC$p.value)

wilcox.test(recallRandomSVM, recallClusterCentroidsSVM, paired = TRUE,alternative = "l")
wilcoxonTestSVMRecallRC = wilcox.test(recallRandomSVM, recallClusterCentroidsSVM, paired = TRUE,alternative = "l")
print(wilcoxonTestSVMRecallRC$p.value)

wilcox.test(accNearMissSVM, accClusterCentroidsSVM, paired = TRUE,alternative = "l")
wilcoxonTestSVMAccSVM = wilcox.test(accNearMissSVM, accClusterCentroidsSVM, paired = TRUE,alternative = "l")
print(wilcoxonTestSVMAccSVM$p.value)

wilcox.test(precisionNearMissSVM, precisioSVMlusterCentroidsSVM, paired = TRUE,alternative = "l")
wilcoxonTestSVMPrecisionSVM = wilcox.test(precisionNearMissSVM, precisioSVMlusterCentroidsSVM, paired = TRUE,alternative = "l")
print(wilcoxonTestSVMPrecisionSVM$p.value)

wilcox.test(f1NearMissSVM, f1ClusterCentroidsSVM, paired = TRUE,alternative = "l")
wilcoxonTestSVMF1SVM = wilcox.test(f1NearMissSVM, f1ClusterCentroidsSVM, paired = TRUE,alternative = "l")
print(wilcoxonTestSVMF1SVM$p.value)

wilcox.test(recallNearMissSVM, recallClusterCentroidsSVM, paired = TRUE,alternative = "l")
wilcoxonTestSVMRecallSVM = wilcox.test(recallNearMissSVM, recallClusterCentroidsSVM, paired = TRUE,alternative = "l")
print(wilcoxonTestSVMRecallSVM$p.value)

################################
pdf(file="accSVMCIC2017.pdf")
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
        ylim = c(0.8,1 ), yaxs = "i"  , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()

pdf(file="f1SVMCIC2017.pdf")
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
        ylim = c(0.8,1 ), yaxs = "i"  , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()

pdf(file="precisionSVMCIC2017.pdf")
par(cex.lab=1.5) # is for y-axis

par(cex.axis=1.5) # is for x-axis
par(mgp=c(2,1,0))
par(mar=c(7,5,1,1)) 
boxplot( precisionRandomSVM, precisioSVMlusterCentroidsSVM, precisionNearMissSVM,
        main = "",
        at = c(2,4,5),
        names = c( "Aleatória", "Centroides", "NearMiss"),
        las = 2,
        col = c("red","blue","green"),
        border = "red",
        horizontal = FALSE,
        notch = FALSE,
        ylim = c(0.8,1 ), yaxs = "i"  , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()

pdf(file="recallSVMCIC2017.pdf")
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
        ylim = c(0.8,1 ), yaxs = "i"  , cex.main=1.5,
        cex.lab=1.0,
        font.main=20,las=0)
dev.off()
