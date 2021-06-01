#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from joblib import Parallel, delayed

DRAWLEN = 10

F = open("../name.txt", "r")
FNAME = F.read()
F2 = open("../setid.txt", "r")
SETID = F2.read()
tmp = np.load("../data_np/" + FNAME + "/" + FNAME + ".npy")


def draw_single(i):
    fig = plt.figure(figsize=(12, 8)) #...1
    ax = fig.add_subplot(111) #...2
    ax.plot(tmp[i])
    plt.title("set " + str(int(i)))
    plt.xlabel("slot")
    plt.ylabel("load time")
    plt.ylim(0, 1000)
    # plt.ylim(0, 12)
    plt.savefig("../fig/" + FNAME + "/set"+ SETID + "/scan-gpg18_" + str(i))
    # plt.savefig("../fig/sys-elg_loop/scan-elg_loop" + str(i))
    plt.close()

def main():
    print(len(tmp))
    print(len(tmp[0]))
    print(FNAME)
    Parallel(n_jobs=-1, verbose = 3)([delayed(draw_single)(i) for i in range(DRAWLEN)])
    F.close()
    F2.close()

if __name__ == '__main__':
    main()
