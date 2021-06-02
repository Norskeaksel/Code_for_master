# %%
import importlib
import pandas as pd
import numbers
import os
import numpy as np
import glob
import plotingFunctions

importlib.reload(plotingFunctions)
from plotingFunctions import *

# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_i   nteractivity = "all"

def pr(df):
    print(df.to_string())


def insertRow(df, row):
    df.loc[-1] = row  # adding a row
    df.index = df.index + 1  # shifting index
    df = df.sort_index()  # sorting by index
    return df

def powerBalance(scenario,Alltech,folder,filename="PowerBalanceNO"):

    PB = pd.read_csv("Rdomain\\Tables\\" + Alltech + folder+scenario+"\\"+filename + ".csv").rename(
        columns={"Type": "Technology"})  # .apply(lambda x: x.abs() if np.issubdtype(x.dtype, np.number) else x)
    # for i in range(1, 6)]
    negativeExports = [-abs(i) if type(i) != str else i for i in list(PB.iloc[0, :])]
    PB.iloc[0] = negativeExports
    balance = [PB.iloc[1, i] + negativeExports[i] if i > 1 else negativeExports[i] for i in
               range(len(negativeExports))]
    balance[0] = 'Power Balance'
    balance_df = pd.DataFrame(balance).T
    balance_df.columns = PB.columns
    pr(balance_df)
    #PB = PB.append(pd.DataFrame(balance_df), ignore_index=True)
    Sum=[PB.iloc[0, i] + PB.iloc[3, i] if i > 1 else PB.iloc[0,i] for i in
               range(len(negativeExports))]



    Sum[0]="Sum"
    Sum2=[PB.iloc[1, i] + PB.iloc[2, i] if i > 1 else PB.iloc[0,i] for i in
               range(len(negativeExports))]
    Sum2[0]="Sum2"


    sum_df=pd.DataFrame(Sum).T
    sum_df.columns = PB.columns
    sum2_df=pd.DataFrame(Sum2).T
    sum2_df.columns=PB.columns


    PB = PB.append(pd.DataFrame(sum_df), ignore_index=True)
    PB = PB.append(pd.DataFrame(sum2_df), ignore_index=True)
    #PB = PB[~PB['Technology'].isin(["Export", "Import"])]
    return PB

Alltech = "" #"HydroWindThermalPV\\" "Alltech\\"
#Read our results
SCC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"SC\\totalPowerCapacitiesNO.csv")
TFC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TF\\totalPowerCapacitiesNO.csv")
DTC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"DT\\totalPowerCapacitiesNO.csv")
GDC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerCapacitiesNO.csv")

SCP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"SC\\totalPowerProductionsNO.csv")
TFP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"TF\\totalPowerProductionsNO.csv")
DTP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"DT\\totalPowerProductionsNO.csv")
GDP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"GD\\totalPowerProductionsNO.csv")

folder=""
TF_PB = powerBalance("TF", Alltech, folder)
SC_PB = powerBalance("SC", Alltech, folder)
DT_PB = powerBalance("DT", Alltech, folder)
GD_PB = powerBalance("GD", Alltech, folder)

TF_HB = powerBalance("TF", Alltech, folder,"h2NO")
SC_HB = powerBalance("SC", Alltech, folder,"h2NO")
DT_HB = powerBalance("DT", Alltech, folder,"h2NO")
GD_HB = powerBalance("GD", Alltech, folder,"h2NO")


# Read original results
OSCC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"Original\\SC\\totalPowerCapacitiesNO.csv")
OTFC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"Original\\TF\\totalPowerCapacitiesNO.csv")
ODTC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"Original\\DT\\totalPowerCapacitiesNO.csv")
OGDC = pd.read_csv("Rdomain\\Tables\\"+Alltech+"Original\\GD\\totalPowerCapacitiesNO.csv")

OSCP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"Original\\SC\\totalPowerProductionsNO.csv")
OTFP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"Original\\TF\\totalPowerProductionsNO.csv")
ODTP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"Original\\DT\\totalPowerProductionsNO.csv")
OGDP = pd.read_csv("Rdomain\\Tables\\"+Alltech+"Original\\GD\\totalPowerProductionsNO.csv")

folder="Original\\"
OTF_PB = powerBalance("TF", Alltech, folder)
OSC_PB = powerBalance("SC", Alltech, folder)
ODT_PB = powerBalance("DT", Alltech, folder)
OGD_PB = powerBalance("GD", Alltech, folder)

