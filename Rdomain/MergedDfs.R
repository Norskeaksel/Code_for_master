library(ggplot2)
library(scales)
library(plotly)
library(reshape2)
library(dplyr)
library(tidyverse)
library(knitr)
rm(list=ls())

scenario="GradualDevelopment" #Only needed for testing/debugging purposes
scenarios=c("GradualDevelopment")#, "GradualDevelopment", "SocietalCommitment", "TechnoFriendly", "DirectedTransition")#, "MiddleEarth"
technologies=c("PV","Hydro","Wind Onshore","Wind Offshore")# Deep","Wind Offshore Transitional" #All others are set to thermal
#technologies=c("P_Biomass","P_Gas","RES_Hydro_Large","RES_Hydro_Small","RES_PV_Rooftop_Commercial",
#               "RES_PV_Rooftop_Residential","RES_PV_Utility_Avg","RES_PV_Utility_Inf","RES_PV_Utility_Opt",
#               "RES_Wind_Offshore_Deep","RES_Wind_Offshore_Transitional","RES_Wind_Offshore_Deep",
#               "RES_Wind_Onshore_Avg","RES_Wind_Onshore_Opt","HLI_Biomass_CHP_CCS")

technologyUses=c("HLR","Demand","FRT", "HHI", "HLI", "HMI", "PSNG", "X_Electrolysis")#,"X_Biofuel", "X_Gasifier","X_Methanation")
h2=c("H2")
TU=F
Signy=F
AggrigateTechnologies=T #Should always be true because it sets adds unseen technologies with 0-values. Change technologies instead
regions=c("NO")#,"Mordor2","Mordor3","Mordor4","Mordor5")
Allregions=read.csv("AllRegionsNO1_5.csv")
regions<- as.vector(unique(Allregions$AllNations))


sep=","


toThermal=function(df,aggrigations){
  col="Technology"
  for (row in 1:nrow(df)){
    makeThermal=TRUE
    for(tech in aggrigations){
      if(df[row,col]==tech){
        makeThermal=FALSE
        break
      }
    }
    if(makeThermal){
      #print(paste("Make Other: ",df[row,col]))
      df[row,col] = "Thermal"#"Other"
    }
  }
  return (df)
}

getMissingTechnologies=function(df, aggrigations){
  for(tech in aggrigations){
    if(!any(df$Technology == tech)){
      #print(paste("missing tech ",tech))
      missingRow=df[1,]
      missingRow$Technology = tech
      for(i in seq(2015,2050,5)){
        missingRow[toString(i)] = 0
      }
      df[nrow(df) + 1,] = missingRow
    }
  }
  return (df)
}

renameTechnologies=function(df, aggrigations){
  for(tech in aggrigations){
    lastName=tail(strsplit(tech, " ")[[1]],1)
    regex=paste(".*",lastName,".*",sep="")
    #print(regex)
    df$Technology = sub(regex, tech, df$Technology)
  }
  df = toThermal(df, aggrigations)
  df = getMissingTechnologies(df, aggrigations)
  return (df)
}

totals=function(df,PJ2Twh=FALSE, includeCategory=FALSE){
  if(includeCategory){
    df=aggregate(.~Scenario+Category+Technology,data=df, FUN=sum)
  }
  else{
    df=aggregate(.~Scenario+Technology,data=df, FUN=sum)
  }
  if(nrow(df)>length(scenarios)){
    if(includeCategory){
      tot=aggregate(.~Scenario+Category,df,sum)
    }
    else{
      tot=df[,-2]
      tot=aggregate(.~Scenario,tot,sum) #Caclulate sum
    }
    tot$Technology="Sum" 
    df=rbind(df, tot) #Adds sum to end of df
  }
  df=df[order(df$Scenario, decreasing = TRUE),]
  if(PJ2Twh==TRUE){
    df=mutate_if(df, is.numeric, ~ . / 3.6)
  }
  df=format(df, digits=2, nsmall=2)
  return (df)
}

TUscenario=function(scenario){
  TU_Capacities=read.csv(paste("TU\\",scenario,'Capacity.csv',sep=""),check.names = FALSE,sep = sep)
  TU_Productions=read.csv(paste("TU\\",scenario,'Production.csv',sep=""),check.names = FALSE, sep = sep)
  return (list(TU_Capacities,TU_Productions))
}

