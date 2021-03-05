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
# SCC = pd.read_csv("Rdomain\\Tables\\SC\\totalPowerCapacities.csv")
# TFC = pd.read_csv("Rdomain\\Tables\\TF\\totalPowerCapacities.csv")
# DTC = pd.read_csv("Rdomain\\Tables\\DT\\totalPowerCapacities.csv")
DTC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"DT\\totalPowerCapacitiesNO.csv")
GDC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerCapacitiesNO.csv")

# Read our new productions
# SCP = pd.read_csv("Rdomain\\Tables\\SC\\totalPowerProductions.csv")
# TFP = pd.read_csv("Rdomain\\Tables\\TF\\totalPowerProductions.csv")
# DTP = pd.read_csv("Rdomain\\Tables\\DT\\totalPowerProductions.csv")
DTP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"DT\\totalPowerProductionsNO.csv")
GDP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerProductionsNO.csv")

# # Read TU Capacities
# TU_SCC = pd.read_csv("Rdomain\\Tables\\TUresults\\SC\\totalPowerCapacitiesNO.csv")
# TU_TFC = pd.read_csv("Rdomain\\Tables\\TUresults\\TF\\totalPowerCapacities.csv")
# TU_DTC = pd.read_csv("Rdomain\\Tables\\TUresults\\DT\\totalPowerCapacities.csv")
TU_DTC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TUresults\\DT\\totalPowerCapacitiesNO.csv")
TU_GDC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TUresults\\GD\\totalPowerCapacitiesNO.csv")
#TU_GDC_Old = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TUresults\\GD\\Old\\totalPowerCapacities.csv")
#
# # Read TU productions
# TU_SCP = pd.read_csv("Rdomain\\Tables\\TUresults\\SC\\totalPowerProductionsNO.csv")
# TU_TFP = pd.read_csv("Rdomain\\Tables\\TUresults\\TF\\totalPowerProductions.csv")
# TU_DTP = pd.read_csv("Rdomain\\Tables\\TUresults\\DT\\totalPowerProductions.csv")
TU_DTP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TUresults\\DT\\totalPowerProductionsNO.csv")
TU_GDP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TUresults\\GD\\totalPowerProductionsNO.csv")
#TU_GDP_Old = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TUresults\\GD\\Old\\totalPowerProductions.csv")
#
# # Read TF regions
# TF_NO1C = pd.read_csv("Rdomain\\Tables\\TF\\totalPowerCapacitiesNO1.csv")
# TF_NO2C = pd.read_csv("Rdomain\\Tables\\TF\\totalPowerCapacitiesNO2.csv")
#
# TF_NO1P = pd.read_csv("Rdomain\\Tables\\TF\\totalPowerProductionsNO1.csv")
# TF_NO2P = pd.read_csv("Rdomain\\Tables\\TF\\totalPowerProductionsNO2.csv")

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
# Si_GDC = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\totalPowerCapacities.csv")
# Si_GDP = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\totalPowerProductions.csv")
# Si_TFC = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\TF\\totalPowerCapacitiesNO.csv")
# Si_TFP = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\TF\\totalPowerProductionsNO.csv")
# Si_DTC = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\DT\\totalPowerCapacitiesNO.csv")
# Si_DTP = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\DT\\totalPowerProductionsNO.csv")
# Si_SCC = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\SC\\totalPowerCapacitiesNO.csv")
# Si_SCP = pd.read_csv("Rdomain\\Tables\\" + Alltech + "Signy\\SC\\totalPowerProductionsNO.csv")

# Read MiddleEarth files
# MC=[pd.read_csv("Rdomain\\Tables\\"+Alltech+"MiddleEarth\\totalPowerCapacitiesMordor"+str(i)+".csv") for i in range(1,6)]
# MP=[pd.read_csv("Rdomain\\Tables\\"+Alltech+"MiddleEarth\\totalPowerProductionsMordor"+str(i)+".csv") for i in range(1,6)]

# Read GD files
# NO_GDC = [pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerCapacities.csv")]#+str(i)+".csv") for i in range(1,6)]
# NO_GDP = [pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerProductions.csv")]#+str(i)+".csv") for i in range(1,6)]

# Read PowerBalance
i=""
NO_DT_PB = [pd.read_csv("Rdomain\\Tables\\" + Alltech + "DT\\PowerBalanceNO" + str(i) + ".csv").rename(
    columns={"Type": "Technology"})#.apply(lambda x: x.abs() if np.issubdtype(x.dtype, np.number) else x)
            ]#for i in range(1, 6)]
