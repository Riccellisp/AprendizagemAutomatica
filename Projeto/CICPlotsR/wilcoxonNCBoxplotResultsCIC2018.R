    #Results CIC2018 NC All
    accAllNC <- c(0.2670472288922090,0.2667903661157250,0.2667614770861770,0.2670785634153270,0.2501267358780280,0.2668106634223580,0.2669056368548170,0.2669352595395810,0.2667925344069870,0.2847291501725570)
    accAllNC = round(accAllNC, 3)
    
    f1AllNC <- c(0.3582996144417310,0.3579484593775240,0.3580274110433150,0.3582253620389240,0.3435509082883750,0.3580026860076130,0.3580784269923630,0.3581746471928790,0.3579867634385190,0.3735914110526930)
    f1AllNC = round(f1AllNC, 3)
    
    precisionAllNC <- c(0.9074060140685790,0.9072151289177510,0.9075077329456940,0.9071154776135320,0.8931729497545500,0.9074778895095240,0.9071035317941470,0.9075229940977070,0.9072561405619640,0.9208868619565790)
    precisionAllNC = round(precisionAllNC, 3)
    
    recallAllNC  <- c(0.2670472288922090,0.2667903661157250,0.2667614770861770,0.2670785634153270,0.2501267358780280,0.2668106634223580,0.2669056368548170,0.2669352595395810,0.2667925344069870,0.2847291501725570)
    recallAllNC = round(recallAllNC, 3)
    
        
    #Results CIC2018 NC Random
    accRandomNC <- c(0.4791212839938280,0.4686404771225270,0.4766769521265570,0.4834526907223610,0.4774414534736450,0.4778996937389180,0.4820917862159480,0.4779492021092860,0.4742510419784920,0.4911863587169270)
    accRandomNC = round(accRandomNC, 3)
    
    f1RandomNC <- c(0.4535829822066130,0.4436643622943630,0.4512801984271920,0.4588958718480180,0.4506790494793540,0.4514694779712110,0.4573036422465460,0.4526214042310620,0.4468870188379810,0.4687204141869350)
    f1RandomNC = round(f1RandomNC, 3)
    
    precisionRandomNC <- c(0.5432404865679740,0.5250859456197840,0.5458267015353290,0.5327561092313490,0.5263743013167810,0.5411451870600530,0.5721119055982440,0.5419548068921220,0.5282213856105300,0.6000904871587310)
    precisionRandomNC = round(precisionRandomNC, 3)
    
    recallRandomNC  <- c(0.4791212839938280,0.4686404771225270,0.4766769521265570,0.4834526907223610,0.4774414534736450,0.4778996937389180,0.4820917862159480,0.4779492021092860,0.4742510419784920,0.4911863587169270)
    recallRandomNC = round(recallRandomNC, 3)
    
    
    #Results CIC2018 NC Cluster Centroids
    accClusterCentroidsNC <- c(0.8799940129412570,0.8884680037764520,0.8835056531650810,0.8847376056370460,0.8839661961452550,0.8856586915973930,0.8892278996937380,0.8813526147327690,0.8875123770925920,0.8768277799525640)
    accClusterCentroidsNC = round(accClusterCentroidsNC, 3)
    
    f1ClusterCentroidsNC <- c(0.8739150346079610,0.8817469651110090,0.8802699031525520,0.8781783347125530,0.8778476398250090,0.8793227592663190,0.8825918950995680,0.8749915133709430,0.8808570843811670,0.8740589199405260)
    f1ClusterCentroidsNC = round(f1ClusterCentroidsNC, 3)
    
    precisionClusterCentroidsNC <- c(0.8833410418436790,0.8954786249768310,0.8972017082822910,0.8890990673258420,0.8932042047144000,0.8892546309058090,0.8953462496477510,0.8845042088684710,0.8933539181982650,0.8906166947528360)
    precisionClusterCentroidsNC = round(precisionClusterCentroidsNC, 3)
    
    recallClusterCentroidsNC  <- c(0.8799940129412570,0.8884680037764520,0.8835056531650810,0.8847376056370460,0.8839661961452550,0.8856586915973930,0.8892278996937380,0.8813526147327690,0.8875123770925920,0.8768277799525640)
    recallClusterCentroidsNC = round(recallClusterCentroidsNC, 3)
    
    #Results CIC2018 NC Cluster Centroids
    accNearMissNC <- c(0.8650378796601190,0.8680083818822390,0.8671333502199090,0.8658898841734400,0.8661316692380310,0.8668915651553180,0.8666728072397350,0.8662352914085700,0.8672369723904480,0.8657977755774050)
    accNearMissNC = round(accNearMissNC, 3)
    
    f1NearMissNC <- c(0.8662282542149190,0.8692188946409150,0.8683182603054020,0.8671171323211630,0.8673558415289700,0.8680751985136170,0.8675121544204270,0.8675224196302290,0.8684546547629910,0.8669888686477370)
    f1NearMissNC = round(f1NearMissNC, 3)
    
    precisionNearMissNC <- c(0.8876340457410830,0.8898755282388160,0.8892627102819880,0.8882843324499250,0.8884190803719900,0.8890632281985430,0.8878791907881530,0.8888245106001110,0.8891049076410120,0.888421773245457)
    precisionNearMissNC = round(precisionNearMissNC, 3)
    
    recallNearMissNC  <- c(0.8650378796601190,0.8680083818822390,0.8671333502199090,0.8658898841734400,0.8661316692380310,0.8668915651553180,0.8666728072397350,0.8662352914085700,0.8672369723904480,0.8657977755774050)
    recallNearMissNC = round(recallNearMissNC, 3)
    
    
    # Computando os testes
    wilcox.test(accRandomNC, accClusterCentroidsNC, paired = TRUE,alternative = "l")
    wilcoxonTestNCAccRC = wilcox.test(accRandomNC, accClusterCentroidsNC, paired = TRUE,alternative = "l")
    print(wilcoxonTestNCAccRC$p.value)
    
    wilcox.test(precisionRandomNC, precisionClusterCentroidsNC, paired = TRUE,alternative = "l")
    wilcoxonTestNCPrecisionRC = wilcox.test(precisionRandomNC, precisionClusterCentroidsNC, paired = TRUE,alternative = "l")
    print(wilcoxonTestNCPrecisionRC$p.value)
    
    wilcox.test(f1RandomNC, f1ClusterCentroidsNC, paired = TRUE,alternative = "l")
    wilcoxonTestNCF1RC = wilcox.test(f1RandomNC, f1ClusterCentroidsNC, paired = TRUE,alternative = "l")
    print(wilcoxonTestNCF1RC$p.value)
    
    wilcox.test(recallRandomNC, recallClusterCentroidsNC, paired = TRUE,alternative = "l")
    wilcoxonTestNCRecallRC = wilcox.test(recallRandomNC, recallClusterCentroidsNC, paired = TRUE,alternative = "l")
    print(wilcoxonTestNCRecallRC$p.value)
    
    wilcox.test(accNearMissNC, accClusterCentroidsNC, paired = TRUE,alternative = "l")
    wilcoxonTestNCAccNC = wilcox.test(accNearMissNC, accClusterCentroidsNC, paired = TRUE,alternative = "l")
    print(wilcoxonTestNCAccNC$p.value)
    
    wilcox.test(precisionNearMissNC, precisionClusterCentroidsNC, paired = TRUE,alternative = "l")
    wilcoxonTestNCPrecisionNC = wilcox.test(precisionNearMissNC, precisionClusterCentroidsNC, paired = TRUE,alternative = "l")
    print(wilcoxonTestNCPrecisionNC$p.value)
    
    wilcox.test(f1NearMissNC, f1ClusterCentroidsNC, paired = TRUE,alternative = "l")
    wilcoxonTestNCF1NC = wilcox.test(f1NearMissNC, f1ClusterCentroidsNC, paired = TRUE,alternative = "l")
    print(wilcoxonTestNCF1NC$p.value)
    
    wilcox.test(recallNearMissNC, recallClusterCentroidsNC, paired = TRUE,alternative = "l")
    wilcoxonTestNCRecallNC = wilcox.test(recallNearMissNC, recallClusterCentroidsNC, paired = TRUE,alternative = "l")
    print(wilcoxonTestNCRecallNC$p.value)
    
    ################################
    pdf(file="accNCCIC2018.pdf")
    par(cex.lab=1.5) # is for y-axis
    
    par(cex.axis=1.5) # is for x-axis
    par(mgp=c(2,1,0))
    par(mar=c(7,5,1,1)) 
      boxplot(accAllNC, accRandomNC, accClusterCentroidsNC, accNearMissNC,
              main = "",
              at = c(1,2,4,5),
              names = c("Completa", "Aleatória", "Centroides", "NearMiss"),
              las = 2,
              col = c("orange","red","blue","green"),
              border = "red",
              horizontal = FALSE,
              notch = FALSE,
              ylim = c(0.2,1 ), yaxs = "i" , cex.main=1.5,
              cex.lab=1.0,
              font.main=20,las=0)
      dev.off()
    
      pdf(file="f1NCCIC2018.pdf")
      par(cex.lab=1.5) # is for y-axis
      
      par(cex.axis=1.5) # is for x-axis
      par(mgp=c(2,1,0))
      par(mar=c(7,5,1,1))     
    boxplot(f1AllNC, f1RandomNC, f1ClusterCentroidsNC, f1NearMissNC,
            main = "",
            at = c(1,2,4,5),
            names = c("Completa", "Aleatória", "Centroides", "NearMiss"),
            las = 2,
            col = c("orange","red","blue","green"),
            border = "red",
            horizontal = FALSE,
            notch = FALSE,
            ylim = c(0.3,1 ), yaxs = "i" , cex.main=1.5,
            cex.lab=1.0,
            font.main=20,las=0)
    dev.off()
    
    pdf(file="precisionNCCIC2018.pdf")
    par(cex.lab=1.5) # is for y-axis
    
    par(cex.axis=1.5) # is for x-axis
    par(mgp=c(2,1,0))
    par(mar=c(7,5,1,1)) 
    boxplot(precisionAllNC, precisionRandomNC, precisionClusterCentroidsNC, precisionNearMissNC,
            main = "",
            at = c(1,2,4,5),
            names = c("Completa", "Aleatória", "Centroides", "NearMiss"),
            las = 2,
            col = c("orange","red","blue","green"),
            border = "red",
            horizontal = FALSE,
            notch = FALSE,
            ylim = c(0.5,1 ), yaxs = "i" , cex.main=1.5,
            cex.lab=1.0,
            font.main=20,las=0)
    dev.off()
    
    pdf(file="recallNCCIC2018.pdf")
    par(cex.lab=1.5) # is for y-axis
    
    par(cex.axis=1.5) # is for x-axis
    par(mgp=c(2,1,0))
    par(mar=c(7,5,1,1)) 
    boxplot(recallAllNC, recallRandomNC, recallClusterCentroidsNC, recallNearMissNC,
            main = "",
            at = c(1,2,4,5),
            names = c("Completa", "Aleatória", "Centroides", "NearMiss"),
            las = 2,
            col = c("orange","red","blue","green"),
            border = "red",
            horizontal = FALSE,
            notch = FALSE,
            ylim = c(0.2,1 ), yaxs = "i" , cex.main=1.5,
            cex.lab=1.0,
            font.main=20,las=0)
    dev.off()
