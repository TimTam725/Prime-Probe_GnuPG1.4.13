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

cor = "ssmsssssmssmsmsssmsmsmsmsmsssssmsmsmssmsmsssmsmsmsmsmsmsssmsmsms\
ssmssmsmssmsmssssmsmssmssssmssmssmsmssmssmssmssmsmssmsssssssmsmsssmsmsmsm\
sssmsssssmsmssmsssmssmsmssmssmssssssmsssmssssssssmsssmssssssmsmssmsssmssm\
ssmsmssmssmsssmsmssmsssssmssmsmssmsssmssmsssmssmsssmsmssmsmssmssmssssmssm\
ssmsmsmssmsssmsmsssssmssmsmsmsmsssmssmsmsmssmsmssmssmsmsmsmsmssmssmsmsmsm\
smssssmssssmsmsmssmsmsmsmssmsmsmsssssmsssmsmssssmsssmssmsmsmsmssmsssmsmsm\
smsmssssssmsmsmsmsmsssmsmsmssmssmssmsmssmsmssmssmsmssssmssmsssmssmsmssmss\
msmssssmsmsssssmsmsmsssmssssmsmssmsmsmssmsssssmssmssmsmssmssmsmsmsmssmsms\
smsssmsmsmsmsmsmsmsssmssmssssms"

# 連続してTHRよりも大きい場合 & cont > 1
def hist_levedit(i):
    obs = "".join(data[i])
    # rev = Levenshtein.distance(temp, cor)
    editops = Levenshtein.editops(obs, cor)
    # 編集内容のカウント
    # [N->S, N->M, S->N, M->N, S->M, M->S]
    count=[0, 0, 0, 0, 0, 0]
    for t in editops:
        # insert の場合
        if t[0] == "insert":
            if cor[t[2]] == "s":
                count[0]+=1


            elif cor[t[2]] == "m":
                count[1]+=1

            # else:
            #     print("error : unexpected correct word.")
            #     quit()

        # delete の場合
        elif t[0] == "delete":
                if obs[t[1]] == "s":
                    count[2]+=1

                elif obs[t[1]] == "m":
                    count[3]+=1

                # else:
                #     print("error : unexpected obtain word.")
                #     quit()

            # replace の場合
        elif t[0] == "replace":
                if (obs[t[1]] == "s") and (cor[t[2]] == "m"):
                    count[4]+=1

                elif (obs[t[1]] == "m") and (cor[t[2]] == "s"):
                    count[5]+=1

            # else:
            #     print("error : unexpected Replace word.")
            #     quit()

        # else:
        #     print("Error : tuple 0 is unexpected edit.")
        #     quit()
    return count


def main():
    print(len(data))
    # lev_data = Parallel(n_jobs=-1, verbose = 3)([delayed(hist_levedit)(i) for i in range(LEN)])

    ins_s = []
    ins_m = []
    del_s = []
    del_m = []
    rep_s = []
    rep_m = []
    for i in range(LEN):
        lev = hist_levedit(i)
        # lev_data.append(lev)
        ins_s.append(lev[0])
        ins_m.append(lev[1])
        del_s.append(lev[2])
        del_m.append(lev[3])
        rep_s.append(lev[4])
        rep_m.append(lev[5])

    # ins_s = [i[0] for i in lev_data]
    # ins_m = [i[1] for i in lev_data]
    # del_s = [i[2] for i in lev_data]
    # del_m = [i[3] for i in lev_data]
    # rep_s = [i[4] for i in lev_data]
    # rep_m = [i[5] for i in lev_data]
    # print(len(c_out))
    # sns.distplot(c_out[0:LEN],kde=False, rug=False, color='black', bins=100, fit=norm)
    # sns.set()
    fig = plt.figure(figsize=(16, 9)) #...1
    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    plt.rc('legend', fontsize=16)
    # fig = plt.figure() #...1
    # fig.text(0.2, 0.5, "correct time : 405")
    # fig.text(0.2, 0.8, "SAMPLES : 10000")
    ax = fig.add_subplot(311)
    ax.set_title("insert edit hist", fontsize = 20, color = "black")
    ax.hist(ins_s, bins = 20, density = True, ec = "k", range = (0, 20), label="Null -> Square")
    ax.hist(ins_m, bins = 20, density = True, ec = "k", range = (0, 20), label="Null -> Multiply", color="cyan")
    ax.set_xlabel("Number of insertions", fontsize = 15, color = "black")
    ax.set_ylabel("freq.(max = 1.0)", fontsize = 15, color = "black")
    plt.legend()
    plt.xticks(np.arange(0, 21, 1), fontsize = 15, color = "black")
    plt.yticks(fontsize = 15, color = "black")

    ax = fig.add_subplot(312)
    ax.set_title("delete edit hist", fontsize = 20, color = "black")
    ax.hist(del_s, bins = 20, density = True, ec = "k", range = (0, 20), label="Square -> NULL")
    ax.hist(del_m, bins = 20, density = True, ec = "k", range = (0, 20), label="Multiply -> NULL", color="cyan")
    ax.set_xlabel("Number of deletions", fontsize = 15, color = "black")
    ax.set_ylabel("freq.(max = 1.0)", fontsize = 15, color = "black")
    plt.legend()
    plt.xticks(np.arange(0, 21, 1), fontsize = 15, color = "black")
    plt.yticks(fontsize = 15, color = "black")

    ax = fig.add_subplot(313)
    ax.set_title("replace edit hist", fontsize = 20, color = "black")
    ax.hist(rep_s, bins = 20, density = True, ec = "k", range = (0, 20), label="Square -> Multiply")
    ax.hist(rep_m, bins = 20, density = True, ec = "k", range = (0, 20), label="Multiply -> Square", color="cyan")
    ax.set_xlabel("Number of replacements", fontsize = 15, color = "black")
    ax.set_ylabel("freq.(max = 1.0)", fontsize = 15, color = "black")
    plt.legend()
    plt.xticks(np.arange(0, 21, 1), fontsize = 15, color = "black")
    plt.yticks(fontsize = 15, color = "black")

    # plt.show()
    plt.savefig("../../data_slide/fig/" + FNAME + "_str_" + "single" + str(single) + "_SorM" + str(SorM) + "_levdis_editops")
    F.close()

if __name__ == '__main__':
    main()
