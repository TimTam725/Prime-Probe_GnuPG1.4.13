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
# tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_split.npy")

LEN = 10000

def main():

    for single in range(1, 10):
        for SorM in range(5, 20):
            with open("../data_str/" + FNAME + "_str_single" + str(single) + "_SorM" + str(SorM) + ".csv", 'r') as f:
                data = list(csv.reader(f, lineterminator='\n'))
            c_out = []
            for i in range(LEN):
                temp = "".join(data[i])
                sum = len(temp) - 1
                sqr = temp.count("s")
                # rev = Levenshtein.distance(temp, real)
                d = [sum, sqr]
                c_out.append(d)
            hist_sum = [i[0] for i in c_out]
            hist_sqr = [i[1] for i in c_out]
            hist_mul = [(i[0] - i[1]) for i in c_out]
            fig = plt.figure(figsize=(12, 8)) #...1
            # fig = plt.figure() #...1
            ax = fig.add_subplot(311)
            ax.set_title("Length of Observed Operation Sequence")
            ax.set_xlabel("times")
            # fig.text(0.2, 0.5, "correct time : 405")
            # fig.text(0.2, 0.8, "SAMPLES : 10000")
            ax.set_ylabel("freq rate (max = 1.0)")
            # plt.xticks(np.arange(605 - 25, 605 + 25 + 1, 5))
            ax.hist(hist_sum, bins = 50, density = True, ec = "k")
            # ax.hist(hist_sum, bins = 50, density = True, ec = "k", range = (606 - 25, 606 + 25))

            ax = fig.add_subplot(312)
            ax.hist(hist_sqr, bins = 50, density = True, ec = "k")
            # ax.hist(hist_sqr, bins = 50, density = True, ec = "k", range = (404 - 25, 404 + 25))
            ax.set_title("Square")
            # plt.xticks(np.arange(405 - 25, 405 + 25 + 1, 5))

            ax = fig.add_subplot(313)
            ax.set_title("Multiply")
            ax.hist(hist_mul, bins = 50, density = True, ec = "k")
            # ax.hist(hist_mul, bins = 50, density = True, ec = "k", range = (202 - 25, 202 + 25))
            # plt.xticks(np.arange(200 - 25, 200 + 25 + 1, 5))
            filename = "../fig/" + FNAME + "/hist_str/" + FNAME + "_str_single" + str(single) + "_SorM" + str(SorM)
            plt.savefig(filename)
            plt.close()
    # sns.set()
    # ax = fig.add_subplot(414)
    # ax.hist(hist_rev, bins = 100, density = True, ec = "k")
    # ax.set_title(FNAME + " : cont > 2")
    # ax.set_xlabel("times")
    # fig.text(0.2, 0.5, "correct time : 405")
    # fig.text(0.2, 0.8, "SAMPLES : 10000")
    # ax.set_ylabel("freq rate (max = 1.0)")
    # plt.xticks(np.arange(250, 451, 10))
    # plt.show()
    F.close()

if __name__ == '__main__':
    main()
