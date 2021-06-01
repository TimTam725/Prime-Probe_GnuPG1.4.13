#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
# import seaborn as sns #python heat map
import numpy as np
# import csv

# mylist = []
# THR = 140
THR = 200
L = 10
C = 300
OFF = 0

# f = open("../data/scan-gpg13_set52_4000.csv", "r")
# tmp = np.loadtxt("../data/scan-gpg13_set52_4000.csv", delimiter = ",")
F = open("../name.txt", "r")
FNAME = F.read()
# tmp = np.load("../data_np/" + FNAME + "/" + FNAME + ".npy")
tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_cut10_split_middle.npy")
# L3-capture
# id = [316, 317, 318, 319]
tm = np.zeros((L, C))
for i in range(L):
    for j in range(OFF, OFF + C):
        if tmp[i][j] > THR:
            tm[i][j - OFF] = tmp[i][j]
        else:
            tm[i][j - OFF] = tmp[i][j]


# print(t[0])
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
plt.plot(tm[0])


# sns.heatmap(tm[50:80, 3800:4200], cmap = "Blues")
# sns.heatmap(tm, cmap = "Blues")

# major_xticks = np.arange(0, 8193, 7117)
# minor_xticks = np.arange(0, 8193, 100)
# # ax.set_xticks(major_xticks)
# ax.set_xticklabels(major_xticks)
# ax.set_xticks(minor_xticks, minor=True)
# plt.grid(which = 'minor', alpha = 0.2)
# plt.grid(which = 'major')
ax.set_xlabel("Slot number")
ax.set_ylabel("Set number")

plt.show()
# plt.savefig('f1.jpg')
