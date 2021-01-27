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

os.chdir("C:\\Users\\ahsor\\Dropbox\\Masteroppgave\\PlotData")

# Read our new capacities
SCC = pd.read_csv("Rdomain\\Tables\\SC\\totalPowerCapacities.csv")
TFC = pd.read_csv("Rdomain\\Tables\\TF\\totalPowerCapacities.csv")
DTC = pd.read_csv("Rdomain\\Tables\\DT\\totalPowerCapacities.csv")
GDC = pd.read_csv("Rdomain\\Tables\\GD\\totalPowerCapacities.csv")

# Read our new productions
SCP = pd.read_csv("Rdomain\\Tables\\SC\\totalPowerProductions.csv")
TFP = pd.read_csv("Rdomain\\Tables\\TF\\totalPowerProductions.csv")
DTP = pd.read_csv("Rdomain\\Tables\\DT\\totalPowerProductions.csv")
GDP = pd.read_csv("Rdomain\\Tables\\GD\\totalPowerProductions.csv")

# Read TU Capacities
TU_SCC = pd.read_csv("Rdomain\\Tables\\TUresults\\SC\\totalPowerCapacities.csv")
TU_TFC = pd.read_csv("Rdomain\\Tables\\TUresults\\TF\\totalPowerCapacities.csv")
TU_DTC = pd.read_csv("Rdomain\\Tables\\TUresults\\DT\\totalPowerCapacities.csv")
TU_GDC = pd.read_csv("Rdomain\\Tables\\TUresults\\GD\\totalPowerCapacities.csv")

# Read TU productions
TU_SCP = pd.read_csv("Rdomain\\Tables\\TUresults\\SC\\totalPowerProductions.csv")
TU_TFP = pd.read_csv("Rdomain\\Tables\\TUresults\\TF\\totalPowerProductions.csv")
TU_DTP = pd.read_csv("Rdomain\\Tables\\TUresults\\DT\\totalPowerProductions.csv")
TU_GDP = pd.read_csv("Rdomain\\Tables\\TUresults\\GD\\totalPowerProductions.csv")

# Read TU CPLEX results
TU_CPLEX_DTC = pd.read_csv("Rdomain\\Tables\\TUresults\\DT_CPLEX\\totalPowerCapacities.csv")
TU_CPLEX_DTP = pd.read_csv("Rdomain\\Tables\\TUresults\\DT_CPLEX\\totalPowerProductions.csv")

# Read our old capacities
TFC_Old = pd.read_csv("OldProjectResults\\TF\\TFtotalPowerCapacities.csv")
DTC_Old = pd.read_csv("OldProjectResults\\DT\\DTtotalPowerCapacities.csv")
GDC_Old = pd.read_csv("OldProjectResults\\GD\\GDtotalPowerCapacities.csv")

# Read our old productions
TFP_Old = pd.read_csv("OldProjectResults\\TF\\TFtotalPowerProductions.csv")
DT_Old = pd.read_csv("OldProjectResults\\DT\\DTtotalPowerProductions.csv")
GDP_Old = pd.read_csv("OldProjectResults\\GD\\GDtotalPowerProductions.csv")


#All GG
"""plotDfs([SCC,TFC,DTC,GDC], "Power Capacities [GW] All scenarios [SC,TF,DT,GD]", False)
plotDfs([SCP,TFP,DTP,GDP], "Power Productions [TWh] All scenarios [SC,TF,DT,GD]", False)


# GG VS RR
plotDfs([GDC, TU_GDC], "GradualDevelopment Power Capacities [GW] GG vs RR", False)
plotDfs([GDP, TU_GDP], "GradualDevelopment Power Productions [TWh] GG vs RR", False)
plotDfs([SCC, TU_SCC], "SocietalCommitment Power Capacities [GW] GG vs RR", False)
plotDfs([SCP, TU_SCP], "SocietalCommitment Power Productions [TWh] GG vs RR", False)

# GG_New vs GG_Old
plotDfs([GDC, GDC_Old], "GradualDevelopment Power Capacities [GW] New vs Old", False)
plotDfs([GDP, GDP_Old], "GradualDevelopment Power Productions [TWh] New vs Old", False)
plotDfs([TFC, TFC_Old], "TechnoFriendly Power Capacities [GW] New vs Old", False)
plotDfs([TFP, TFP_Old], "TechnoFriendly Power Productions [GW] New vs Old", False)"""

#Comparing solvers
plotDfs([DTC, TU_DTC, TU_CPLEX_DTC], "DirectedTransition Power Capacities [GW] GG vs RR_Gurobi vs RR_CPLEX", False)
plotDfs([DTP,TU_DTP,TU_CPLEX_DTP],"DirectedTransition Power Productions [TWh] GG vs RR_Gurobi vs RR_CPLEX", False)