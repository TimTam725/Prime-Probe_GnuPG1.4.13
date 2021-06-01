#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from joblib import Parallel, delayed
import Levenshtein
# import seaborn as sns
import csv
import seaborn as sns; sns.set()

F = open("../../name.txt", "r")
FNAME = F.read()
single = 3
SorM = 10
# tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_split.npy")
with open("../../data_slide/data_str/" + FNAME + "_str_" + "single" + str(single) + "_SorM" + str(SorM) + ".csv", 'r') as f:
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
def hist_sm(i):
    temp = "".join(data[i])
    sum = len(temp) - 1
    sqr = temp.count("s")
    d = [sum, sqr]
    return d


def main():
    print(len(data))
    # a = "".join(data[0])
    # print(a)
    # print(type(data[0]))
    # c_out = Parallel(n_jobs=-1, verbose = 3)([delayed(hist_check)(i) for i in range(LEN)])
    c_out = []
    for i in range(LEN):
        d = hist_sm(i)
        c_out.append(d)
    hist_sum = [i[0] for i in c_out]
    hist_sqr = [i[1] for i in c_out]
    hist_mul = [(i[0] - i[1]) for i in c_out]
    # hist_rev = [i[2] for i in c_out]
    # print(len(c_out))
    # sns.distplot(c_out[0:LEN],kde=False, rug=False, color='black', bins=100, fit=norm)
    # sns.set()
    fig = plt.figure(figsize=(16, 9)) #...1
    # plt.title(FNAME + "_str_single" + str(single) + "_SorM" + str(SorM))
    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    # fig = plt.figure() #...1
    ax = fig.add_subplot(311)
    ax.set_title("Length of Observed Operation Sequence", fontsize = 20, color = "black")
    ax.set_xlabel("times", fontsize = 15, color = "black")
    ax.set_ylabel("freq.(max = 1.0)", fontsize = 15, color = "black")
    fig.text(0.18, 0.82, "SAMPLES : 10000", color = "black", fontsize = 15)
    fig.text(0.33, 0.75, "correct length : 606", fontsize = 25, color = "red")
    ax.hist(hist_sum, bins = 50, density = True, ec = "k", range = (606 - 25 - 5, 606 + 25 - 5))
    plt.xticks(np.arange(605 - 10 - 25, 605 + 25 - 10 + 1, 5), color = "black", fontsize = 15)
    plt.yticks(color = "black", fontsize = 15)
    plt.axvline(x = 606.5, color = "red")

    ax = fig.add_subplot(312)
    ax.set_title("Square timing", fontsize = 20, color = "black")
    ax.set_xlabel("times", fontsize = 15, color = "black")
    ax.set_ylabel("freq.(max = 1.0)", fontsize = 15, color = "black")
    fig.text(0.18, 0.52, "SAMPLES : 10000", color = "black", fontsize = 15)
    fig.text(0.57, 0.50, "correct times : 404", fontsize = 25, color = "red")
    plt.axvline(x = 404.5, color = "red")
    ax.hist(hist_sqr, bins = 50, density = True, ec = "k", range = (404 - 25, 404 + 25))
    plt.xticks(np.arange(405 - 25, 405 + 25 + 1, 5), color = "black", fontsize = 15)
    plt.yticks(color = "black", fontsize = 15)

    # patch = patches.Arrow(x=0.5, y=0.5, dx=0.2, dy=0.2, width=0.1)
    ax = fig.add_subplot(313)
    ax.set_title("Multiply timing", fontsize = 20, color = "black")
    ax.set_xlabel("times", fontsize = 15, color = "black")
    ax.set_ylabel("freq.(max = 1.0)", fontsize = 15, color = "black")
    fig.text(0.18, 0.22, "SAMPLES : 10000", color = "black", fontsize = 15)
    fig.text(0.35, 0.20, "correct times : 202", fontsize = 25, color = "red")
    plt.axvline(x = 202.5, color = "red")
    ax.hist(hist_mul, bins = 50, density = True, ec = "k", range = (202 - 25 - 5, 202 + 25 - 5))
    plt.xticks(np.arange(200 - 25 - 5, 200 + 25 - 5 + 1, 5), color = "black", fontsize = 15)
    plt.yticks(color = "black", fontsize = 15)
    # plt.show()
    plt.savefig("../../data_slide/fig/" + FNAME + "_str_" + "single" + str(single) + "_SorM" + str(SorM))
    F.close()

if __name__ == '__main__':
    main()
