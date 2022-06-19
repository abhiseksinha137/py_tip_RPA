# This program will plot the counts for different values of threshold in a single directory for Angular 
# Data


from tofData import tofdata 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pi=np.pi
plt.close('all')

dirPath='E:/dataAnalysis/tip RPA/new/20220519/G/TipVerticalScan/20220519_G_run1/'
settings=pd.read_csv(dirPath+'settings.csv')
settings=settings.sort_values(by='Angle')
fileNames=settings['FileName'].values
Angles=settings['Angle'].values

counts=[]
theta=2*Angles*pi/180
zeros=[]
for i,fileName in enumerate(fileNames):
    Angle=Angles[i]
    
    fileName=dirPath+fileName
    td=tofdata(fileName, threshold=0.1)
    counts.append(td.getCounts())
    if counts[-1]==0:
        zeros.append(Angle)
        
    
fig,ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, counts, '.')   

    
    
 

# td=tofdata()


