'''A script to load annotated csvs into gcloud compute instance'''
import os
import numpy as np
nums = np.arange(101, 131)
csv_paths = ['csh{}/csh{}.ann.features.csv'.format(num, num) for num in nums]
path = '/home/dyllanjr/Desktop/home_ann_csvs/'
for csv in csv_paths:
    os.system('gcloud compute scp {} instance-1:~'.format(path + csv))
