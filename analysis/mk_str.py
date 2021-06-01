#-*- coding: utf-8 -*-
# import matplotlib.pyplot as plt
import numpy as np
from joblib import Parallel, delayed
import Levenshtein
import csv

F = open("../name.txt", "r")
FNAME = F.read()
# tmp = np.load("../data_np/" + FNAME + "/" + FNAME + ".npy")
tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_split.npy")
SAMPLES = 8
TH1 = 50
TH2 = 12
LEN = 10000
THR = 200

# 連続してTHRよりも大きい場合
def count_mul(i):
    cnt = 0
    pre = 0
    now = 0
    a = -1
    b = -1
    lis = ""
    for j in range(len(tmp[i])):
        now = tmp[i][j]
        if pre < THR:
            if now >= THR:
                b = j
        else:
            if now < THR:
                if (j - b - 1) > 2:
                    if (b - a) >= TH2:
                        lis += "sm"
                    else:
                        lis += "s"
                    # cnt += 1
                    a = j
                # upper_cont = 0
        pre = tmp[i][j]
    lis += "x"
    return lis


def main():
    print(len(tmp))
    print(len(tmp[0]))
    c_out = Parallel(n_jobs=-1, verbose = 3)([delayed(count_mul)(i) for i in range(LEN)])
    print(len(c_out))
    print(type(c_out[0]))
    print(c_out[0])
    # print(c_out)

    filename = "../data_str/" + FNAME + "_str.csv"
    with open(filename, 'w') as f:
        writer=csv.writer(f, lineterminator='\n')
        for row in c_out:
            if row is None:
                continue
            writer.writerow(row)
            # writer.writerow("".join(row))

    F.close()

if __name__ == '__main__':
    main()
