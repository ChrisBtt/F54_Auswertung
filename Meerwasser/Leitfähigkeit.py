import matplotlib.pyplot as plt
import numpy as np


def to_hour(seconds):
    '''Rechnet die gemessene Zeitdauer von Sekunden in Stunden um'''
    return seconds / 3600


time_sec2, hI1 = np.loadtxt(
                            'Wellenlängenbereich 252-760/FP_10_08_2017_12_53_23_HIoverI_Wavebin0252to0760.txt',
                            skiprows=1, usecols=(1, 2), unpack=True)
hI2 = np.loadtxt(
                 'Wellenlängenbereich 264-368/FP_10_08_2017_12_53_23_HIoverI_Wavebin0264to0368.txt',
                 skiprows=1, usecols=2, unpack=True)
hI3 = np.loadtxt(
                 'Wellenlängenbereich 496-764/FP_10_08_2017_12_53_23_HIoverI_Wavebin0496to0764.txt',
                 skiprows=1, usecols=2, unpack=True)
hI4 = np.loadtxt(
                 'Wellenlängenbereich 496-764/FP_10_08_2017_12_53_23_HIoverI_Wavebin0596to0796.txt',
                 skiprows=1, usecols=2, unpack=True)
hI5 = np.loadtxt(
                 'Wellenlängenbereich 548-644/FP_10_08_2017_12_53_23_HIoverI_Wavebin0548to0644.txt',
                 skiprows=1, usecols=2, unpack=True)

time2 = to_hour(time_sec2)

co2Air = np.loadtxt(
                    'FP_10_08_2017_12_53_23-data.asc',
                    skiprows=1, usecols=2, unpack=True) - 170

print("Python3 geht")

plt.plot(time2[184:597], hI1[184:597] / 0.038 / 4681 * 10 ** 6, color='blue', label='284 - 836')
plt.plot(time2[184:597], hI2[184:597] / 0.038 / 5697 * 10 ** 6, color='green', label='288 - 432')
plt.plot(time2[184:597], hI3[184:597] / 0.038 / 3984 * 10 ** 6, color='violet', label='524 - 880')
plt.plot(time2[184:597], hI4[184:597] / 0.038 / 4110 * 10 ** 6, color='orange', label='304 - 376')
plt.plot(time2[184:597], hI5[184:597] / 0.038 / 3643 * 10 ** 6, color='brown', label='596 - 796')
plt.plot(time2[184:597], co2Air[190:603], '-r', label='Luftkonzentration')
plt.xlabel('Zeit $[h]$')
plt.ylabel('Konzentration $[ppm]$')
plt.yscale('log')
plt.legend(loc='best')
plt.savefig('Indikator.pdf', format='PDF')
plt.show()

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
