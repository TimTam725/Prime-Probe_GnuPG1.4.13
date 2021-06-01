#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

F = open("../name.txt", "r")
FNAME = F.read()
# tmp = np.load("./data/scan-elg.npy")
#f = open("../data/scan-gpg18_set57_4.csv", "r")
#tmp = np.loadtxt("../data/scan-gpg18_set57_4.csv", delimiter = ",")
# tmp = np.load("../data_np/scan-gpg13_set52_4000/scan-gpg13_set52_4000_cut10_split.npy")
tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_split.npy")

print(len(tmp))
print(len(tmp[0]))

# plt.show()   # axesはAxesオブジェクトの2x2の配列
id = [3000, 3000 + 1, 3000 + 2, 3000 + 3]
fig = plt.figure(figsize=(12, 8)) #...1
ax = fig.add_subplot(221) #...2
ax.plot(tmp[id[0]])
plt.title("set " + str(id[0]))
plt.xlabel("slot")
plt.ylabel("load time")
plt.ylim(0, 1000)
ax = fig.add_subplot(222) #...2
ax.plot(tmp[id[1]])
plt.title("set " + str(id[1]))
plt.xlabel("slot")
plt.ylabel("load time")
plt.ylim(0, 1000)
ax = fig.add_subplot(223) #...2
ax.plot(tmp[id[2]])
plt.title("set " + str(id[2]))
plt.xlabel("slot")
plt.ylabel("load time")
plt.ylim(0, 1000)
ax = fig.add_subplot(224) #...2
ax.plot(tmp[id[3]])
plt.title("set " + str(id[3]))
plt.xlabel("slot")
plt.ylabel("load time")
plt.ylim(0, 1000)
plt.show()
F.close()
