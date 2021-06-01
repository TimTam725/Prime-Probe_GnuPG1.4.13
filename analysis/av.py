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

plt.figure(figsize=(12, 8)) #...1
# plt.title(str(id[i]))
plt.subplot(4, 1, 1) #...2
avlist = []
# sqlist = tmp[id[0]][0 : 100] ** 2
# print(sqlist)
# print(tmp[id[0]][0 : 100])
for j in range(len(tmp[0]) - LEN):
    ave = np.average(tmp[id[0]][j:j + LEN])
    avlist.append(ave)
plt.plot(avlist)
plt.subplot(4, 1, 2) #...2
avlist = []
for j in range(len(tmp[0]) - LEN):
    ave = np.average(tmp[id[1]][j:j + LEN])
    avlist.append(ave)
plt.plot(avlist)
plt.subplot(4, 1, 3) #...2
avlist = []
for j in range(len(tmp[0]) - LEN):
    ave = np.average(tmp[id[2]][j:j + LEN])
    avlist.append(ave)
plt.plot(avlist)
plt.subplot(4, 1, 4) #...2
avlist = []
for j in range(len(tmp[0]) - LEN):
    ave = np.average(tmp[id[3]][j:j + LEN])
    avlist.append(ave)
plt.plot(avlist)
# for i in tqdm(range(len(id))):
# plt.plot(np.abs(F1), color="b")

plt.show()
