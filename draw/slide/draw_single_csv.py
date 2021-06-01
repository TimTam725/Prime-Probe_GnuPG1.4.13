#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
# import seaborn as sns #python heat map
import numpy as np
import seaborn as sns; sns.set()
# import csv

# mylist = []
# THR = 140
THR = 200
L = 10
C = 300
OFF = 0

# F = open("../../name.txt", "r")
# FNAME = F.read()
f = open("../../data/scan-gpg13_set52_4000.csv", "r")
tmp = np.loadtxt("../../data/scan-gpg13_set52_4000.csv", delimiter = ",")
# tmp = np.load("../data_np/" + FNAME + "/" + FNAME + ".npy")
# tmp = np.load("../../data_np/" + FNAME + "/" + FNAME + "_cut10_split_middle.npy")

# fig = plt.figure()
fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(111)
plt.plot(tmp[2])
plt.ylim(0, 1000)
plt.yticks(np.arange(0, 1000, 100), fontsize = 15, color = "black")
plt.xticks(np.arange(0, len(tmp[0]), 5000), fontsize = 15, color = "black")



ax.set_xlabel("Time slot number", fontsize = 30, color = "black")
ax.set_ylabel("Load time (cycles)", fontsize = 30, color = "black")

plt.show()
# plt.savefig('f1.jpg')
