#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

F = open("../name.txt", "r")
FNAME = F.read()

# tmp = np.load("../data_np/" + FNAME + "/" + FNAME + ".npy")
tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_cut10.npy")
# sample 1000 slot 5000
LEN = 7200
# sample 1000 slot 2000
# LEN = 16000

def main():
    # sample 100
    # id = [5700, 14500, 23250]
    # sample 1000
    # id = [6500, 15250, 23900]
    # id = [11000, 12000, 13000]
    #scan-gpg18_set
    # set26
    # id = [6600, 15300, 23900]
    #set34
    # id = [5400, 14000, 22600]
    #set7
    # id = [4100, 12400, 21400]
    #set18
    # id = [4100, 12800, 21450]
    #set23
    # id = [1800, 10500, 19000]
    #set51
    # id = [5250, 14000, 22650]
    #set56
    # id = [7850, 16400, 25200]
    #set61
    # id = [5100, 13500, 22400]

    #scan-gpg13_set
    #set57
    # id = [3700, 13300, 23000]
    #set59
    # id = [3900, 13450, 23100]
    #set6
    # id = [3350, 13000, 22650]
    #set52
    id = [3850, 13450, 23200]


    fig = plt.figure(figsize=(12, 8)) #...1

    ax = fig.add_subplot(311)
    plt.title("set 0")
    plt.xlabel("slot")
    plt.ylabel("load time")
    plt.plot(tmp[0][id[0]:id[0] + LEN])
    plt.ylim(0, 2000)

    ax = fig.add_subplot(312)
    # plt.title("set 1")
    plt.xlabel("slot")
    plt.ylabel("load time")
    plt.plot(tmp[0][id[1]:id[1] + LEN])
    plt.ylim(0, 2000)

    ax = fig.add_subplot(313)
    # plt.title("set 2")
    plt.xlabel("slot")
    plt.ylabel("load time")
    plt.plot(tmp[0][id[2]:id[2] + LEN])
    plt.ylim(0, 2000)

    plt.show()
    F.close()

if __name__ == '__main__':
    main()