plotDfs(NO_DT_PB, "Power Balance [Twh] Directed Transition",False)
plotDfs([DTC, TU_DTC], "Power Capacities [GW] Our vs TU_New" ,False)
plotDfs([DTP,TU_DTP], "Power Productions [TWh] Our vs TU_New",False)

"""

# All GG
plotDfs([SCC,TFC,DTC,GDC], "Power Capacities [GW] All scenarios [SC,TF,DT,GD]", False)
plotDfs([SCP,TFP,DTP,GDP], "Power Productions [TWh] All scenarios [SC,TF,DT,GD]", False)

# Mordor
plotDfs(MC, "Mordor [1-5] Power Capacities [GW]", False)
plotDfs(MP, "Mordor [1-5] Power Productions [TWh]", False)


# Signy vs TU
plotDfs([Si_GDC, TU_GDC], "GradualDevelopment Power Capacities [GW] Signy vs TU", False)
plotDfs([Si_GDP, TU_GDP], "GradualDevelopment Power Productions [TWh] Signy vs TU", False)
plotDfs([Si_TFC, TU_TFC], "TechnoFriendly Power Capacities [GW] Signy vs TU", False)
plotDfs([Si_TFP, TU_TFP], "TechnoFriendly Power Productions [TWh] Signy vs TU", False)
plotDfs([Si_DTC, TU_DTC], "DirectedTransition Power Capacities [GW] Signy vs TU", False)
plotDfs([Si_DTP, TU_DTP], "DirectedTransition Power Productions [TWh] Signy vs TU", False)
plotDfs([Si_SCC, TU_SCC], "SocietalCommitment Power Capacities [GW] Signy vs TU", False)
plotDfs([Si_SCP, TU_SCP], "SocietalCommitment Power Productions [TWh] Signy vs TU", False)

# TechnoFriendlyRegions
plotDfs([TF_NO1C, TF_NO2C, Si_TFC], "TechnoFriendly Power Capacities [GW] NO1 vs NO2 vs Original", False)
plotDfs([TF_NO1P, TF_NO2P, Si_TFP], "TechnoFriendly Power Productions [GW] NO1 vs NO2 vs Original", False)

# GradualDevelopmentRegions
NO_GDC.append(Si_GDC)
NO_GDP.append(Si_GDP)
plotDfs(NO_GDC, "GradualDevelopment Power Capacities [GW] NO1-5 vs Original", False)
plotDfs(NO_GDP, "GradualDevelopment Power Productions [TWh] NO1-5 vs Original", False)



# GG VS RR

plotDfs([GDC, TU_GDC, Si_GDC], "GradualDevelopment Power Capacities [GW] GG vs RR vs Signy", False)
plotDfs([GDP, TU_GDP, Si_GDP], "GradualDevelopment Power Productions [TWh] GG vs RR vs Signy", False)

plotDfs([SCC, TU_SCC], "SocietalCommitment Power Capacities [GW] GG vs RR", False)
plotDfs([SCP, TU_SCP], "SocietalCommitment Power Productions [TWh] GG vs RR", False)

# GG_New vs GG_Old
plotDfs([GDC, GDC_Old], "GradualDevelopment Power Capacities [GW] New vs Old", False)
plotDfs([GDP, GDP_Old], "GradualDevelopment Power Productions [TWh] New vs Old", False)
plotDfs([TFC, TFC_Old], "TechnoFriendly Power Capacities [GW] New vs Old", False)
plotDfs([TFP, TFP_Old], "TechnoFriendly Power Productions [TWh] New vs Old", False)

#Comparing solvers
plotDfs([DTC, TU_DTC, TU_CPLEX_DTC], "DirectedTransition Power Capacities [GW] GG vs RR_Gurobi vs RR_CPLEX", False)
plotDfs([DTP,TU_DTP,TU_CPLEX_DTP],"DirectedTransition Power Productions [TWh] GG vs RR_Gurobi vs RR_CPLEX", False)

TU_DTC = pd.read_csv("Rdomain\\Tables\\TUresults\\totalPowerCapacities.csv")
TU_DTP = pd.read_csv("Rdomain\\Tables\\TUresults\\totalPowerProductions.csv")

plotDfs([TU_DTC], "DirectedTransition Power Capacities [GW] GG vs RR_Gurobi vs RR_CPLEX", False)
"""
