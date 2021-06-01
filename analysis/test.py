#-*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt

LEN = 7200
lis = [0] * LEN
# print(lis)

if all((elem == 0 for elem in lis)):
    print("Yes")
else:
    print("No")

str = "aa"
str += "b" * int(3)
print(str)
# fig.savefig('4-1_a.png', facecolor=fig.get_facecolor())
# F = open("../name.txt", "r")
# FNAME = F.read()
#
# tmp = np.load("../data_np/" + FNAME + "/" + FNAME + "_delay.npy").astype(int)
#
# print(len(tmp))
# print(tmp)
# F.close()
