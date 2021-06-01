#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from joblib import Parallel, delayed

F = open("../name.txt", "r")
FNAME = F.read()
tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_split.npy")
# tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_cut10_split.npy")

SAMPLES = 8
LEN = 10
THR = 200

# 連続してTHRよりも大きい場合 & cont > 3
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
    print(tmp)
    c_out = Parallel(n_jobs=-1, verbose = 3)([delayed(count_mul)(i) for i in range(3000, 3000 + LEN)])
    print(len(c_out))
    print(tmp[3000:3000 + LEN])
    for i in range(LEN):
        print(c_out[i])
    # plt.show()
    F.close()

if __name__ == '__main__':
    main()
