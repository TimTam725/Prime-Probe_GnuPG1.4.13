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

f = open("../../data/scan-gpg13_set52_4000.csv", "r")
tmp = np.loadtxt("../../data/scan-gpg13_set52_4000.csv", delimiter = ",")

F = open("../../name.txt", "r")
FNAME = F.read()
# tmp = np.load("../data_np/" + FNAME + "/" + FNAME + ".npy")
data = np.load("../../data_np/" + FNAME + "/" + FNAME + "_cut10_split_middle.npy")
# with open("../data/scan-gpg13_set52_4000.csv", 'r') as f:
#     data = list(csv.reader(f, lineterminator='\n'))
# tmp = np.load("../data_np/scan-gpg13_set52_4000/scan-gpg13_set52_4000_cut10.npy")

# L3-capture
# id = [316, 317, 318, 319]
tm = np.zeros((L, C))
for i in range(3, 3 + L):
    if i == 15 + 3 + 5:
        for j in range(0, C):
            if data[0][j] > THR:
                tm[i - 3][j] = 2
            else:
                tm[i - 3][j] = 0
    else:
        for j in range(OFF, OFF + C):
            if tmp[i][j] > THR:
                tm[i - 3][j - OFF] = 1
            else:
                tm[i - 3][j - OFF] = 0



fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(111)

df_mask = (tm == 2)
df_mask2 = np.zeros((L, C))
# df_mask2 = [[False for i in range(L)] for j in range(C)]
for i in range(len(tm)):
    for j in range(len(tm[0])):
        if tm[i][j] != 2:
            df_mask2[i][j] = True

b = sns.heatmap(tm, cmap = "Greys", cbar = False, xticklabels = 50, yticklabels = 10, mask = df_mask, vmax = 3, vmin = 0)
sns.heatmap(tm, cmap = "Blues", cbar = False, xticklabels = 50, yticklabels = 10, mask = df_mask2, vmax = 3, vmin = 0)
# sns.heatmap(tm, cmap = "Greys", cbar = False, yticklabels = 10, mask = df_mask, vmax = 3, vmin = 0)
# ax.set_xticklabels(np.arange(0, 300, 10), fontsize = 15)
b.set_xticklabels(b.get_xmajorticklabels(), fontsize = 15, color = "black")
b.set_yticklabels(b.get_ymajorticklabels(), fontsize = 15, color = "black")
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.invert_yaxis()

ax.set_xlabel("Time slot number", labelpad = 10, fontsize = 30, color = "black")
ax.set_ylabel("Cache set number", labelpad = 10, fontsize = 30, color = "black")

plt.show()
# plt.savefig('f1.jpg')
