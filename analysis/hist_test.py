#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from joblib import Parallel, delayed
import Levenshtein
# import seaborn as sns
import csv
import seaborn as sns; sns.set()

F = open("../name.txt", "r")
FNAME = F.read()
single = 2
SorM = 10
# tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_split.npy")
with open("../data_str/" + FNAME + "_str_" + "single" + str(single) + "_SorM" + str(SorM) + ".csv", 'r') as f:
    data = list(csv.reader(f, lineterminator='\n'))

LEN = 10000

real = "ssmsssssmssmsmsssmsmsmsmsmsssssmsmsmssmsmsssmsmsmsmsmsmsssmsmsms\
ssmssmsmssmsmssssmsmssmssssmssmssmsmssmssmssmssmsmssmsssssssmsmsssmsmsmsm\
sssmsssssmsmssmsssmssmsmssmssmssssssmsssmssssssssmsssmssssssmsmssmsssmssm\
ssmsmssmssmsssmsmssmsssssmssmsmssmsssmssmsssmssmsssmsmssmsmssmssmssssmssm\
ssmsmsmssmsssmsmsssssmssmsmsmsmsssmssmsmsmssmsmssmssmsmsmsmsmssmssmsmsmsm\
smssssmssssmsmsmssmsmsmsmssmsmsmsssssmsssmsmssssmsssmssmsmsmsmssmsssmsmsm\
smsmssssssmsmsmsmsmsssmsmsmssmssmssmsmssmsmssmssmsmssssmssmsssmssmsmssmss\
msmssssmsmsssssmsmsmsssmssssmsmssmsmsmssmsssssmssmssmsmssmssmsmsmsmssmsms\
smsssmsmsmsmsmsmsmsssmssmssssms"

# 連続してTHRよりも大きい場合 & cont > 1
def hist_check(i):
    temp = "".join(data[i])
    sum = len(temp) - 1
    sqr = temp.count("s")
    rev = Levenshtein.distance(temp, real)
    d = [sum, sqr, rev]
    return d


def main():
    print(len(data))
    # a = "".join(data[0])
    # print(a)
    # print(type(data[0]))
    # c_out = Parallel(n_jobs=-1, verbose = 3)([delayed(hist_check)(i) for i in range(LEN)])
    c_out = []
    for i in range(LEN):
        d = hist_check(i)
        c_out.append(d)
    hist_sum = [i[0] for i in c_out]
    hist_sqr = [i[1] for i in c_out]
    hist_mul = [(i[0] - i[1]) for i in c_out]
    hist_rev = [i[2] for i in c_out]
    # print(len(c_out))
    # sns.distplot(c_out[0:LEN],kde=False, rug=False, color='black', bins=100, fit=norm)
    # sns.set()
    fig = plt.figure(figsize=(12, 8)) #...1
    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    # fig = plt.figure() #...1
    ax = fig.add_subplot(411)
    ax.set_title("Length of Observed Operation Sequence")
    ax.set_xlabel("times")
    fig.text(0.2, 0.5, "correct time : 405")
    fig.text(0.2, 0.8, "SAMPLES : 10000")
    ax.set_ylabel("freq rate (max = 1.0)")
    plt.xticks(np.arange(605 - 25, 605 + 25 + 1, 5))
    ax.hist(hist_sum, bins = 50, density = True, ec = "k", range = (606 - 25, 606 + 25))

    ax = fig.add_subplot(412)
    ax.hist(hist_sqr, bins = 50, density = True, ec = "k", range = (404 - 25, 404 + 25))
    ax.set_title("Square")
    plt.xticks(np.arange(405 - 25, 405 + 25 + 1, 5))

    ax = fig.add_subplot(413)
    ax.set_title("Multiply")
    ax.hist(hist_mul, bins = 50, density = True, ec = "k", range = (202 - 25, 202 + 25))
    plt.xticks(np.arange(200 - 25, 200 + 25 + 1, 5))

    ax = fig.add_subplot(414)
    ax.set_title("Levenshtein Distance")
    ax.hist(hist_rev, bins = 50, density = True, ec = "k", range = (0, 50))
    # ax.set_xlabel("times")
    # fig.text(0.2, 0.5, "correct time : 405")
    # fig.text(0.2, 0.8, "SAMPLES : 10000")
    ax.set_ylabel("freq rate (max = 1.0)")
    # plt.xticks(np.arange(250, 451, 10))
    plt.show()
    F.close()

if __name__ == '__main__':
    main()
