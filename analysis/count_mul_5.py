#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from joblib import Parallel, delayed

F = open("../name.txt", "r")
FNAME = F.read()
tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_split.npy")

SAMPLES = 15
LEN = 10000
THR = 200

# 連続してTHRよりも大きい場合 & cont > 3 & cont < SAMPLES
def count_mul(i):
    cnt = 0
    cont = 0
    pre = 0
    now = 0
    for j in range(len(tmp[i])):
        now = tmp[i][j]
        if pre < THR:
            if now >= THR:
                cont = 1
        else:
            if now >= THR:
                cont += 1
            else:
                if cont > 3 and cont < SAMPLES:
                    cnt += 1
                cont = 0
        pre = tmp[i][j]
    return cnt


def main():
    print(len(tmp))
    print(len(tmp[0]))
    c_out = Parallel(n_jobs=-1, verbose = 3)([delayed(count_mul)(i) for i in range(LEN)])
    print(len(c_out))
    fig = plt.figure(figsize=(12, 8)) #...1
    ax = fig.add_subplot(111)
    ax.hist(c_out, bins = 100, density = True, ec = "k", range = (300, 700))
    ax.set_title(FNAME + " : cont > 3 & cont < " + str(SAMPLES))
    # ax.set_title("hist : SAMPLES " + str(SAMPLES) + " count under SAMPLES")
    ax.set_xlabel("times")
    ax.set_ylabel("freq")
    # plt.ylim(0, 1000)
    # plt.savefig("../fig/" + FNAME + "/hist/hist_" + str(SAMPLES))
    # plt.savefig("../fig/" + FNAME + "/hist/hist_" + str(SAMPLES) + "_count_under_SAMPLES")
    plt.show()
    F.close()

if __name__ == '__main__':
    main()
