# This program will plot the counts for different values of threshold in a single directory for Angular 
# Data


from tofData import tofdata 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

pi=np.pi
plt.close('all')

dirPath='E:/dataAnalysis/tip RPA/new/20220520/G/TipVerticalScan/20220519_G_run1_5mW_10V/'
imageSavePath=dirPath+'tofImages/'

try:
    os.mkdir(imageSavePath)
except:
    pass
    
settings=pd.read_csv(dirPath+'settings.csv')
settings=settings.sort_values(by='Angle')
fileNames=settings['FileName'].values
Angles=settings['Angle'].values

counts=[]
theta=2*Angles*pi/180
zeros=[]


threshold=0.05
for i,fileName in enumerate(fileNames):
    Angle=Angles[i]
    
    fileName=dirPath+fileName
    td=tofdata(fileName, threshold=threshold)
    counts.append(td.getCounts())
    if counts[-1]==0:
        zeros.append(Angle)
    
    figt, axt = td.plotSignal()
    plt.figure(figt)
    plt.xlim(0.75e-6, 1.25e-6)
    #####  Save  ######
    figt.savefig(imageSavePath+ str(Angle)+'.png')   
    plt.close(figt)
    print(i)
    
fig,ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, counts, '.')  

# Legendre Fit 

    
    
 

# td=tofdata()


