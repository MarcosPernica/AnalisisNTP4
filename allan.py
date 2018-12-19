import allantools
import matplotlib.pyplot as plt

def plotTDEV(TE):
	a = allantools.Dataset(data=TE)
	a.compute("tdev")

	plotter = allantools.Plot()
	plotter.plot(a, errorbars=True, grid=True)

	plotter.ax.set_xlabel("Tau [s]")
	plotter.ax.set_ylabel("TDEV [s]")
	plt.title("Varianza de Allan para NTPv4")
	plotter.show()