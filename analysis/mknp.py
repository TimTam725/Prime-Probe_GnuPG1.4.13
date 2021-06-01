#-*- coding: utf-8 -*-
import numpy as np

def main():
    F = open("../name.txt", "r")
    FNAME = F.read()

    tmp = np.loadtxt("../data/" + FNAME + ".csv", delimiter = ",")
    print(len(tmp)) # 128 + SAMPLES2になってほしい
    np.save("../data_np/" + FNAME + "/" + FNAME, tmp[128:])
    print("finish")
    F.close()

if __name__ == '__main__':
    main()
