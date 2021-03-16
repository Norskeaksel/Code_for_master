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

Alltech = "Alltech\\"
# Read our new capacities
SCC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"SC\\totalPowerCapacitiesNO.csv")
TFC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TF\\totalPowerCapacitiesNO.csv")
DTC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"DT\\totalPowerCapacitiesNO.csv")
GDC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerCapacitiesNO.csv")

# Read our new productions
SCP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"SC\\totalPowerProductionsNO.csv")
TFP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TF\\totalPowerProductionsNO.csv")
DTP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"DT\\totalPowerProductionsNO.csv")
GDP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerProductionsNO.csv")

# # Read TU Capacities
TU_SCC = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"SC\\totalPowerCapacitiesNO.csv")
TU_TFC = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"TF\\totalPowerCapacitiesNO.csv")
TU_DTC = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"DT\\totalPowerCapacitiesNO.csv")
TU_GDC = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"GD\\totalPowerCapacitiesNO.csv")
# TU_GDC_Old = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TUresults\\GD\\Old\\totalPowerCapacities.csv")
#
# # Read TU productions
TU_TFP = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"TF\\totalPowerProductionsNO.csv")
TU_SCP = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"SC\\totalPowerProductionsNO.csv")
TU_DTP = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"DT\\totalPowerProductionsNO.csv")
TU_GDP = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"GD\\totalPowerProductionsNO.csv")
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
MC=[pd.read_csv("Rdomain\\Tables\\"+Alltech+"MiddleEarth\\totalPowerCapacitiesMordor"+str(i)+".csv") for i in range(1,6)]
MP=[pd.read_csv("Rdomain\\Tables\\"+Alltech+"MiddleEarth\\totalPowerProductionsMordor"+str(i)+".csv") for i in range(1,6)]

# Read GD files
# NO_GDC = [pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerCapacities.csv")]#+str(i)+".csv") for i in range(1,6)]
# NO_GDP = [pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerProductions.csv")]#+str(i)+".csv") for i in range(1,6)]

# Read PowerBalance
i=""
#NO_DT_PB = [pd.read_csv("Rdomain\\Tables\\" + Alltech + "DT\\PowerBalanceNO" + str(i) + ".csv").rename(
#    columns={"Type": "Technology"})#.apply(lambda x: x.abs() if np.issubdtype(x.dtype, np.number) else x)
#            ]for i in range(1, 6)]
# plotDfs(NO_DT_PB, "Power Balance [Twh] Directed Transition",False)

#plotDfs([TF_NO1C,TF_NO2C], "TF region Capacities", False)
plotDfs([DTC, TU_DTC], "Power Capacities [GW] Directed Transition Gams 34 vs TU" ,False)
plotDfs([DTP, TU_DTP], "Power Productions [TWh] Directed Transition Gams 34 vs TU",False)
plotDfs([GDC, TU_GDC], "GradualDevelopment Power Capacities [GW] Gams 34 vs TU", False)
plotDfs([GDP, TU_GDP], "GradualDevelopment Power Productions [TWh] Gams 34 vs TU", False)
plotDfs([TFC, TU_TFC], "TechnoFriendly Power Capacities [GW] Gams 34 vs TU", False)
plotDfs([TFP, TU_TFP], "TechnoFriendly Power Productions [TWh] Gams 34 vs TU", False)
plotDfs([SCC, TU_SCC], "SocietalCommitment Power Capacities [GW] GG vs RR", False)
plotDfs([SCP, TU_SCP], "SocietalCommitment Power Productions [TWh] GG vs RR", False)

#plotDfs([Si_TFC, TU_GDC_Old], "GradualDevelopment Power Capacities [GW] Signy vs TU", False)
#plotDfs([Si_TFP, TU_GDP_Old], "GradualDevelopment Power Productions [TWh] Signy vs TU", False)

#plotDfs(MC, "Mordor [1-5] Power Capacities [GW]", False)
#plotDfs(MP, "Mordor [1-5] Power Productions [TWh]", False)

