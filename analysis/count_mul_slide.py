#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from joblib import Parallel, delayed
# import seaborn as sns
import seaborn as sns; sns.set()

F = open("../name.txt", "r")
FNAME = F.read()
tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_split.npy")

SAMPLES = 8
LEN = 10000
THR = 200

# 連続してTHRよりも大きい場合 & cont > 1
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
                if cont > 2:
                    cnt += 1
                cont = 0
        pre = tmp[i][j]
    return cnt


def main():
    print(len(tmp))
    print(len(tmp[0]))
    c_out = Parallel(n_jobs=-1, verbose = 3)([delayed(count_mul)(i) for i in range(LEN)])
    print(len(c_out))
    # sns.distplot(c_out[0:LEN],kde=False, rug=False, color='black', bins=100, fit=norm)
    # sns.set()
    fig = plt.figure(figsize=(12, 8)) #...1
    # fig = plt.figure() #...1
    ax = fig.add_subplot(111)
    ax.set_title(FNAME + " : cont > 2")
    ax.set_xlabel("times")
    fig.text(0.2, 0.5, "correct time : 405")
    fig.text(0.2, 0.8, "SAMPLES : 10000")
    ax.set_ylabel("freq rate (max = 1.0)")
    plt.xticks(np.arange(250, 451, 10))
    ax.hist(c_out, bins = 200, density = True, ec = "k", range = (250, 450))
    # ax.PairGrid(iris)
    # ax.set()
    # plt.savefig("../fig/" + FNAME + "/hist/hist_" + FNAME + "_cont2")
    # plt.ylim(0, 1000)
    # plt.savefig("../fig/" + FNAME + "/hist/hist_" + str(SAMPLES))
    # plt.savefig("../fig/" + FNAME + "/hist/hist_" + str(SAMPLES) + "_count_under_SAMPLES")
    plt.show()
    F.close()

if __name__ == '__main__':
    main()
