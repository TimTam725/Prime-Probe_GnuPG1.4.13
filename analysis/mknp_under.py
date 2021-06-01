#-*- coding: utf-8 -*-
import numpy as np
from joblib import Parallel, delayed

THR = 2000
F = open("../name.txt", "r")
FNAME = F.read()
tmp = np.load("../data_np/" + FNAME + "/"+ FNAME + ".npy")
SAMPLES = 4000
# OFFSET = 128

def _under2000(i):
    lis = np.zeros(len(tmp[0]))
    for j in range(len(tmp[i])):
        if tmp[i][j] > THR:
            lis[j] = THR
        else:
            lis[j] = tmp[i][j]
    return lis, i

def main():
    print(len(tmp))
    print(len(tmp[0]))
    ans = np.zeros((SAMPLES, len(tmp[0])))
    para_out = Parallel(n_jobs=-1, verbose = 3)([delayed(_under2000)(i) for i in range(SAMPLES)])
    para_out.sort(key=lambda x: x[1])
    for i in range(SAMPLES):
        ans[i] = para_out[i][0]
    print(ans[0])
    np.save("../data_np/" + FNAME + "/" + FNAME + "_under2000", ans)
    F.close()

if __name__ == '__main__':
    main()
