#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns#python heat map
import numpy as np
import csv

# mylist = []
# THR = 140
THR = 200
L = 36
C = 300
OFF = 5000
# THR1 = 100
# THR2 = 150
# THR3 = 200
# THR4 = 5

f = open("../data/scan-gpg13_set52_4000.csv", "r")
tmp = np.loadtxt("../data/scan-gpg13_set52_4000.csv", delimiter = ",")

F = open("../name.txt", "r")
FNAME = F.read()
# tmp = np.load("../data_np/" + FNAME + "/" + FNAME + ".npy")
data = np.load("../data_np/" + FNAME + "/" + FNAME + "_cut10_split_middle.npy")
# with open("../data/scan-gpg13_set52_4000.csv", 'r') as f:
#     data = list(csv.reader(f, lineterminator='\n'))
# tmp = np.load("../data_np/scan-gpg13_set52_4000/scan-gpg13_set52_4000_cut10.npy")

# L3-capture
# id = [316, 317, 318, 319]
tm = np.zeros((L, C))
for i in range(3, 3 + L):
    if i == 15 + 3:
        for j in range(0, C):
            if data[0][j] > THR:
                tm[i - 3][j] = 1
            else:
                tm[i - 3][j] = 0
    else:
        for j in range(OFF, OFF + C):
            if tmp[i][j] > THR:
                tm[i - 3][j - OFF] = 1
            else:
                tm[i - 3][j - OFF] = 0



fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

df_mask = (tm == 2)
df_mask2 = (tm == 1)
# print(df_mask)
# sns.heatmap(tm[50:80, 3800:4200], cmap = "Blues")
sns.heatmap(tm, cmap = "Greys", cbar = False, xticklabels = 50, yticklabels = 10, mask = df_mask, vmax = 3, vmin = 0)
# sns.heatmap(tm, cmap = "Blues", cbar = False, xticklabels = 50, yticklabels = 10, mask = df_mask2, vmax = 3, vmin = 0)
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.invert_yaxis()
# plt.imshow(tm,interpolation='nearest',cmap='jet',aspect= "auto")
# plt.xticks(np.arange(0, 300, 10))
# major_xticks = np.arange(0, 8193, 7117)
# minor_xticks = np.arange(0, 8193, 100)
# # ax.set_xticks(major_xticks)
# ax.set_xticklabels(major_xticks)
# ax.set_xticks(minor_xticks, minor=True)
# plt.grid(which = 'minor', alpha = 0.2)
# plt.grid(which = 'major')
ax.set_xlabel("Time slot number", labelpad = 10, fontsize = 15)
ax.set_ylabel("Cache set number", labelpad = 10, fontsize = 15)

plt.show()
# plt.savefig('f1.jpg')
