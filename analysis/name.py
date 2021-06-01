#-*- coding: utf-8 -*-
# import numpy as np
# FNAME = input()
f = open("../data_np/scan-gpg18_set34_1000/name.txt", "r")
FNAME = f.read()
print(FNAME[0])
print(FNAME)
f.close()
