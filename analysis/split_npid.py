#-*- coding: utf-8 -*-
# import matplotlib.pyplot as plt
import numpy as np
from joblib import Parallel, delayed

F = open("../name.txt", "r")
FNAME = F.read()

tmp = np.load("../data_np/" + FNAME + "/" + FNAME + ".npy")
delay = np.load("../data_np/" + FNAME + "/" + FNAME + "_delay.npy").astype(int)
SAMPLES = 4000
#gpg18_set26_4000
N = 3
LEN = 7200
id = [3850, 13450, 23200]
chek_list = [0] * LEN
check_len = len(tmp[0])
# LEN = 7000
#gpg18_set22_4000
# id = [5250, 14250, 22750]
# id = [6500, 15250, 23900]
# N = 1
# LEN = 16000
# id = [11000]

def delay_tmp(i):
    id2 = id - delay[int(i / N)]
    if (id2[i % N] + LEN) >= check_len or id2[i % N] >= check_len:
        lis = chek_list
    else:
        lis = tmp[int(i / N)][id2[i % N]:id2[i % N] + LEN]

    return lis, i

def main():
    para_out = Parallel(n_jobs=-1, verbose = 3)([delayed(delay_tmp)(i) for i in range(SAMPLES * N)])
    para_out.sort(key=lambda x: x[1])
    ans = np.zeros((SAMPLES * N, LEN))
    # print(para_out[])
    # print(type(para_out))
    # print(para_out)
    # print(type(para_out[0]))
    # print(para_out[0])
    # print(type(para_out[0][0]))
    # print(para_out[0][0])
    # print(len(para_out[0][0]))
    # print(len(para_out[0]))
    # print(para_out[0][1])
    cnt = 0
    # lis = []
    check = 0
    for i in range(len(para_out)):
        if all((elem == 0 for elem in para_out[i][0])):
            check += 1
        else:
            ans[cnt] = para_out[i][0]
            cnt += 1

            # lis.append(i)
    print(cnt)
    print(check)
    print(check + cnt)
    print(ans)
    # print(lis)
        # for j in range(LEN):
    np.save("../data_np/" + FNAME + "/" + FNAME + "_split", ans)
    F.close()

if __name__ == '__main__':
    main()
