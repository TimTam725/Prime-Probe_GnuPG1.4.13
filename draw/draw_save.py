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

# tmp = np.load("./data/scan-elg.npy")
f = open("../data/scan-gpg18_set57_4.csv", "r")
tmp = np.loadtxt("../data/scan-gpg18_set57_4.csv", delimiter = ",")

print(len(tmp))
print(len(tmp[0]))

for i in tqdm(range(len(tmp))):
    fig = plt.figure(figsize=(12, 8)) #...1
    ax = fig.add_subplot(111) #...2
    ax.plot(tmp[i])
    plt.title("set " + str(i))
    plt.xlabel("slot")
    plt.ylabel("load time")
    plt.ylim(0, 1000)
    plt.savefig("../fig/scan-gpg18_set57_4/scan-gpg18_" + str(int(i / 4)) + "v" + str(i % 4))
    # plt.savefig("../fig/sys-elg_loop/scan-elg_loop" + str(i))
    plt.close()
# for i in tqdm(range(len(tmp))):
#     if i == mulid[id]:
#         # print("kita")
#         id += 1
#         fig = plt.figure(figsize=(12, 8)) #...1
#         ax = fig.add_subplot(111) #...2
#         ax.plot(tmp[i])
#         plt.title("set " + str(i))
#         plt.xlabel("slot")
#         plt.ylabel("load time")
#         plt.ylim(0, 1000)
#         plt.savefig("./fig/scan-elg_all/scan-elg" + str(i))
#         plt.close()
#         if id == len(mulid):
#             break
#     else:
#         continue
