#-*- coding: utf-8 -*-
import numpy as np
from tqdm import tqdm
# from numba import jit, prange,njit
from joblib import Parallel, delayed

LEN = 2000
F = open("../name.txt", "r")
FNAME = F.read()

tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_under2000.npy")

sig0 = []
# iddata = []
lis = []
for j in range(len(tmp[0]) - LEN):
    ave = np.average(tmp[0][j:j + LEN])
    lis.append(ave)
sig0 = lis - sum(lis)/len(lis)

def corr_all(i):
    avlist = []
    corr_list = int(0)
    if i == 0:
        corr_list = 0
    else:
        for j in range(len(tmp[0]) - LEN):
            ave = np.average(tmp[i][j:j + LEN])
            avlist.append(ave)
        sig1 = avlist - sum(avlist)/len(avlist)
        # print("ok 1")
        corr01 = np.correlate(sig0, sig1, "full")
        # print("ok 2")
        estimated_delay = corr01.argmax() - (len(sig0) - 1)
        corr_list = estimated_delay

    return corr_list, i

def main():
    print(len(tmp))
    print(len(tmp[0]))
    # sig0 = corr_f()
    print(sig0)
    processed = Parallel(n_jobs=-1, verbose = 3)([delayed(corr_all)(i) for i in range(len(tmp))])
    # print(processed[0])
    # print(processed[1])

    processed.sort(key=lambda x: x[1])
    processed_data = [t[0] for t in processed]
    # print(len(processed_data))
    # print(processed_data)
    np.save("../data_np/" + FNAME + "/" + FNAME + "_delay", processed_data)
    F.close()

if __name__ == '__main__':
    main()
