#-*- coding: utf-8 -*-
import numpy as np

F = open("../name.txt", "r")
FNAME = F.read()
tmp = np.load("../data_np/" + FNAME + "/"+ FNAME + ".npy")

def main():

    print(len(tmp)) # 128 + SAMPLES2になってほしい
    print(len(tmp[0 : 10])) # 128 + SAMPLES2になってほしい
    print(tmp[0:10])
    np.save("../data_np/" + FNAME + "/" + FNAME + "_cut10", tmp[0:10])
    print("finish")
    F.close()

if __name__ == '__main__':
    main()
