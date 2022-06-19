# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 21:49:27 2022

@author: abhisek
"""
## This script plots a single file
import pandas as pd
import matplotlib.pyplot as plt
from tofData import tofdata 

plt.close('all')

dirPath='E:/dataAnalysis/tip RPA/new/20220519/G/TipVerticalScan/20220519_G_run1/'
Angle=176


settings=pd.read_csv(dirPath+'settings.csv')


row=settings.loc[settings['Angle']==Angle]
fileName=dirPath+row['FileName'].values[0]

td=tofdata(fileName,level_empty_data=False, threshold =0.1)
td.plotSignal()
print('counts =',td.getCounts())

