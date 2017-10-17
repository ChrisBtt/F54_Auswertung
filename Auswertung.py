import matplotlib.pyplot as plt
import numpy as np


def to_hour(seconds):
    '''Rechnet die gemessene Zeitdauer von Sekunden in Stunden um'''
    return seconds / 3600


def messungen(evasion_start, evasion_stop, begasung_start, begasung_stop, sauer_start, sauer_stop, alkali_start, alkali_stop, height, skim_start, skim_stop, lampe_start, lampe_stop, indi_start, indi_stop, dunkel_start, dunkel_stop):

    evasion1 = plt.plot(np.linspace(evasion_start/3600, skim_start/3600, 1e+3), np.full(1000, height), label='Evasion', color='blue', linewidth=2)
    skim = plt.plot(np.linspace(skim_start/3600, skim_stop/3600, 1e+3), np.full(1000, height), label='Skimmung', color='magenta', linewidth=2)
    evasion2 = plt.plot(np.linspace(skim_stop/3600, evasion_stop/3600, 1e+3), np.full(1000, height), linewidth=2, color='blue')
    lampe = plt.plot(np.linspace(lampe_start/3600, lampe_stop/3600, 1e+3), np.full(1000, height), label='Lampe', color='orange', linewidth=2)
    indikator = plt.plot(np.linspace(indi_start/3600, indi_stop/3600, 1e+3), np.full(1000, height), label='Indikator', color='green', linewidth=2)
    begasung = plt.plot(np.linspace(begasung_start/3600, begasung_stop/3600, 1e+3), np.full(1000, height), label='Begasung', color='violet', linewidth=2)
    sauer = plt.plot(np.linspace(sauer_start/3600, sauer_stop/3600, 1e+3), np.full(1000, height), label='Säurereferenz', color='purple', linewidth=2)
    alkali = plt.plot(np.linspace(alkali_start/3600, alkali_stop/3600, 1e+3), np.full(1000, height), label='Laugenreferenz', color='chocolate', linewidth=2)
    dunkel = plt.plot(np.linspace(dunkel_start/3600, dunkel_stop/3600, 1e+3), np.full(1000, height), label='Dunkelmessung', color='black', linewidth=2)

    return evasion1, evasion2, skim, begasung, sauer, alkali, lampe, indikator


time_sec2, conduct, tempWater = np.loadtxt(
    'VE-Wasser/FP_10_08_2017_10_02_57_Conductivity_Twater-data.asc',
    skiprows=1, usecols=(1, 2, 3), unpack=True)

time2 = to_hour(time_sec2)

# plt.plot(time2, tempWater, marker='.', color='red', label='Temperatur', linewidth=1)
# plt.xlabel('Zeit $[h]$')
# plt.ylabel('Temperatur $[°C]$')
# plt.title('Wassertemperatur')
# messungen(2256, 5844, 1173, 2040, 6596, 6774, 8401, 8602, 22.0, 2515, 2555, 0, 469, 730, 1035, 8634, 8815)
# plt.legend(loc='best')
# plt.savefig('VE-Wasser/Wassertemperatur.pdf', format='PDF')
# plt.show()

# plt.plot(time2, conduct, '-r', label='Leitfähigkeit', linewidth=1)
# plt.xlabel('Zeit $[h]$')
# plt.ylabel('Leitfähigkeit $[\mu S/cm]$')
# plt.title('Leitfähigkeit')
# messungen(2256, 5844, 1173, 2040, 6596, 6774, 8401, 8602, 22.0, 2515, 2555, 0, 469, 730, 1035, 8634, 8815)
# plt.legend(loc='best')
# plt.savefig('VE-Wasser/Leitfähigkeit.pdf', format='PDF')
# plt.show()

time_sec1, co2_air, tempAir, wind, waterHeight, p0xyAbs = np.loadtxt(
    'VE-Wasser/FP_10_08_2017_10_02_13-data.asc', skiprows=2,
    usecols=range(1, 7), unpack=True)

time1 = to_hour(time_sec1)

# plt.plot(time1, co2_air, marker='.', color='red', label='Partialdruck', linewidth=1)
# plt.xlabel('Zeit $[h]$')
# plt.ylabel('Partialdruck $[ppm]$')
# plt.title('$CO_2$ Partialdruck in Luft')
# messungen(2256, 5844, 1173, 2040, 6596, 6774, 8401, 8602, 500.0, 2515, 2555, 0, 469, 730, 1035, 8634, 8815)
# plt.legend(loc='best')
# plt.savefig('VE-Wasser/Partialdruck.pdf', format='PDF')
# plt.show()

# plt.plot(time1, tempAir, '-r', linewidth=1, label='Temperatur')
# plt.xlabel('Zeit $[h]$')
# plt.ylabel('Temperatur $[°C]$')
# plt.title('Lufttemperatur')
# messungen(2256, 5844, 1173, 2040, 6596, 6774, 8401, 8602, 22.5, 2515, 2555, 0, 469, 730, 1035, 8634, 8815)
# plt.legend(loc='best')
# plt.savefig('VE-Wasser/Lufttemperatur.pdf', format='PDF')
# plt.show()

# plt.plot(time1, wind, '-r', linewidth=1, label='Geschwindigkeit')
# plt.xlabel('Zeit $[h]$')
# plt.ylabel('Geschwindigkeit $[m/s]$')
# plt.title('Windgeschwindigkeit')
# messungen(2256, 5844, 1173, 2040, 6596, 6774, 8401, 8602, 2.5, 2515, 2555, 0, 469, 730, 1035, 8634, 8815)
# plt.legend(loc='best')
# plt.savefig('VE-Wasser/Windgeschwindigkeit.pdf', format='PDF')
# plt.show()

# plt.plot(time1, waterHeight, '-r', linewidth=1, label='Höhe')
# plt.xlabel('Zeit $[h]$')
# plt.ylabel('Höhe $[mm]$')
# plt.title('Wasserhöhe')
# messungen(2256, 5844, 1173, 2040, 6596, 6774, 8401, 8602, 78.0, 2515, 2555, 0, 469, 730, 1035, 8634, 8815)
# plt.legend(loc='best')
# plt.savefig('VE-Wasser/Wasserhoehe.pdf', format='PDF')
# plt.show()

plt.plot(time1, p0xyAbs, '-r', linewidth=1, label='Druck')
plt.xlabel('Zeit $[h]$')
plt.ylabel('Druck $[bar]$')
plt.title('Luftdruck im Kanal')
messungen(2256, 5844, 1173, 2040, 6596, 6774, 8401, 8602, 1.6, 2515, 2555, 0, 469, 730, 1035, 8634, 8815)
plt.legend(loc='best')
plt.savefig('VE-Wasser/Luftdruck.pdf', format='PDF')
plt.show()