sumAll=function(Capacities,Productions,scenario){
  CP=TUscenario(scenario)
  TU_Capacities=CP[[1]]
  TU_Productions=CP[[2]]
  
  names(TU_Capacities)[names(TU_Capacities) == "Year"] <- "2015"
  names(TU_Capacities)[names(TU_Capacities) == "Value"] <- "2020"
  
  SumsC=colSums(Capacities[,(ncol(Capacities)-7):ncol(Capacities)], na.rm = TRUE)
  TU_SumsC=colSums(TU_Capacities[,(ncol(TU_Capacities)-7):ncol(TU_Capacities)], na.rm = TRUE)
  SumsP <- colSums(Productions[,(ncol(Productions)-7):ncol(Productions)], na.rm = TRUE)
  TU_SumsP <- colSums(TU_Productions[,(ncol(TU_Productions)-7):ncol(TU_Productions)], na.rm = TRUE)
  Cdiff=SumsC-TU_SumsC
  Pdiff=SumsP-TU_SumsP
  print(scenario)
  print("Summed up Capacity Differences GR vs RR:")
  print(Cdiff)
  #print(SumsC)
  print("Summed up Production Differences GR vs RR:")
  print(Pdiff)
  #print(sumsP)
  writeLines("\n")
}

mergeScenariosDf= function(scenarios,TU=F){
  scenarioCapacitiesSub= list()
  scenarioProductionsSub = list()
  scenarioProductionsUse = list()
  scenarioPowerBalance = list()
  
  if(TU==T){
    for(i in 1:length(scenarios)){
      scenarios[i]=paste("TU\\",scenarios[i],sep="")
    }
  }else if(Signy==T){
    for(i in 1:length(scenarios)){
      scenarios[i]=paste("Signy\\",scenarios[i],sep="")
    }
  }
  c=0
  for(scenario in scenarios){
    c=c+1
    Capacities=read.csv(paste(scenario,'Capacity.csv',sep=""),check.names = FALSE,sep = sep)
    Productions=read.csv(paste(scenario,'Production.csv',sep=""),check.names = FALSE, sep = sep)
    
    Capacities$Scenario=scenario
    Productions$Scenario=scenario
    
    names(Capacities)[names(Capacities) == "Year"] <- "2015"
    names(Capacities)[names(Capacities) == "Value"] <- "2020"

    
    Capacities[is.na(Capacities)] = 0
    Productions[is.na(Productions)] = 0
    
    #sumAll(Capacities,Productions, scenario)
    #next

    
    Capacities=Capacities[Capacities$Region==region,]
    Productions=Productions[Productions$Region==region,]
    

    CapacitiesSub=Capacities[which(Capacities$Type=="TotalCapacity" 
                                   & (Capacities$Category=="Power")),]
                                   #|Capacities$Category=="Industry"
                                   #|Capacities$Category=="Buildings"
                                   #|Capacities$Category=="Transportation")) ,]
    ProductionsSub=Productions[which(Productions$Type=="Production"
                                     & (Productions$Category=="Power")),]
                                     #|Productions$Category=="Industry"
                                      # |Productions$Category=="Buildings"
                                       #|Productions$Category=="Transportation")),]
    
    #if(AggrigateTechnologies==T){
      CapacitiesSubAgg=renameTechnologies(CapacitiesSub, technologies)
      ProductionsSubAgg=renameTechnologies(ProductionsSub, technologies)
    #}
    hydrogenData=renameTechnologies(Productions, h2)
      
    ProductionsUse=Productions[Productions$Type=="Use",]
    ProductionsPowerUse = ProductionsUse %>% filter_all(any_vars(. %in% c('Power')))
    years=str(seq(2015,2050,5))
    Productions=Productions %>% filter_all(any_vars(. %in% c('Power')))
    PowerBalance=aggregate(.~Type+Scenario,data=Productions[,-c(1:6,8)],FUN = sum)
    PowerBalance=mutate_if(PowerBalance, is.numeric, ~. / 3.6)
    
    UseOftechnologies = aggregate(.~Technology+Scenario,data=ProductionsPowerUse[,c(3,9:17)],FUN = sum)
    UseOftechnologies=mutate_if(UseOftechnologies, is.numeric, ~. / 3.6)
    UseOftechnologiesAgg = renameTechnologies(UseOftechnologies, technologyUses)
  
    #hydrogenData=aggregate(.~Technology+Scenario+Type,data=hydrogenData[,c(3,9:17)],FUN = sum)
    
    scenarioCapacitiesSub[[c]]=CapacitiesSubAgg
    scenarioProductionsSub[[c]]=ProductionsSubAgg
    
    scenarioProductionsUse[[c]]=ProductionsPowerUse
    scenarioPowerBalance[[c]]=PowerBalance
    
  }
  mergedCapacitiesSubdf <- do.call(rbind, scenarioCapacitiesSub)
  mergedProductionsSubdf <- do.call(rbind, scenarioProductionsSub)
  mergedProductionsUse <- do.call(rbind, scenarioProductionsUse)
  totalPowerBalance <- do.call(rbind, scenarioPowerBalance)
  return (list(mergedCapacitiesSubdf, mergedProductionsSubdf, mergedProductionsUse, totalPowerBalance, UseOftechnologiesAgg))
}

