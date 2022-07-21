# -*- coding: utf-8 -*-
"""
Created on Mon May 30 14:52:19 2022

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
plt.close('all')
pi=np.pi
colList=['k', 'r', 'm', 'c', 'g','deeppink', 'yellow', 'k', 'r', 'm', 'c', 'g','k', 'r', 'm', 'c', 'g']

basePath='E:/dataAnalysis/tip RPA/20220612/G/AngularDist/'
try:
    os.mkdir(basePath+'images')
except:
    pass
        

dirSettings=pd.read_csv(basePath+'dirSettings.csv')
dirSettings=dirSettings.sort_values(by=['Run', 'Power', 'Voltage'])

fileNameList=dirSettings['FileName'].values
runList=dirSettings['Run'].values
powerList=dirSettings['Power'].values
polList=dirSettings['Pol'].values
volList=dirSettings['Voltage'].values

mentionRun=True
mentionPower=False
mentionPol=False
mentionVoltage=False

figNum=1;
j=1
# plt.figure(0)
for i, fileName in enumerate(fileNameList):
    if fileName=='images':
        continue
    
    run=runList[i]
    power=powerList[i]
    pol=polList[i]
    voltage=volList[i]
    
    settingsCounts=pd.read_csv(basePath+fileName+'/settingsCounts.csv')
    Angle=2*settingsCounts['Angle'].values
    Counts=settingsCounts['Counts'].values
    
    theta=Angle*pi/180
    fy,A,B,C,phi=fitLegendre.fitLegendre4(theta,Counts)
    
    min=np.min(fy)
    max=np.max(fy)
    contrast=(max-min)/(max+min)
    contrastStr='%2.2f'%contrast
    
    plt.figure(i+1)
    # fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    plt.plot(theta*180/pi, Counts, '.', color= colList[i], alpha=0.5)
    plt.plot(theta*180/pi, fy, '--', color=colList[i],linewidth=2)
    plt.xlabel('Angle')
    plt.ylabel('Counts')
    
    #create the plotname
    plotName=''
    if mentionRun:
        plotName='Run '+ str(run)
    if mentionPower:
        plotName=plotName+' Power '+ str(power) + 'mW'
    if mentionPol:
        plotName=plotName
    if mentionVoltage:
        plotName=plotName+ ' Voltage '+ str(voltage)+'V'
    
    #plotName='Run '+ str(run)+ ' Power '+ str(power) + 'mW' + ' Voltage '+ str(voltage)+'V'
    
    plt.title(plotName+ ' contrast = ' + contrastStr)

    plt.savefig(basePath+'images/'+plotName+'.png')
    
    # print(colList[i])
    print(fileName, str(run), str(power), str(voltage), colList[i])
    
    
    plt.figure(100)
    plt.plot(theta*180/pi, fy/np.max(fy), '--', color=colList[i],linewidth=3, label=plotName)
    
    ## Get the polar plot
    plt.figure(i+20)
    plt.axes(projection = 'polar')
    plt.yticks(color='w')
    plt.polar(theta, Counts, '.', color=colList[i], alpha=0.5 )
    plt.polar(theta, fy, '--', color=colList[i] )
    plt.title(plotName)
    plt.savefig(basePath+'images/'+plotName+' Polar.png',  transparent=True)
    
    
    ## Write a csv file of the fits
    tofFileName=settingsCounts['FileName']
    
    writeData={'Angle':Angle/2, 'FileName':tofFileName, 'Counts':Counts, 'theta':theta, 'fit':fy }
    dfFit=pd.DataFrame(writeData)
    
    # dfFit=pd.DataFrame([Angle/2, tofFileName, Counts, theta, fy], 
                       # columns=['Angle','FileName', 'Counts', 'theta', 'fit'])
    dfFit.to_csv(basePath+fileName+'/settingsCountsFit'+plotName+'.csv',index=False)
    dfFit.to_csv(basePath+fileName+'/settingsCountsFit.csv',index=False)
    
plt.figure(100)
plt.legend(framealpha=0.1)
plt.savefig(basePath+'images/'+'figComp.png')
    
    
    
    
    
    # if i>0 :
    #     if run!=runList[i-1]:
    #         plt.figure(figNum)
    #         figNum=figNum+1
    #         j=1
        
    # plt.subplot(1,3,j)
    # # fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    # plt.plot(theta,Counts)
    # plt.plot(theta,fy)
    # j=j+1