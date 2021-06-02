# %%
import random
from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# plt.matplotlib.use('Qt5Agg') #Show plot in separate window

def makeStr(val):
    if val == 0:
        string = ""
    else:
        string = str(val)
        if len(string) > 3:
            string = string[0:3]
        if string[-1] == '.':
            string = string[0:-1]
    return string


# %%
colorMap = {"p": "#7e1e9c",
            "g": "#15b01a",
            "b": "#0343df",
            "r": "#e50000",
            "t": "#029386",
            "y": "#ffff14",
            "c": "#00ffff",
            "o": "#f97306",
            "bur": "#610023",
            "hp": "#ff028d",
            "bb": "#0165fc",
            "wb": "#a2cffe",
            "yg": "#c0fb2d",
            "gold": "#dbb40c",
            "sfg": "#7af9ab",
            "bg": "#137e6d",
            "fg": "#06470c",
            "ochre": "#bf9005",
            "kg": "#02ab2e",
            "lo": "#fdaa48",
            "peach": "#ffb07c",
            "db": "#00035b",
            "dg": "#033500",
            "ab": "#070d0d",
            "lg": "#0cff0c"
            }
techColor = {
    "Hydro": "b",
    "Thermal": "r",
    "Other": "r",
    "Wind Onshore": "g",
    "Wind": "g",
    "PV": "o",
    "PV Utility": "o",
    "PV Rooftop": "y",
    "Wind Offshore Transitional": "c",
    "Wind Offshore Deep": "p",
    "Wind Offshore": "p",
    "Export": "o",
    "Import": "c",
    "Production": "b",
    "Use": "r",

    "P_Biomass": "bur",
    "HLI_Biomass_CHP_CCS": "r",
    "P_Gas": "hp",
    "RES_Hydro_Large": "bb",
    "RES_Hydro_Small": "wb",
    "RES_PV_Rooftop_Commercial": "y",
    "RES_PV_Rooftop_Residential": "ochre",
    "RES_PV_Utility_Avg": "yg",
    "RES_PV_Utility_Inf": "lo",
    "RES_PV_Utility_Opt": "gold",
    "RES_Wind_Offshore_Transitional": "sfg",
    "RES_Wind_Offshore_Deep": "bg",
    "RES_Wind_Onshore_Avg": "kg",
    "RES_Wind_Onshore_Opt": "fg",

    "Biomass": "bur",
    "Biofuel": "bg",
    "Gas_Bio": "gold",
    "Gas_Natural": "r",
    "Gas_Synth": "peach",
    "H2": "b",
    "Oil": "ab",
    "Power": "g",
    "Hardcoal": "o",

    "Power Balance": "lg"
}


# %%
def plotDfs(dfs, title, unit, ascending=True, years=None, showNumbers=False,H2=0):
    if years is None:
        years = list(map(str, range(2015, 2051, 5)))

    x = np.arange(len(years))
    width = 1.55 - 0.15 * len(dfs)
    opacity = 1
    fig, ax = plt.subplots()
    plt.grid(axis="y", zorder=0)
    if H2:
        plt.ylim([-120, 120])

    nonZeroTechnologies = set()
    for i in range(len(dfs)):
        prev = defaultdict(int)
        df = dfs[i]
        for tech in df['Technology']:
            try:
                colorMap[techColor[tech]]
            except:
                techColor[tech] = tech
                colorMap[tech] = tuple(random.choice(range(32, 256, 32)) / 255 for i in range(4))

        # df = df.sort_values(by='2015', ascending=ascending)
        base = 0
        negative_base = 0
        for trueIdx, (idx, row) in enumerate(df.iterrows()):
            use_base = True
            tech = row['Technology']
            # if sum(np.array(row[2::])) == 0:
            # continue
            # print(row[years])
            if row[years].sum():
                nonZeroTechnologies.add(tech)

            if row[years][-1] < 0:
                use_base = False
            # try:
            color = colorMap[techColor[tech]]
            # except:
            # techColor[tech] = tech
            # colorMap[tech] = tuple(random.choice(range(32, 256, 32)) / 255 for i in range(4))
            # color = colorMap[tech]

            barsXPossitions = np.array(list(map(int, years))) + (i - (len(dfs) - 1) / 2) * width * 1.1
            if tech not in ["Sum", "Sum2"]:
                ax.bar(barsXPossitions, row[years], width,
                       label=tech,
                       bottom=base if use_base else negative_base, alpha=opacity, zorder=3, color=color)
                ax.set_xlabel("Year", fontsize=14)
                ax.set_ylabel(unit, fontsize=14)

            if use_base:
                base += row[years]
            else:
                negative_base += row[years]

            if showNumbers > 0:
                for idx, xPos in enumerate(barsXPossitions):
                    year = years[idx]
                    val = row[year]

                    if tech in ["Sum", "Sum2"]:
                        bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
                        ymin, ymax = ax.get_ylim()
                        # yPos=prev[year]+ymax/50
                        yPos = val
                        yPos += max(ymax / 45,1)+H2 if yPos >= 0 else -max(ymax / 45,1)-H2

                        color = "black"
                        string = "%d" % round(val)# if round(val) else ""
                        ax.text(xPos, yPos, string, ha="center", va="center", color=color,
                                fontsize=8+H2 if abs(yPos) > 100 else 9.5,
                                fontweight="bold")
                        prev[year] += row[year]
                    elif showNumbers > 1:
                        color = "pink"
                        #yPos = val
                        #ymin, ymax = ax.get_ylim()
                        #yPos += max(ymax / 45,1) if yPos >= 0 else -max(ymax / 45,1)
                        yPos = prev[year] + val / 2
                        string = "%d" % round(val) if round(val) else ""
                        #print("string =",string,"yPos =", round(yPos), end=" ")

                        ax.text(xPos, yPos, string, ha="center", va="center", color=color,
                                fontsize=8.5 if yPos > 100 else 9.5, fontweight="bold")

                    prev[year] += row[year]
                #print()

    patches = [mpatches.Patch(color=colorMap[techColor[tech]], label=tech) for tech in df['Technology'] if
               tech not in ["Sum", "Sum2"] and tech in nonZeroTechnologies]
    ax.legend(handles=patches, loc="best")
    plt.title(title)
    # manager = plt.get_current_fig_manager()
    # manager.window.showMaximized()

    figure = plt.gcf()  # get current figure
    figure.set_size_inches(14, 8)  # set figure's size manually to your full screen (32x18)
    plt.savefig("plots\\" + title.replace(" ", "_"))  # , bbox_inches='tight')  # bbox_inches removes extra white spaces
    plt.show()