for(i in regions){
  region=i
  dfList=mergeScenariosDf(scenarios,TU)
  mergedCapacitiesSubdf <- dfList[[1]]
  mergedProductionsSubdf <- dfList[[2]]
  mergedProductionsUse <- dfList[[3]]
  totalPowerBalance <- dfList[[4]]
  useOftechnologies <- dfList[[5]]
   
  mergedPowerCapacities=mergedCapacitiesSubdf[mergedCapacitiesSubdf$Category=="Power",]
  mergedPowerProductions=mergedProductionsSubdf[mergedProductionsSubdf$Category=="Power",]

  
  totalPowerCapacities = totals(mergedPowerCapacities[,-c(1,2,4)])
  totalPowerProductions = totals(mergedPowerProductions[,-c(1,2,4:8)],TRUE)
  totalUseOftechnologies=totals(useOftechnologies)
  
  
  names=c("totalPowerCapacities.csv","totalPowerProductions.csv")#,"totalPowerEmissions.csv","totalPowerCosts.csv")
  
  if(TU==T){
    write.csv(totalPowerCapacities,paste("Tables\\TUresults\\totalPowerCapacities",region,".csv",sep="")
              ,row.names=FALSE, quote = FALSE)
    write.csv(totalPowerProductions,paste("Tables\\TUresults\\totalPowerProductions",region,".csv",sep="")
              ,row.names=FALSE, quote = FALSE)
    write.csv(totalPowerBalance,paste("Tables\\TUresults\\PowerBalance",region,".csv",sep=""),
              row.names=FALSE, quote = FALSE)
    write.csv(totalUseOftechnologies,paste("Tables\\TUresults\\technologyUses",region,".csv",sep=""),
              row.names=FALSE, quote = FALSE)
  }else if(Signy ==T){
    write.csv(totalPowerCapacities,paste("Tables\\Signy\\totalPowerCapacities",region,".csv",sep=""),
              row.names=FALSE, quote = FALSE)
    write.csv(totalPowerProductions,paste("Tables\\Signy\\totalPowerProductions",region,".csv",sep="")
              ,row.names=FALSE, quote = FALSE)
    write.csv(totalPowerBalance,paste("Tables\\Signy\\PowerBalance",region,".csv",sep=""),
              row.names=FALSE, quote = FALSE)
    write.csv(totalUseOftechnologies,paste("Tables\\Signy\\technologyUses",region,".csv",sep=""),
              row.names=FALSE, quote = FALSE)
  }else{
    write.csv(totalPowerCapacities,paste("Tables\\totalPowerCapacities",region,".csv",sep="")
              ,row.names=FALSE, quote = FALSE)
    write.csv(totalPowerProductions,paste("Tables\\totalPowerProductions",region,".csv",sep="")
               ,row.names=FALSE, quote = FALSE)
    # write.csv(totalPowerBalance,paste("Tables\\PowerBalance",region,".csv",sep=""),
    #           row.names=FALSE, quote = FALSE)
    # write.csv(totalUseOftechnologies,paste("Tables\\technologyUses",region,".csv",sep=""),
    #           row.names=FALSE, quote = FALSE)

  }
}

View(totalPowerCapacities)
View(totalPowerProductions)
#View(totalProductionsUse)
View(totalPowerBalance)
View(totalUseOftechnologies)

balance=totalPowerBalance
balance$Type="Balance"
balance=aggregate(.~Scenario+Type,balance,sum)
totalPowerBalance=rbind(totalPowerBalance, balance)
totalPowerBalance$Scenario=NULL
plotfolder="plots\\"
scenario="GradualDevelopment"
source("PlottingFunctions.R")
plotCategories(totalPowerBalance,totalPowerBalance$Type, "Power Balance", "TWh","Type")

