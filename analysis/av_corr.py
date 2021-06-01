#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns #python heat map
import numpy as np
import time
from tqdm import tqdm
import os
import csv

# mylist = []
# THR = 0
LEN = 2000
SAMPLES = 100
tmp = np.load("../data_np/scan-gpg18_set34_100_under2000.npy")
# tmp = np.load("../data_np/scan-gpg18_set34_4.npy")

print(len(tmp))
print(len(tmp[0]))
id = [0, 1, 2, 3]
# id = [SAMPLES * 47, SAMPLES * 47 + 1, SAMPLES * 47 + 2, SAMPLES * 47 + 3]

avlist0 = []
for j in range(len(tmp[0]) - LEN):
    ave = np.average(tmp[id[0]][j:j + LEN])
    avlist0.append(ave)
avlist1 = []
for j in range(len(tmp[0]) - LEN):
    ave = np.average(tmp[id[1]][j:j + LEN])
    avlist1.append(ave)
avlist2 = []
for j in range(len(tmp[0]) - LEN):
    ave = np.average(tmp[id[2]][j:j + LEN])
    avlist2.append(ave)
avlist3 = []
for j in range(len(tmp[0]) - LEN):
    ave = np.average(tmp[id[3]][j:j + LEN])
    avlist3.append(ave)

sig0 = avlist0 - sum(avlist0)/len(avlist0)
sig1 = avlist1 - sum(avlist1)/len(avlist1)
sig2 = avlist2 - sum(avlist2)/len(avlist2)
sig3 = avlist3 - sum(avlist3)/len(avlist3)

corr01 = np.correlate(sig0, sig1, "full")
corr02 = np.correlate(sig0, sig2, "full")
corr03 = np.correlate(sig0, sig3, "full")
MID = int(len(corr01) / 2)
RAN = 5000
# estimated_delay = corr.argmax() - (len(sig2) - 1)
# print("estimated delay is " + str(estimated_delay))
plt.figure(figsize=(12, 8)) #...1
# correlation = np.corrcoef(sig1, sig2)
# print(correlation[0, 1])
plt.subplot(4, 2, 1) #...2
plt.title("sig 0")
plt.plot(sig0)
# plt.plot(np.abs(F1), color="b")
plt.subplot(4, 2, 2)
plt.title("sig 1")
plt.plot(sig1)
# plt.plot(np.arange(len(sig2)) + estimated_delay, sig2, color="r")
# plt.plot(np.abs(F2), color="r")
# estimated_delay = corr01[MID - RAN : MID + RAN].argmax()
estimated_delay = corr01.argmax() - (len(sig0) - 1)
print(estimated_delay)
plt.subplot(4, 2, 3)
plt.title("sig 0 and 1")
plt.plot(np.arange(len(sig0)), sig0)
plt.plot(np.arange(len(sig1)) + estimated_delay, sig1 )
plt.xlim([0, len(sig0)])

estimated_delay = corr02.argmax() - (len(sig0) - 1)
print(estimated_delay)
plt.subplot(4, 2, 4)
plt.title("sig 0 and 2")
plt.plot(np.arange(len(sig0)), sig0)
plt.plot(np.arange(len(sig2)) + estimated_delay, sig2 )
plt.xlim([0, len(sig0)])

estimated_delay = corr03.argmax() - (len(sig0) - 1)
print(estimated_delay)
plt.subplot(4, 2, 5)
plt.title("sig 0 and 3")
plt.plot(np.arange(len(sig0)), sig0)
plt.plot(np.arange(len(sig2)) + estimated_delay, sig3 )
plt.xlim([0, len(sig0)])

estimated_delay = corr01.argmax() - (len(sig0) - 1)
print(estimated_delay)
plt.subplot(4, 2, 6)
plt.title("sig 0 and 1")
plt.plot(np.arange(len(tmp[0])), tmp[0])
plt.plot(np.arange(len(tmp[1])) + estimated_delay, tmp[1] )
plt.xlim([0, len(tmp[1])])

estimated_delay = corr02.argmax() - (len(sig0) - 1)
print(estimated_delay)
plt.subplot(4, 2, 7)
plt.title("sig 0 and 2")
plt.plot(np.arange(len(tmp[0])), tmp[0])
plt.plot(np.arange(len(tmp[2])) + estimated_delay, tmp[2] )
plt.xlim([0, len(tmp[2])])

estimated_delay = corr03.argmax() - (len(sig0) - 1)
print(estimated_delay)
plt.subplot(4, 2, 8)
plt.title("sig 0 and 1")
plt.plot(np.arange(len(tmp[0])), tmp[0])
plt.plot(np.arange(len(tmp[3])) + estimated_delay, tmp[3] )
plt.xlim([0, len(tmp[3])])
plt.show()
