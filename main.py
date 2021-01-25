# %%
import importlib
import pandas as pd
import os
import numpy as np
import glob
import plotingFunctions
importlib.reload(plotingFunctions)
from plotingFunctions import *
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"

os.chdir("C:\\Users\\ahsor\\Dropbox\\Masteroppgave\\PlotData")

#Read our new capacities
GDC=pd.read_csv("Rdomain\\Tables\\GD\\totalPowerCapacities.csv")
TFC=pd.read_csv("Rdomain\\Tables\\TF\\totalPowerCapacities.csv")
SCC=pd.read_csv("Rdomain\\Tables\\SC\\totalPowerCapacities.csv")
DTC=pd.read_csv("Rdomain\\Tables\\DT\\totalPowerCapacities.csv")

#Read our new productions
GDP=pd.read_csv("Rdomain\\Tables\\GD\\totalPowerProductions.csv")
SCP=pd.read_csv("Rdomain\\Tables\\SC\\totalPowerProductions.csv")
TFP=pd.read_csv("Rdomain\\Tables\\TF\\totalPowerProductions.csv")
DTP=pd.read_csv("Rdomain\\Tables\\DT\\totalPowerProductions.csv")

#Read TU Capacities
TU_GDC=pd.read_csv("Rdomain\\Tables\\GD\\VS_TUtotalPowerCapacities.csv")
TU_SCC=pd.read_csv("Rdomain\\Tables\\SC\\VS_TUtotalPowerCapacities.csv")

#Read TU productions
TU_GDP=pd.read_csv("Rdomain\\Tables\\GD\\VS_TUtotalPowerProductions.csv")
TU_SCP=pd.read_csv("Rdomain\\Tables\\SC\\VS_TUtotalPowerProductions.csv")

#Read our old capacities
GDC_Old=pd.read_csv("OldProjectResults\\GD\\GDtotalPowerCapacities.csv")
TFC_OLD=pd.read_csv("OldProjectResults\\TF\\TFtotalPowerCapacities.csv")

#Read our old productions
GDP_Old=pd.read_csv("OldProjectResults\\GD\\GDtotalPowerProductions.csv")


plotDfs([TFC, TFC_OLD], "TechnoFriendly Power Capacities [GW] New vs Old", False)
plotDfs([GDC, TU_GDC], "GradualDevelopment Power Capacities [GW] GG vs RR", False)
plotDfs([GDP, TU_GDP], "GradualDevelopment Power Productions [TWh] GG vs RR", False)
plotDfs([SCC, TU_SCC], "SocietalCommitment Power Capacities [GW] GG vs RR", False)
plotDfs([SCC, TU_SCC], "SocietalCommitment Power Productions [TWh] GG vs RR", False)
plotDfs([GDC, GDC_Old], "GradualDevelopment Power Capacities [GW] New vs Old", False)
plotDfs([GDP, GDP_Old], "GradualDevelopment Power Productions [TWh] New vs Old", False)



