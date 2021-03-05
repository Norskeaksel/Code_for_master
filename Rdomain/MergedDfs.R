library(ggplot2)
library(scales)
library(plotly)
library(reshape2)
library(dplyr)
library(tidyverse)
library(knitr)
rm(list=ls())

scenario="GradualDevelopment" #Only needed for testing/debugging purposes
scenarios=c("GradualDevelopment")#MiddleEarth")# GradualDevelopment, SocietalCommitment, TechnoFriendly
#technologies=c("PV","Hydro","Wind Onshore","Wind Offshore Deep","Wind Offshore Transitional") #All others are set to thermal
technologies=c("P_Biomass","P_Gas","RES_Hydro_Large","RES_Hydro_Small","RES_PV_Rooftop_Commercial",
               "RES_PV_Rooftop_Residential","RES_PV_Utility_Avg","RES_PV_Utility_Inf","RES_PV_Utility_Opt",
               "RES_Wind_Offshore_Deep","RES_Wind_Offshore_Transitional","RES_Wind_Offshore_Deep",
               "RES_Wind_Onshore_Avg","RES_Wind_Onshore_Opt")
TU=F
Signy=F
AggrigateTechnologies=T
regions=c("NO")#1","NO2","NO3","NO4","NO5")
sep=","


toThermal=function(df){
  col="Technology"
  for (row in 1:nrow(df)){
    makeThermal=TRUE
    for(tech in technologies){
      if(df[row,col]==tech){
        makeThermal=FALSE
        break
      }
    }
    if(makeThermal){
      print(paste("Make Other: ",df[row,col]))
      df[row,col] = "Other"
    }
  }
  return (df)
}

getMissingTechnologies=function(df){
  for(tech in technologies){
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

renameTechnologies=function(df){
  for(tech in technologies){
    lastName=tail(strsplit(tech, " ")[[1]],1)
    regex=paste(".*",lastName,".*",sep="")
    #print(regex)
    df$Technology = sub(regex, tech, df$Technology)
  }
  df = toThermal(df)
  df = getMissingTechnologies(df)
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
    
    if(AggrigateTechnologies==T){
      CapacitiesSub=renameTechnologies(CapacitiesSub)
      ProductionsSub=renameTechnologies(ProductionsSub)
    }
    
    ProductionsUse=Productions[Productions$Type=="Use",]
    years=str(seq(2015,2050,5))
    Productions=Productions %>% filter_all(any_vars(. %in% c('Power')))
    PowerBalance=aggregate(.~Type+Scenario,data=Productions[,-c(1:6,8)],FUN = sum)
    PowerBalance=mutate_if(PowerBalance, is.numeric, ~. / 3.6)
    #ProductionsUseOftechnologies = aggregate(.~Technology+Scenario,data=ProductionsUse[,c(3,10:17)],FUN = sum)
  
    scenarioCapacitiesSub[[c]]=CapacitiesSub
    scenarioProductionsSub[[c]]=ProductionsSub
    
    scenarioProductionsUse[[c]]=ProductionsUse
    scenarioPowerBalance[[c]]=PowerBalance
    
  }
  mergedCapacitiesSubdf <- do.call(rbind, scenarioCapacitiesSub)
  mergedProductionsSubdf <- do.call(rbind, scenarioProductionsSub)
  mergedProductionsUse <- do.call(rbind, scenarioProductionsUse)
  totalPowerBalance <- do.call(rbind, scenarioPowerBalance)
  return (list(mergedCapacitiesSubdf, mergedProductionsSubdf, mergedProductionsUse, totalPowerBalance))
}

for(i in regions){
  region=i
  dfList=mergeScenariosDf(scenarios,TU)
  mergedCapacitiesSubdf <- dfList[[1]]
  mergedProductionsSubdf <- dfList[[2]]
  mergedProductionsUse <- dfList[[3]]
  totalPowerBalance <- dfList[[4]]
  #totalProductionsUseOftechnologies <- dfList[[5]]
   
  mergedPowerCapacities=mergedCapacitiesSubdf[mergedCapacitiesSubdf$Category=="Power",]
  mergedPowerProductions=mergedProductionsSubdf[mergedProductionsSubdf$Category=="Power",]

  
  totalPowerCapacities = totals(mergedPowerCapacities[,-c(1,2,4)])
  totalPowerProductions = totals(mergedPowerProductions[,-c(1,2,4:8)],TRUE)
  
  
  names=c("totalPowerCapacities.csv","totalPowerProductions.csv")#,"totalPowerEmissions.csv","totalPowerCosts.csv")
  
  if(TU==T){
    write.csv(totalPowerCapacities,paste("Tables\\TUresults\\totalPowerCapacities",region,".csv",sep="")
              ,row.names=FALSE, quote = FALSE)
    write.csv(totalPowerProductions,paste("Tables\\TUresults\\totalPowerProductions",region,".csv",sep="")
              ,row.names=FALSE, quote = FALSE)
    write.csv(totalPowerBalance,paste("Tables\\TUresults\\PowerBalance",region,".csv",sep=""),
              row.names=FALSE, quote = FALSE)
  }else if(Signy ==T){
    write.csv(totalPowerCapacities,paste("Tables\\Signy\\totalPowerCapacities",region,".csv",sep=""),
              row.names=FALSE, quote = FALSE)
    write.csv(totalPowerProductions,paste("Tables\\Signy\\totalPowerProductions",region,".csv",sep="")
              ,row.names=FALSE, quote = FALSE)
    write.csv(totalPowerBalance,paste("Tables\\Signy\\PowerBalance",region,".csv",sep=""),
              row.names=FALSE, quote = FALSE)
  }else{
    write.csv(totalPowerCapacities,paste("Tables\\totalPowerCapacities",region,".csv",sep="")
              ,row.names=FALSE, quote = FALSE)
    write.csv(totalPowerProductions,paste("Tables\\totalPowerProductions",region,".csv",sep="")
              ,row.names=FALSE, quote = FALSE)
    write.csv(totalPowerBalance,paste("Tables\\PowerBalance",region,".csv",sep=""),
              row.names=FALSE, quote = FALSE)

  }
}

View(totalPowerCapacities)
#View(totalPowerProductions)
#View(totalProductionsUse)

View(totalPowerBalance)
balance=totalPowerBalance
balance$Type="Balance"
balance=aggregate(.~Scenario+Type,balance,sum)
totalPowerBalance=rbind(totalPowerBalance, balance)
totalPowerBalance$Scenario=NULL
plotfolder="plots\\"
scenario="GradualDevelopment"
source("PlottingFunctions.R")
plotCategories(totalPowerBalance,totalPowerBalance$Type, "Power Balance", "TWh","Type")


