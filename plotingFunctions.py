# %%
import random
import numpy as np
import matplotlib.pyplot as plt

#plt.matplotlib.use('Qt5Agg') #Show plot in separate window

# %%
colorMap = {"p": "#7e1e9c",
         "g": "#15b01a",
         "b": "#0343df",
         "r": "#e50000",
         "t": "#029386",
         "y": "#ffff14",
         "c": "#00ffff",
         "o": "#f97306"}

techColor = {
    "Hydro": "b",
    "Thermal": "r",
    "Wind Onshore": "g",
    "PV": "o",
    "Wind Offshore Transitional": "c",
    "Wind Offshore Deep": "p",
}


# %%

def plotDfs(dfs, title, ascending=True):
    years = list(map(str, range(2015, 2051, 5)))
    x = np.arange(len(years))
    # labels = ['TF DF
    width = 1.55-0.15*len(dfs)
    opacity = 1
    fig, ax = plt.subplots()
    color_str = "pocgrb" if ascending else "brgcop"
    plt.grid(axis="y", zorder=0)
    for i in range(len(dfs)):
        df=dfs[i]
        df = df[df.Technology != "Sum"]
        df = df.sort_values(by='2015', ascending=ascending)
        base = 0
        for trueIdx, (idx, row) in enumerate(df.iterrows()):
            color=""
            tech=row['Technology']
            try:
                color=colorMap[techColor[tech]]
            except:
                color=tuple(random.choice(range(32, 256, 32)) / 255 for _ in range(4))

            ax.bar(np.array(list(map(int,years)))+(i-(len(dfs)-1)/2)*width*1.1, row[years], width, label=tech,
                   bottom=base, alpha=opacity, zorder=3, color=color)
            # print(row['Technology'])
            base += row[years]

        ax.legend(df['Technology'])

    plt.title(title)
    #manager = plt.get_current_fig_manager()
    #manager.window.showMaximized()

    figure = plt.gcf()  # get current figure
    figure.set_size_inches(14, 8)  # set figure's size manually to your full screen (32x18)
    plt.savefig("plots\\"+title)#, bbox_inches='tight')  # bbox_inches removes extra white spaces
    plt.show()
