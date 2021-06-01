#-*- coding: utf-8 -*-
# import matplotlib.pyplot as plt
import numpy as np
from joblib import Parallel, delayed
import Levenshtein

F = open("../name.txt", "r")
FNAME = F.read()
tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_cut10_split.npy")
# tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_split.npy")
st = "ssmsssssmssmsmsssmsmsmsmsmsssssmsmsmssmsmsssmsmsmsmsmsmsssmsmsms\
ssmssmsmssmsmssssmsmssmssssmssmssmsmssmssmssmssmsmssmsssssssmsmsssmsmsmsm\
sssmsssssmsmssmsssmssmsmssmssmssssssmsssmssssssssmsssmssssssmsmssmsssmssm\
ssmsmssmssmsssmsmssmsssssmssmsmssmsssmssmsssmssmsssmsmssmsmssmssmssssmssm\
ssmsmsmssmsssmsmsssssmssmsmsmsmsssmssmsmsmssmsmssmssmsmsmsmsmssmssmsmsmsm\
smssssmssssmsmsmssmsmsmsmssmsmsmsssssmsssmsmssssmsssmssmsmsmsmssmsssmsmsm\
smsmssssssmsmsmsmsmsssmsmsmssmssmssmsmssmsmssmssmsmssssmssmsssmssmsmssmss\
msmssssmsmsssssmsmsmsssmssssmsmssmsmsmssmsssssmssmssmsmssmssmsmsmsmssmsms\
smsssmsmsmsmsmsmsmsssmssmssssms"
SAMPLES = 8
TH = 10
LEN = 3
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
                    if (b - a) >= TH:
                        lis += "sm"
                    else:
                        lis += "s"
                    cnt += 1
                    a = j
                # upper_cont = 0
        pre = tmp[i][j]
    return cnt, lis


def main():
    print(len(tmp))
    print(len(tmp[0]))
    c_out = Parallel(n_jobs=-1, verbose = 3)([delayed(count_mul)(i) for i in range(0, 0 + LEN)])
    print(len(c_out))
    for i in range(LEN):
        moji = c_out[i][1]
        print(Levenshtein.ratio(moji, st))
        print(Levenshtein.editops(moji, st))
        print(moji)
        print("moji len : ", end="")
        print(len(moji))
        print("cnt : ", end="")
        print(c_out[i][0])
        # print(len(moji))
    # print(moji)
    # print(type(c_out[0][1]))
    # print(st)
    # plt.ylim(0, 1000)
    # plt.show()
    F.close()

if __name__ == '__main__':
    main()
