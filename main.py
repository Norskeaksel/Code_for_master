# %%
import importlib
import pandas as pd
import os
import numpy as np
import glob
import plotingFunctions

importlib.reload(plotingFunctions)
from plotingFunctions import *

# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

Alltech = "Alltech\\"#Alltech\\" #"HydroWindThermalPV\\" "Alltech\\"
# Read our new capacities
#SCC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"SC\\totalPowerCapacitiesNO.csv")
#TFC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TF\\totalPowerCapacitiesNO.csv")
#DTC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"DT\\totalPowerCapacitiesNO.csv")
GDC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerCapacitiesNO.csv")
#GDC48 = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerCapacities48.csv")
#CDCTrade= pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerCapacitiesTrade.csv")
CDCelectric= pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerCapacitiesElectric.csv")
CDCelectricTrade=pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerCapacitiesElectricTrade.csv")
#GDCDynamicCF = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerCapacitiesDynamicCF.csv")

# Read our new productions
#SCP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"SC\\totalPowerProductionsNO.csv")
#TFP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TF\\totalPowerProductionsNO.csv")
#DTP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"DT\\totalPowerProductionsNO.csv")
#GDPTrade = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerProductionsTrade.csv")
GDP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerProductionsNO.csv")
GDPelectric = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerProductionsElectric.csv")
GDPelectricTrade = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerProductionsElectricTrade.csv")
GDPtradeAndPower = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerProductionsTradeAndPower.csv")
#GDP48 = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerProductions48.csv")
#GDPDynamicCF = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerProductionsDynamicCF.csv")
#NVEP=pd.read_csv("Rdomain\\Tables\\"+Alltech+"NVE\\totalPowerProductions.csv")

# # Read TU Capacities
#TU_SCC = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"SC\\totalPowerCapacitiesNO.csv")
#TU_TFC = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"TF\\totalPowerCapacitiesNO.csv")
#TU_DTC = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"DT\\totalPowerCapacitiesNO.csv")
#TU_GDC = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"GD\\totalPowerCapacitiesNO.csv")
# TU_GDC_Old = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TUresults\\GD\\Old\\totalPowerCapacities.csv")
#
# # Read TU productions
#TU_TFP = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"TF\\totalPowerProductionsNO.csv")
#TU_SCP = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"SC\\totalPowerProductionsNO.csv")
#TU_DTP = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"DT\\totalPowerProductionsNO.csv")
#TU_GDP = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"GD\\totalPowerProductionsNO.csv")
#TU_GDP_Old = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TUresults\\GD\\Old\\totalPowerProductions.csv")
#
# # Read TF regions
TF_NO1C = pd.read_csv("Rdomain\\Tables\\TF\\totalPowerCapacitiesNO1.csv")
TF_NO2C = pd.read_csv("Rdomain\\Tables\\TF\\totalPowerCapacitiesNO2.csv")

TF_NO1P = pd.read_csv("Rdomain\\Tables\\TF\\totalPowerProductionsNO1.csv")
TF_NO2P = pd.read_csv("Rdomain\\Tables\\TF\\totalPowerProductionsNO2.csv")

# Read TU CPLEX results
# TU_CPLEX_DTC = pd.read_csv("Rdomain\\Tables\\TUresults\\DT_CPLEX\\totalPowerCapacities.csv")
# TU_CPLEX_DTP = pd.read_csv("Rdomain\\Tables\\TUresults\\DT_CPLEX\\totalPowerProductions.csv")

# Read our old capacities
# TFC_Old = pd.read_csv("OldProjectResults\\TF\\TFtotalPowerCapacities.csv")
# DTC_Old = pd.read_csv("OldProjectResults\\DT\\DTtotalPowerCapacities.csv")
# GDC_Old = pd.read_csv("OldProjectResults\\GD\\GDtotalPowerCapacities.csv")

# Read our old productions
# TFP_Old = pd.read_csv("OldProjectResults\\TF\\TFtotalPowerProductions.csv")
# DT_Old = pd.read_csv("OldProjectResults\\DT\\DTtotalPowerProductions.csv")
# GDP_Old = pd.read_csv("OldProjectResults\\GD\\GDtotalPowerProductions.csv")

