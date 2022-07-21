# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 03:54:38 2022

@author: abhisek
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import utility
import fitLegendre
import math
import os
import re

def replaceChars(text):
    chars = r"{}[]',:"
    for c in chars:
        text = text.replace(c, ' ')
    text=re.sub('\\s+', ' ', text)
    return text

plt.close('all')

pi=np.pi
colList=['k', 'r', 'm', 'c', 'g', 'k', 'r', 'm', 'c', 'g','k', 'r', 'm', 'c', 'g']

basePath='E:/dataAnalysis/tip RPA/new/20220520/LG/TipVerticalScan/'
plotSelection={'Run': [1,2,3], 'Power':[10], 'Voltage':[0]}
figureSavePath=basePath+'images/'+ replaceChars(str(plotSelection)).strip()
try:
    os.mkdir(figureSavePath) 
except:
    pass
dirSettings=pd.read_csv(basePath+'dirSettings.csv')
dirSettings=dirSettings.sort_values(by=['Run', 'Power', 'Voltage'])

fileNameList=dirSettings['FileName'].values
runList=dirSettings['Run'].values
powerList=dirSettings['Power'].values
polList=dirSettings['Pol'].values
volList=dirSettings['Voltage'].values

plotNum=0;
for i, fileName in enumerate(fileNameList):
    run=runList[i]
    power=powerList[i]
    pol=polList[i]
    voltage=volList[i]
    
    if not (run in plotSelection['Run']):
        continue
    if not (power in plotSelection['Power']):
        continue
    if not (voltage in plotSelection['Voltage']):
        continue
    
    
    
    
    settingsCounts=pd.read_csv(basePath+fileName+'/settingsCountsFit.csv')
    theta=settingsCounts['theta'].values
    Counts=settingsCounts['Counts'].values
    fy=settingsCounts['fit'].values
    
    plotName='Run '+ str(run)+ ' Power '+ str(power) + 'mW' + ' Voltage '+ str(voltage)+'V'
    
    # plot Individual
    plt.figure(plotNum)
    plt.plot(theta*180/pi, Counts, '.'+colList[plotNum], alpha=0.5)
    plt.plot(theta*180/pi, fy, '--'+colList[plotNum], label=plotName)
    plt.title(plotName)
    
    ## Save
    plt.savefig(figureSavePath+'/'+plotName+'.png')
    
    
    plt.figure(plotNum+20)
    plt.axes(projection = 'polar')
    plt.yticks(color='w')
    plt.polar(theta, Counts, '.'+colList[plotNum], alpha=0.5)
    plt.polar(theta, fy, '--'+colList[plotNum], label=plotName)
    plt.title(plotName)
    
    ## Save
    
    plt.savefig(figureSavePath+'/'+plotName+' Polar.png', transparent=True)
    
    
    
    # Plot together
    plt.figure(100)
    plt.plot(theta*180/pi, fy/np.max(fy), '-'+colList[plotNum], label=plotName)
    
    print(fileName, str(run), str(power), str(voltage))
    plotNum=plotNum+1
    
    
plt.figure(100)
plt.legend(framealpha=0.1)

# figManager = plt.get_current_fig_manager()
# figManager.window.showMaximized()

## Save
plt.savefig(figureSavePath+'/figComp.png', dpi=600)
    
    

















