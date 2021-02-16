library(ggplot2)
library(scales)
library(plotly)
library(reshape2)
library(dplyr)
library(tidyverse)
library(knitr)
rm(list=ls())

scenario="GradualDevelopment" #Only needed for testing/debugging purposes
scenarios=c("GradualDevelopment")# SocietalCommitment 
technologies=c("PV","Hydro","Wind Onshore","Wind Offshore Deep","Wind Offshore Transitional") #All others are set to thermal
TU=F
Signy=T #Makes read csv separatpr ";"
region="NO"

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
      df[row,col] = "Thermal"
    }
  }
  return (df)
}

getMissingTechnologies=function(df){
  for(tech in technologies){
    if(!any(df$Technology == tech)){
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

totals=function(df,PJ2Twh=FALSE){
  df=aggregate(.~Scenario+Technology,data=df, FUN=sum)
  if(nrow(df)>length(scenarios)){
    tot=df[,-2]
    tot=aggregate(.~Scenario,tot,sum)
    tot$Technology="Sum" #Caclulate sum
    df=rbind(df, tot)
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
  #scenarioCostsSub = list()
  #scenarioEmissionsSub = list()
  sep=","
  if(TU==T){
    for(i in 1:length(scenarios)){
      scenarios[i]=paste("TU\\",scenarios[i],sep="")
    }
  }else if(Signy==T){
    sep=";"
    for(i in 1:length(scenarios)){
      scenarios[i]=paste("Signy\\",scenarios[i],sep="")
    }
  }
  c=0
  for(scenario in scenarios){
    c=c+1
    Capacities=read.csv(paste(scenario,'Capacity.csv',sep=""),check.names = FALSE,sep = sep)
    Productions=read.csv(paste(scenario,'Production.csv',sep=""),check.names = FALSE, sep = sep)
    #Costs=read.csv(paste(scenario,'Costs.csv',sep=""),check.names = FALSE)
    #Emissions=read.csv(paste(scenario,'Emissions.csv',sep=""),check.names = FALSE)
    
    Capacities$Scenario=scenario
    Productions$Scenario=scenario
    #Costs$Scenario=scenario
    #Emissions$Scenario=scenario
    
    names(Capacities)[names(Capacities) == "Year"] <- "2015"
    names(Capacities)[names(Capacities) == "Value"] <- "2020"
    #names(Costs)[names(Costs) == "Year"] <- "2015"
    #names(Costs)[names(Costs) == "Value"] <- "2020"
    #names(Emissions)[names(Emissions) == "Year"] <- "2015"
    #names(Emissions)[names(Emissions) == "Value"] <- "2020"

    
    Capacities[is.na(Capacities)] = 0
    Productions[is.na(Productions)] = 0
    #Costs[is.na(Costs)] = 0
    #Emissions[is.na(Emissions)] = 0
    
    CapacitiesSub=Capacities[which(Capacities$Region==region 
                                   & Capacities$Type=="TotalCapacity" 
                                   & (Capacities$Category=="Power"
                                   |Capacities$Category=="Industry"
                                   |Capacities$Category=="Buildings"
                                   |Capacities$Category=="Transportation")) ,]
    ProductionsSub=Productions[which(Productions$Region==region 
                                     & Productions$Type=="Production"
                                     & (Productions$Category=="Power"
                                     |Productions$Category=="Industry"
                                       |Productions$Category=="Buildings"
                                       |Productions$Category=="Transportation")),]
    
    # CostsSub=Costs[which(Costs$Region== 
    #                      & (Costs$Category=="Power"
    #                         |Costs$Category=="Industry"
    #                         |Costs$Category=="Buildings"
    #                         |Costs$Category=="Transportation")),]
    # EmissionsSub=Emissions[which(Emissions$Region== 
    #                              & (Emissions$Category=="Power"
    #                              |Emissions$Category=="Industry"
    #                              |Emissions$Category=="Buildings"
    #                              |Emissions$Category=="Transportation")),]
    
    CapacitiesSub=renameTechnologies(CapacitiesSub)
    ProductionsSub=renameTechnologies(ProductionsSub)
    #CostsSub=renameTechnologies(CostsSub)
    #EmissionsSub=renameTechnologies(EmissionsSub)
    # 
    # if(is.null(EmissionsSub$`2045`)){
    #   EmissionsSub$`2045`=0
    # }
    
    scenarioCapacitiesSub[[c]]=CapacitiesSub
    scenarioProductionsSub[[c]]=ProductionsSub
    #scenarioEmissionsSub[[c]]=EmissionsSub
    #scenarioCostsSub[[c]]=CostsSub
  }
  mergedCapacitiesSubdf <- do.call(rbind, scenarioCapacitiesSub)
  mergedProductionsSubdf <- do.call(rbind, scenarioProductionsSub)
  #mergedEmissionsSubdf <- do.call(rbind, scenarioEmissionsSub)
  #mergedCostsSubdf <- do.call(rbind, scenarioCostsSub)
  return (list(mergedCapacitiesSubdf,mergedProductionsSubdf))#,mergedEmissionsSubdf,mergedCostsSubdf))
}


dfList=mergeScenariosDf(scenarios,TU)
mergedCapacitiesSubdf <- dfList[[1]]
mergedProductionsSubdf <- dfList[[2]]
#mergedEmissionsSubdf <- dfList[[3]]
#mergedCostsSubdf <- dfList[[4]]

# View(mergedPowerCapacitiesSubdf)
# View(mergedPowerProductionsSubdf)
# View(mergedPowerEmissionsSubdf)
# View(mergedPowerCostsSubdf)
 
mergedPowerCapacities=mergedCapacitiesSubdf[mergedCapacitiesSubdf$Category=="Power",]
mergedPowerProductions=mergedProductionsSubdf[mergedProductionsSubdf$Category=="Power",]
# mergedPowerEmissions=mergedEmissionsSubdf[mergedEmissionsSubdf$Category=="Power",]
# mergedPowerCosts=mergedCostsSubdf[mergedCostsSubdf$Category=="Power",]
# View(mergedPowerCapacities)
# View(mergedPowerProductions)
# View(mergedPowerEmissions)
# View(mergedPowerCosts)

totalPowerCapacities = totals(mergedPowerCapacities[,-c(1,2,4)])
totalPowerProductions = totals(mergedPowerProductions[,-c(1,2,4:8)],TRUE)
# totalPowerEmissions = totals(mergedPowerEmissions[,-c(1:3,5)])
# totalPowerCosts =totals(mergedPowerCosts[,-c(1,2,4)])

# View(totalPowerCapacities)
# View(totalPowerProductions)
# View(totalPowerEmissions)
# View(totalPowerCosts)

names=c("totalPowerCapacities.csv","totalPowerProductions.csv")#,"totalPowerEmissions.csv","totalPowerCosts.csv")

if(TU==T){
  write.csv(totalPowerCapacities,"Tables\\TUresults\\totalPowerCapacities.csv",row.names=FALSE, quote = FALSE)
  write.csv(totalPowerProductions,"Tables\\TUresults\\totalPowerProductions.csv",row.names=FALSE, quote = FALSE)
  #write.csv(totalPowerEmissions,"Tables\\TUresults\\totalPowerEmissions.csv",row.names=FALSE, quote = FALSE)
  #write.csv(totalPowerCosts,"Tables\\TUresults\\totalPowerCosts.csv",row.names=FALSE, quote = FALSE)
}else if(Signy ==T){
  write.csv(totalPowerCapacities,"Tables\\Signy\\totalPowerCapacities.csv",row.names=FALSE, quote = FALSE)
  write.csv(totalPowerProductions,"Tables\\Signy\\totalPowerProductions.csv",row.names=FALSE, quote = FALSE)
}else{
  write.csv(totalPowerCapacities,"Tables\\totalPowerCapacities.csv",row.names=FALSE, quote = FALSE)
  write.csv(totalPowerProductions,"Tables\\totalPowerProductions.csv",row.names=FALSE, quote = FALSE)
  #write.csv(totalPowerEmissions,"Tables\\totalPowerEmissions.csv",row.names=FALSE, quote = FALSE)
  #write.csv(totalPowerCosts,"Tables\\totalPowerCosts.csv",row.names=FALSE, quote = FALSE)
}

#df=totalPowerCapacities
#df=year2Col(totalPowerCapacities)
#View(df)

