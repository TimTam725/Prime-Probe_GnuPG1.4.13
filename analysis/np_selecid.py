#-*- coding: utf-8 -*-
import numpy as np
import csv

SAMPLES = 100
ID = 47
tmp = np.load("../data_np/set34_all/scan-gpg18_set34_100.npy")

np.save("../data_np/set34_100_id47/set34_100_id47", tmp[SAMPLES * ID : SAMPLES * ID + SAMPLES])
