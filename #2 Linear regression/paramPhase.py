import numpy as np
import matplotlib.pyplot as plt


def paramPhase(dfValuesPhases, nazwa, nr):
    """
    Visualizes specific parameter as a function of phase angle
    """

    plt.style.use("classic")
    pory = ["Zima", "Wiosna", "Lato", "Jesień"]
    name = dfValuesPhases.columns[0]
    nameDict = {"Temperature": "temperatura [" + r"$^o$" + "C]",
                "Pressure": "ciśnienie [hPa]", "Humidity": "wilgotność [-]"}
    limDict = {"Temperature": [-5, 30], "Pressure": [1012, 1024],
               "Humidity": [0.4, 1]}

    meanValues = np.zeros([4, 24])

    for i, pora in enumerate(pory):
        dfseason = dfValuesPhases[(dfValuesPhases["YearPhase"]
                                   <= i*np.pi/2+0.1) &
                                  (dfValuesPhases["YearPhase"]
                                   >= i*np.pi/2-0.1)]

        for j, mT in enumerate(meanValues[i, :]):

            df_mV = dfseason[(dfseason["DayPhase"] <= j/24*2*np.pi+0.01) &
                             (dfseason["DayPhase"] >= j/24*2*np.pi-0.01)]
            meanValues[i, j] = df_mV[name].mean()

    fig = plt.figure(figsize=(16, 12))
    axes = []
    ymaxes = []
    ymins = []

    for sub in range(len(pory)):
        axes.append(fig.add_subplot(2, 2, sub+1) )
        axes[sub].set_title(pory[sub], {"fontsize": 28})
        axes[sub].plot(meanValues[sub,:], linewidth=2)
        axes[sub].set_xlabel("Godzina", {"fontsize": 24})
        axes[sub].set_ylabel("Śr. " + nameDict[name], {"fontsize": 24})
        axes[sub].tick_params(axis="both", which="both", labelsize=24)
        axes[sub].yaxis.offsetText.set_fontsize(24)
        axes[sub].minorticks_on()
        axes[sub].set_xlim(0, 24)
        ymaxes.append(max(meanValues[sub, :]))
        ymins.append(min(meanValues[sub, :]))

    for ax in axes:
        ax.set_ylim(limDict[name])

    plt.suptitle(nazwa + " - zmienność w ciągu dnia", fontsize=32)

    plt.subplots_adjust(left=0.08, bottom=0.1, right=0.99, top=0.9,
                        wspace=0.3, hspace=0.4)
    plt.savefig(Figure=fig, fname="plots/2AD"+str(nr)+".png")