# Read Signys files
# Si_GDC = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\GD\\totalPowerCapacities.csv")
# Si_GDP = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\GD\\totalPowerProductions.csv")
# Si_TFC = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\TF\\totalPowerCapacitiesNO.csv")
# Si_TFP = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\TF\\totalPowerProductionsNO.csv")
# Si_DTC = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\DT\\totalPowerCapacitiesNO.csv")
# Si_DTP = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\DT\\totalPowerProductionsNO.csv")
# Si_SCC = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\SC\\totalPowerCapacitiesNO.csv")
# Si_SCP = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\SC\\totalPowerProductionsNO.csv")

# Read MiddleEarth files
#MC=[pd.read_csv("Rdomain\\Tables\\"+Alltech+"MiddleEarth\\totalPowerCapacitiesMordor"+str(i)+".csv") for i in range(1,6)]
#MP=[pd.read_csv("Rdomain\\Tables\\"+Alltech+"MiddleEarth\\totalPowerProductionsMordor"+str(i)+".csv") for i in range(1,6)]

# Read GD files
# NO_GDC = [pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerCapacities.csv")]#+str(i)+".csv") for i in range(1,6)]
# NO_GDP = [pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerProductions.csv")]#+str(i)+".csv") for i in range(1,6)]

# Read PowerBalance
i=""
#NO_DT_PB = [pd.read_csv("Rdomain\\Tables\\" + Alltech + "DT\\PowerBalanceNO" + str(i) + ".csv").rename(
#    columns={"Type": "Technology"})#.apply(lambda x: x.abs() if np.issubdtype(x.dtype, np.number) else x)
#            ]for i in range(1, 6)]

# read technologyUses
'''i=""
NO_SC_use = [pd.read_csv("Rdomain\\Tables\\" + Alltech + "SC\\technologyUsesNO" + str(i) + ".csv") for _ in range(1,2)]
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
df=NO_SC_use[0]
for c in [c for c in df.columns if df[c].dtype in numerics]:
    df[c] = df[c].abs()
NO_SC_use=df'''
# plotDfs(NO_DT_PB, "Power Balance [Twh] Directed Transition",False)

#plotDfs([TF_NO1C,TF_NO2C], "TF region Capacities", False)
#plotDfs([DTC, TU_DTC], "Power Capacities [GW] Directed Transition Gams 34 vs TU" ,False)
#plotDfs([DTP, TU_DTP], "Power Productions [TWh] Directed Transition Gams 34 vs TU",False)
#plotDfs([GDC, CDCelectricTrade, ], "GradualDevelopment Power Capacities [GW] Original vs Updates vs NVE", False)
unit='TWh'
ascending=False
NVE=False
showNumbers=True
#plotDfs([GDPDynamicCF, GDPelectric, GDPelectricTrade, NVEP], "GradualDevelopment Power Productions ["+unit+"] Dynamic vs Electric vs Trade vs NVE", unit, ascending, NVE, showNumbers)
plotDfs([GDP, GDPelectricTrade, GDPtradeAndPower], "GradualDevelopment Power Productions ["+unit+"] Electric Trade vs Trade and power", unit, ascending, NVE, showNumbers)

#plotDfs([GDP,GDPDynamicCF,NVEP],"Original vs Dynamic vs NVE's Power Productions [TWh]",False,True)
#plotDfs([TFC, TU_TFC], "TechnoFriendly Power Capacities [GW] Gams 34 vs TU", False)
#plotDfs([TFP, TU_TFP], "TechnoFriendly Power Productions [TWh] Gams 34 vs TU", False)
#plotDfs([SCC, TU_SCC], "SocietalCommitment Power Capacities [GW] GG vs RR", False)
#plotDfs([SCP, TU_SCP], "SocietalCommitment Power Productions [TWh] GG vs RR", False)
#plotDfs([NO_SC_use], "SocietalCommitment Technology Power Use", False)

#plotDfs([Si_TFC, TU_GDC_Old], "GradualDevelopment Power Capacities [GW] Signy vs TU", False)
#plotDfs([Si_TFP, TU_GDP_Old], "GradualDevelopment Power Productions [TWh] Signy vs TU", False)

#plotDfs(MC, "Mordor [1-5] Power Capacities [GW]", False)
#plotDfs(MP, "Mordor [1-5] Power Productions [TWh]", False)

