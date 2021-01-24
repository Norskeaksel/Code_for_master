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

"""GDC=pd.read_csv("Rdomain\\Tables\\GD\\totalPowerCapacities.csv")
TU_GDC=pd.read_csv("Rdomain\\Tables\\GD\\VS_TUtotalPowerCapacities.csv")
reproduction([GDC,TU_GDC],"GradualDevelopment Power Capacities [GW] GG vs RR", False)

GDP=pd.read_csv("Rdomain\\Tables\\GD\\totalPowerProductions.csv")
TU_GDP=pd.read_csv("Rdomain\\Tables\\GD\\VS_TUtotalPowerProductions.csv")
reproduction([GDP,TU_GDP],"GradualDevelopment Power Productions [TWh] GG vs RR", False)

SCC=pd.read_csv("Rdomain\\Tables\\SC\\totalPowerCapacities.csv")
TU_SCC=pd.read_csv("Rdomain\\Tables\\SC\\VS_TUtotalPowerCapacities.csv")
reproduction([SCC,TU_SCC],"SocietalCommitment Power Capacities [GW] GG vs RR", False)

SCP=pd.read_csv("Rdomain\\Tables\\SC\\totalPowerProductions.csv")
TU_SCP=pd.read_csv("Rdomain\\Tables\\SC\\VS_TUtotalPowerProductions.csv")
reproduction([SCC,TU_SCC],"SocietalCommitment Power Productions [TWh] GG vs RR", False)

GDC=pd.read_csv("Rdomain\\Tables\\GD\\totalPowerCapacities.csv")
GDC_Old=pd.read_csv("OldProjectResults\\GD\\GDtotalPowerCapacities.csv")
reproduction([GDC,GDC_Old],"GradualDevelopment Power Capacities [GW] New vs Old", False)

GDP=pd.read_csv("Rdomain\\Tables\\GD\\totalPowerProductions.csv")
GDP_Old=pd.read_csv("OldProjectResults\\GD\\GDtotalPowerProductions.csv")
reproduction([GDP,GDP_Old],"GradualDevelopment Power Productions [TWh] New vs Old", False)"""

TFC=pd.read_csv("Rdomain\\Tables\\TF\\totalPowerCapacities.csv")
TFC_OLD=pd.read_csv("OldProjectResults\\TF\\TFtotalPowerCapacities.csv")
reproduction([TFC, TFC_OLD],"TechnoFriendly Power Capacities [GW] New vs Old", False)