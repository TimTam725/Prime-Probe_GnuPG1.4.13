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
def hist_levdis(i):
    temp = "".join(data[i])
    rev = Levenshtein.distance(temp, real)
    return rev


def main():
    print(len(data))
    lev_data = []
    for i in range(LEN):
        lev = hist_levdis(i)
        lev_data.append(lev)
    # print(len(c_out))
    # sns.distplot(c_out[0:LEN],kde=False, rug=False, color='black', bins=100, fit=norm)
    # sns.set()
    fig = plt.figure(figsize=(16, 9)) #...1
    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    # fig = plt.figure() #...1
    fig.text(0.50, 0.8, "SAMPLES : 10000", fontsize = 20, color = "black")
    # fig.text(0.4, 0.5, "correct length : 405", fontsize = 15)

    ax = fig.add_subplot(111)
    # ax.set_title("Levenshtein Distance")
    ax.hist(lev_data, bins = 50, density = True, ec = "k", range = (0, 50))
    ax.set_xlabel("Levenshtein Distance", fontsize = 30, color = "black")
    ax.set_ylabel("freq.(max = 1.0)", fontsize = 30, color = "black")
    plt.xticks(np.arange(0, 51, 5), fontsize = 15, color = "black")
    plt.yticks(color = "black", fontsize = 15)
    # plt.show()
    plt.savefig("../../data_slide/fig/" + FNAME + "_str_" + "single" + str(single) + "_SorM" + str(SorM) + "_levdis")
    F.close()

if __name__ == '__main__':
    main()
