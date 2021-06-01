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
L = len(tmp[0])
# TH1 = 50
# TH2 = 12
LEN = 10000
THR = 200

# 連続してTHRよりも大きい場合
def count_mul(i, single, SorM):
    pre = 0
    now = 0
    a = -1
    b = -1
    c = -1
    lis = ""
    for j in range(L):
        now = tmp[i][j]
        if pre < THR:
            if now >= THR:
                b = j
        else:
            if now < THR:
                if a == -1: #初期状態
                    a = j
                    c = j - b - 1
                else:
                    if (j - b - 1) > single: #自乗算が観測できた場合
                        if (b - a) >= SorM:
                            if c >= single:
                                lis += "s" * int(c / single)
                                lis += "m"
                            else:
                                lis += "sm"
                        else:
                            if c >= single:
                                lis += "s" * int(c / single)
                            else:
                                lis += "s"
                        a = j
                        c = j - b - 1
                    # cnt += 1
                # upper_cont = 0
        pre = tmp[i][j]
        #debug
        # print(j, end="")
        # print(" now : ", end="")
        # print(now, end="")
        # print(" pre : ", end="")
        # print(pre)
        # print("a : ", end = "")
        # print(a, end = "")
        # print(" b : ", end = "")
        # print(b, end = "")
        # print(" c : ", end = "")
        # print(c)
    lis += "x"
    return lis


def main():
    print(len(tmp))
    print(len(tmp[0]))
    # top = 2
    # single = 8
    # SorM = 10
    for single in range(1, 10):
        for SorM in range(5, 20):
            print("single : ", end = "")
            print(single, end = "")
            print(" SorM : ", end = "")
            print(SorM)
            c_out = Parallel(n_jobs=-1, verbose = 1)([delayed(count_mul)(i, single, SorM) for i in range(LEN)])
            #保存
            filename = "../data_str/" + FNAME + "_str_single" + str(single) + "_SorM" + str(SorM) + ".csv"
            with open(filename, 'w') as f:
                writer=csv.writer(f, lineterminator='\n')
                for row in c_out:
                    if row is None:
                        continue
                    writer.writerow(row)
    # print(len(c_out[0]))
    # print(c_out[0])
    # for top in range(0, 5):
    #     print(len(c_out))
    #     print(type(c_out[0]))
    #     print(c_out[0])
    # print(c_out)

    # filename = "../data_str/" + FNAME + "_str.csv"
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
