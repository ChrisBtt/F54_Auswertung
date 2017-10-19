import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def to_hour(seconds):
    '''Rechnet die gemessene Zeitdauer von Sekunden in Stunden um'''
    return seconds / 3600


time_sec2, conduct = np.loadtxt('/Users/logosalmac/Desktop/F54_Auswertung/VE-Wasser/FP_10_08_2017_10_02_57_Conductivity_Twater-data.asc',skiprows=1, usecols=(1, 2), unpack=True)

time2 = to_hour(time_sec2)

time_sec1, co2Air = np.loadtxt(
    '/Users/logosalmac/Desktop/F54_Auswertung/VE-Wasser/FP_10_08_2017_10_02_13-data.asc',
    skiprows=1, usecols=(1, 2), unpack=True)

time1 = to_hour(time_sec1)

def linear(x,a,b):
    return a * x + b

popt, pcov = curve_fit(linear, time2[275:718], conduct[275:718] ** 2 / 37456 / 0.038 * 10 ** 6)

plt.plot(time2[275:718], conduct[275:718] ** 2 / 37456 / 0.038 * 10 ** 6, '-b', label='wasserseitige $CO_2$-Konzentration')
plt.plot(time2[275:718], co2Air[259:702], '-r', label='luftseitige $CO_2$-Konzentration')
plt.xlabel('Zeit $[h]$')
plt.ylabel('Partialdruck $[ppm]$')
plt.yscale('log')
plt.legend(loc='best')
plt.savefig('LeitfaehigkeitQuadrat.pdf', format='PDF')
plt.show()

print("Steigung: ", popt[0])

# fig, ax1 = plt.subplots()
# ax1.plot(time2[255:718], co2Air[239:702] / 0.038 / 24000000, 'b-')
# ax1.set_xlabel('Zeit $[h]$')
# # Make the y-axis label, ticks and tick labels match the line color.
# ax1.set_ylabel('Konzentration $[mol/l]$', color='b')
# ax1.tick_params('y', colors='b')

# ax2 = ax1.twinx()
# ax2.plot(time2[255:718], conduct[255:718] ** 2 / 37456 / 0.038, 'r.')
# ax2.set_ylabel('Konzentration $[mol/l]$', color='r')
# ax2.tick_params('y', colors='r')

# fig.tight_layout()
# plt.show()
