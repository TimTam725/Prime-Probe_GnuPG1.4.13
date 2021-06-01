#-*- coding: utf-8 -*-
# import matplotlib.pyplot as plt
import numpy as np
from joblib import Parallel, delayed
import matplotlib.pyplot as plt
import csv
import seaborn as sns; sns.set()

F = open("../../name.txt", "r")
FNAME = F.read()
# tmp = np.load("../data_np/" + FNAME + "/" + FNAME + ".npy")
tmp = np.load("../../data_slide/data_np/" + FNAME + "_split.npy")
# SAMPLES = 8
LEN = 10000
THR = 200
L = len(tmp[0])

# 連続してTHRよりも大きい場合
def count_mul(i, single, SorM):
    pre = 0
    now = 0
    a = -1
    b = -1
    count = []
    for j in range(L):
        now = tmp[i][j]
        if pre < THR:
            if now >= THR:
                b = j
        else:
            if now < THR:
                if a == -1: #初期状態
                    a = j
                else:
                    # if (j - b - 1) > single:
                    #     if (b - a) >= SorM:
                    #         lis += "sm"
                    #     else:
                    #         lis += "s"
                    #     # cnt += 1
                    count.append(j - b)
                    a = j
                # upper_cont = 0
        pre = tmp[i][j]
    # lis += "x"
    if a > b:
        count.append(a - b)
    else:
        count.append(L - b)
    return count


def main():
    print(len(tmp))
    print(len(tmp[0]))
    single = 3
    SorM = 10
    c_out = Parallel(n_jobs=-1, verbose = 3)([delayed(count_mul)(i, single, SorM) for i in range(LEN)])
    print(len(c_out))
    print(type(c_out[0]))
    print(c_out[0])
    lis = [len(i) for i in c_out]

    fig = plt.figure(figsize=(16, 9)) #...1
    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    # fig = plt.figure() #...1
    # fig.text(0.2, 0.5, "correct time : 405")
    # fig.text(0.2, 0.8, "SAMPLES : 10000")

    ax = fig.add_subplot(111)
    plt.axvline(x = 404.5, color = "red")
    # plt.xticks([404], fontsize = 15, color = "red")
    # plt.xticks(404, color = "red", fontsize = 15)
    # ax.set_title("Levenshtein Distance")
    ax.hist(lis, bins = 250, density = True, ec = "k", range=(300, 550))
    # ax.set_title("Observed timing")
    ax.set_xlabel("Times", fontsize = 30, color = "black")
    ax.set_ylabel("freq.(max = 1.0)", fontsize = 30, color = "black")
    fig.text(0.7, 0.82, "SAMPLES : 10000", fontsize = 25, color = "black")
    fig.text(0.16, 0.6, "correct times : 404", fontsize = 32, color = "red")
    plt.xticks(np.arange(300, 551, 25), fontsize = 15, color = "black")
    plt.yticks(fontsize = 15, color = "black")
    # plt.show()
    plt.savefig("../../data_slide/fig/" + FNAME + "_count")
    # print(c_out)

    # filename = "../../data_slide/data_str/" + FNAME + "_str_" + "single" + str(single) + "_SorM" + str(SorM) + ".csv"
    # with open(filename, 'w') as f:
    #     writer=csv.writer(f, lineterminator='\n')
    #     for row in c_out:
    #         if row is None:
    #             continue
    #         writer.writerow(row)
            # writer.writerow("".join(row))

    F.close()

if __name__ == '__main__':
    main()
