import allantools
import matplotlib.pyplot as plt
import numpy as np


# Receives the TE in seconds and plots the Allan TDEV
def plotTDEV(TE):
    frequency = np.diff(TE[0::64])
    a = allantools.Dataset(data=frequency, rate=1.0/64, data_type='freq')
    a.compute("tdev")

    plotter = allantools.Plot()
    plotter.plot(a, errorbars=True, grid=True)

    plotter.ax.set_xlabel("$\\tau$ [s]")
    plotter.ax.set_ylabel("TDEV [s]")
    plt.title("Varianza de Allan para NTPv4")
    plotter.show()