OTF_HB = powerBalance("TF", Alltech, folder,"h2NO")
OSC_HB = powerBalance("SC", Alltech, folder,"h2NO")
ODT_HB = powerBalance("DT", Alltech, folder,"h2NO")
OGD_HB = powerBalance("GD", Alltech, folder,"h2NO")

# Read TU Capacities
TU_SCC = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"SC\\totalPowerCapacitiesNO.csv")
TU_TFC = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"TF\\totalPowerCapacitiesNO.csv")
TU_DTC = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"DT\\totalPowerCapacitiesNO.csv")
TU_GDC = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"GD\\totalPowerCapacitiesNO.csv")

# Read TU productions
TU_TFP = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"TF\\totalPowerProductionsNO.csv")
TU_SCP = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"SC\\totalPowerProductionsNO.csv")
TU_DTP = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"DT\\totalPowerProductionsNO.csv")
TU_GDP = pd.read_csv("Rdomain\\Tables\\TUresults\\"+Alltech+"GD\\totalPowerProductionsNO.csv")

# Read NVE and Statnett
NVEP=pd.read_csv("Rdomain\\Tables\\"+Alltech+"NVE\\totalPowerProductions.csv")
NVEC=pd.read_csv("Rdomain\\Tables\\"+Alltech+"NVE\\totalPowerCapacities.csv")
StatnettP=pd.read_csv("Rdomain\\Tables\\"+Alltech+"Statnett\\totalPowerProductions.csv")
NVEuse=pd.read_csv("Rdomain\\Tables\\NVE\\powerUse.csv")
StatnettUse=pd.read_csv("Rdomain\\Tables\\Statnett\\powerUse.csv")
# Read GD files
#NO_GDC = [pd.read_csv("Rdomain\\Tables\\totalPowerCapacitiesNO"+str(i)+".csv") for i in range(1,6)]
#NO_GDP = [pd.read_csv("Rdomain\\Tables\\totalPowerProductionsNO"+str(i)+".csv") for i in range(1,6)]
#NO_GD_PB = [pd.read_csv("Rdomain\\Tables\\PowerBalanceNO"+str(i)+".csv") for i in range(1,6)]
#plotDfs(NO_GDC, "Dissaggregated Power capacities [GW] Directed Transition NO1-NO5 ",'GW', 0, None, 2)
#plotDfs(NO_GDP, "Dissaggregated Power productions [GW] Directed Transition NO1-NO5 ",'TWh', 0, None, 2)
#plotDfs(NO_GD_PB, "Dissaggregated Power Balances [TWh] Directed Transition NO1-NO5 ",'TWh', 0, None, 2)

# read technologyUses
'''i=""
NO_SC_use = [pd.read_csv("Rdomain\\Tables\\" + Alltech + "SC\\technologyUsesNO" + str(i) + ".csv") for _ in range(1,2)]
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
df=NO_SC_use[0]
for c in [c for c in df.columns if df[c].dtype in numerics]:
    df[c] = df[c].abs()
NO_SC_use=df'''

#Read UseOfFuels
#TFuse= pd.read_csv("Rdomain\\Tables\\TF\\UseOfFuelsNO.csv").rename(columns={"Fuel":"Technology"})
#TFuse.update(TFuse.select_dtypes(include=[np.number]).abs())

#h2NO=pd.read_csv("Rdomain\\Tables\\" + Alltech + "DT\\h2NO"+".csv").rename(columns={"Type": "Technology"})

#negativeExports = [-i if type(i)!=str else i for i in list(h2NO.iloc[0,:]) ]
#h2NO.iloc[0]=negativeExports

DTuse= pd.read_csv("Rdomain\\Tables\\GD\\UseOfFuelsNO.csv").rename(columns={"Fuel":"Technology"}).apply(lambda x: x.abs() if x.dtype.kind in 'iufc' else x)
#DTuse.update(DTuse.select_dtypes(include=[np.number]).abs())
DTuseOrg= pd.read_csv("Rdomain\\Tables\\Original\\GD\\UseOfFuelsNO.csv").rename(columns={"Fuel":"Technology"}).apply(lambda x: x.abs() if x.dtype.kind in 'iufc' else x)
#DTuseOrg.update(DTuse.select_dtypes(include=[np.number]).abs())


