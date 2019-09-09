import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import style
import matplotlib.pyplot as plt

def plotHistograms(df, nameOfParam):

    plt.style.use('classic')
    minValue = min(df[nameOfParam])
    maxValue = max(df[nameOfParam])
    nameDict = {'Temperature': 'Temperatura ['+ r'$^o$' + 'C]',\
    'ApparentTemperature':'Temperatura odczuwalna ['+r'$^o$' + 'C]',\
    'Humidity':'Wilgotność [-]','Pressure': 'Ciśnienie [hPa]'}


    fig = plt.subplots(4, 3,  dpi = 80, figsize = (10,10), facecolor = 'white')
    plt.suptitle(nameDict[nameOfParam], fontsize = 28)

    axes = []
    ymaxes = []     # inicjalizacja listy maksymalnych wartości na osi y

    for ax in range(11):
        axes.append(plt.subplot(4, 3, ax+1))
        axes[ax].set_title( str(2006 + ax))
        plt.sca(axes[ax])
        sns.distplot(df.loc[str(2006 + ax)].loc[:, nameOfParam] , bins = 15, \
                     kde = False)
        axes[ax].set_xlim(minValue,maxValue)
        ymaxes.append(axes[ax].get_ylim()[1])
        axes[ax].set_xlabel(nameDict[nameOfParam])

    for i,ax in enumerate(axes):
        ax.set_ylim(0,max(ymaxes))
        srednia = df.loc[str(2006+i)].loc[:,nameOfParam].mean()
        std = df.loc[str(2006+i)].loc[:,nameOfParam].std()
        ax.plot([srednia,srednia], [0, max(ymaxes)], '--', color = 'red', \
                 mew=20, ms=30)
        ax.plot([srednia+std,srednia+std], [0, max(ymaxes)], '--', \
                 color = 'green', mew=10, ms=20)
        ax.plot([srednia-std,srednia-std], [0, max(ymaxes)], '--', \
                 color = 'green', mew=10, ms=20)

    plt.subplots_adjust(left = 0.05, bottom = 0.05, right = 0.99, top = 0.9, \
                        wspace = 0.45, hspace = 0.45)

    return fig
