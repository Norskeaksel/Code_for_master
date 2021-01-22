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

GDC=pd.read_csv("Rdomain\\Tables\\GD\\totalPowerCapacities.csv")
TU_GDC=pd.read_csv("Rdomain\\Tables\\GD\\VS_TUtotalPowerCapacities.csv")
dfs=[GDC,TU_GDC]#TFC,DTC,
reproduction(dfs,"GradualDevelopment Power Capacities [GW] GG vs RR", False)
GDP=pd.read_csv("Rdomain\\Tables\\GD\\totalPowerProductions.csv")
TU_GDP=pd.read_csv("Rdomain\\Tables\\GD\\VS_TUtotalPowerProductions.csv")
dfs=[GDP,TU_GDP]
reproduction(dfs,"GradualDevelopment Power Productions [TWh] GG vs RR", False)

SCC=pd.read_csv("Rdomain\\Tables\\SC\\totalPowerCapacities.csv")
TU_SCC=pd.read_csv("Rdomain\\Tables\\SC\\VS_TUtotalPowerCapacities.csv")
dfs=[SCC,TU_SCC]#TFC,DTC,
reproduction(dfs,"SocietalCommitment Power Capacities [GW] GG vs RR", False)
SCP=pd.read_csv("Rdomain\\Tables\\SC\\totalPowerProductions.csv")
TU_SCP=pd.read_csv("Rdomain\\Tables\\SC\\VS_TUtotalPowerProductions.csv")
dfs=[SCC,TU_SCC]#TFC,DTC,
reproduction(dfs,"SocietalCommitment Power Productions [TWh] GG vs RR", False)