grouped = [v for k, v in DTuse.groupby('Category') if v.iloc[0, 0] in {"Buildings", "Industry", "Transportation","Power"}]
groupedorg = [v for k, v in DTuseOrg.groupby('Category') if v.iloc[0, 0] in {"Buildings", "Industry", "Transportation","Power"}]

ascending=False
years=['2015', '2020', '2025', '2030', '2035', '2040', '2045', '2050']
showNumbers=2 #0,1,2

#plotDfs([TU_DTC,TU_TFC,TU_SCC,TU_GDC], "TU Berlin  Power capacities [GW] Directed Transition vs Techno Friendly vs Societal Commitment vs Gradual Development",'GW', ascending, years, showNumbers)
#plotDfs([TU_DTP,TU_TFP,TU_SCP,TU_GDP], "TU Berlin  Power productions [TWh] Directed Transition vs Techno Friendly vs Societal Commitment vs Gradual Development",'TWh', ascending, years, showNumbers)

#plotDfs([ODTC, OTFC, OSCC, OGDC], "Original Power capacities in Directed Transition vs Techno Friendly vs Societal Commitment vs Gradual Development",'GW', ascending, years, showNumbers)
#plotDfs([ODTP, OTFP, OSCP, OGDP], "Original Power productions in Directed Transition vs Techno Friendly vs Societal Commitment vs Gradual Development",'TWh', ascending, years, showNumbers)

#plotDfs([DTC, TFC, SCC, GDC], "Modified Power capacities in Directed Transition vs Techno Friendly vs Societal Commitment vs Gradual Development",'GW', ascending, years, showNumbers)
#plotDfs([DTP, TFP, SCP, GDP], "Modified Power productions in Directed Transition vs Techno Friendly vs Societal Commitment vs Gradual Development",'TWh', ascending, years, showNumbers)

#plotDfs([ODTP, DTP, StatnettP, NVEP], "Directed Transition Power productions Original vs Modified vs Statnett vs NVE","[TWh]", ascending, years, showNumbers)
NVEyears=['2015', '2020', '2025', '2030', '2035', '2040']
#plotDfs([ODTC, DTC, NVEC], "Directed Transition Power Capacities Original vs Modified vs NVE","[GW]", ascending, NVEyears, showNumbers)

#plotDfs([ODT_PB, OTF_PB, OSC_PB, OGD_PB], "Original Power balance Directed Transition vs Techno Friendly vs Societal Commitment vs Gradual Development", "TWh", ascending, years, showNumbers)
#plotDfs([DT_PB, TF_PB, SC_PB, GD_PB], "Modified Power balance Directed Transition vs Techno Friendly vs Societal Commitment vs Gradual Development", "TWh", ascending, years, showNumbers)

DT_Use= DT_PB.loc[DT_PB['Technology'].isin(['Use'])]
ODT_Use= ODT_PB.loc[DT_PB['Technology'].isin(['Use'])]
NVEuse=NVEuse.loc[NVEuse['Technology'].isin(['Use'])]
StatnettUse=StatnettUse.loc[StatnettUse['Technology'].isin(['Use'])]
#plotDfs([ODT_Use, DT_Use, NVEuse,StatnettUse], "Power consumption", "TWh", ascending, years, showNumbers)

h2years=['2030', '2035', '2040', '2045', '2050']
#plotDfs([ODT_HB,OTF_HB,OSC_HB,OGD_HB], "Original Hydrogen Balance Directed Transition vs Techno Friendly vs Societal Commitment vs Gradual Development", "[PJ]", ascending, h2years, showNumbers)
#plotDfs([DT_HB,TF_HB,SC_HB,GD_HB], "Modified Hydrogen Balance Directed Transition vs Techno Friendly vs Societal Commitment vs Gradual Development", "[PJ]", ascending, h2years, showNumbers)
"""plotDfs([ODT_HB,DT_HB], "DirectedTransition Hydrogen Balance Original vs Modified", "[PJ]", ascending, h2years, showNumbers,1.5)

for changed,org in zip(grouped, groupedorg):
    org=org.append(org.sum(numeric_only=True), ignore_index=True)
    org.at[len(org)-1, "Technology"]="Sum"
    changed=changed.append(changed.sum(numeric_only=True), ignore_index=True)
    changed.at[len(changed)-1, "Technology"]="Sum"
    plotDfs([org, changed], "DirectedTransition Use of Energy Carriers in " + org.iloc[0,0]+" Original vs Modified", "TWh", ascending, years, showNumbers)

"""