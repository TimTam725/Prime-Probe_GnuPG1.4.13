#-*- coding: utf-8 -*-
import os
F = open("../name.txt", "r")
FNAME = F.read()
F2 = open("../setid.txt", "r")
FNAME2 = F2.read()

def main():
    data_np_path = "../data_np/"
    fig_path = "../fig/"
    # f = input("input folder name >>")
    # data_np_path
    if os.path.exists(data_np_path + FNAME):
        print(FNAME + " folder exists in " + data_np_path)
    else:
        os.mkdir(data_np_path + FNAME)
        print("maked " + FNAME + " folder in " + data_np_path)
    #fig_path
    if os.path.exists(fig_path + FNAME):
        print(FNAME + " folder exists in " + fig_path)
    else:
        os.mkdir(fig_path + FNAME)
        os.mkdir(fig_path + FNAME + "/set" + FNAME2)
        os.mkdir(fig_path + FNAME + "/set" + FNAME2 + "_delay")
        print("maked " + FNAME + " folder in " + fig_path)
    #hist_path
    if os.path.exists(fig_path + FNAME + "/hist"):
        print(FNAME + "/hist folder exists in " + fig_path)
    else:
        os.mkdir(fig_path + FNAME + "/hist")
        print("maked " + FNAME + " hist folder in " + fig_path)

    F.close()
    F2.close()

if __name__ == '__main__':
    main()
