# %%
import random
import numpy as np
import matplotlib.pyplot as plt

# plt.matplotlib.use('Qt5Agg') #Show plot in separate window

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
            "gold":"#dbb40c",
            "sfg": "#7af9ab",
            "bg": "#137e6d",
            "fg": "#06470c",
            "ochre": "#bf9005",
            "kg": "#02ab2e",
            "lo": "#fdaa48"
}
techColor = {
    "Hydro": "b",
    "Thermal": "r",
    "Other": "r",
    "Wind Onshore": "g",
    "PV": "o",
    "Wind Offshore Transitional": "c",
    "Wind Offshore Deep": "p",
    "Export": "o",
    "Import": "c",
    "Production": "b",
    "Use": "r",
    
    "P_Biomass": "bur",
    "HLI_Biomass_CHP_CCS" : "r",
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
    "RES_Wind_Onshore_Opt": "fg"
}

# %%

def plotDfs(dfs, title, ascending=True):
    years = list(map(str, range(2015, 2051, 5)))
    x = np.arange(len(years))
    width = 1.55 - 0.15 * len(dfs)
    opacity = 1
    fig, ax = plt.subplots()
    plt.grid(axis="y", zorder=0)

    for i in range(len(dfs)):
        df = dfs[i]
        df = df[df.Technology != "Sum"]
        #df = df.sort_values(by='2015', ascending=ascending)
        base = 0
        negative_base = 0
        for trueIdx, (idx, row) in enumerate(df.iterrows()):
            use_base = True
            tech = row['Technology']
            if row[years][-1]<0:
                use_base = False
            try:
                color = colorMap[techColor[tech]]
            except:
                techColor[tech]=tech
                colorMap[tech]=tuple(random.choice(range(32, 256, 32)) / 255 for i in range(4))
                color = colorMap[tech]
            ax.bar(np.array(list(map(int, years))) + (i - (len(dfs) - 1) / 2) * width * 1.1, row[years], width,
                   label=tech,
                   bottom=base if use_base else negative_base, alpha=opacity, zorder=3, color=color)
            if use_base:
                base += row[years]
            else:
                negative_base += row[years]


        ax.legend(df['Technology'])

    plt.title(title)
    # manager = plt.get_current_fig_manager()
    # manager.window.showMaximized()

    figure = plt.gcf()  # get current figure
    figure.set_size_inches(14, 8)  # set figure's size manually to your full screen (32x18)
    plt.savefig("plots\\" + title)  # , bbox_inches='tight')  # bbox_inches removes extra white spaces
    plt.show()


