#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 02:36:05 2022

@author: abhisek
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import utility
import fitLegendre
import math

basePath=r'E:\dataAnalysis\tip RPA\new\20220524\LGm\AngularDist/'
dirList=glob(basePath+'*/')

## Sort dirList according to run number
name=[]
for i, dirName in enumerate(dirList):
    name.append([utility.getRunNum(dirName).replace('run', ''), dirName])
df=pd.DataFrame(name, columns=['run', 'name'])
df=df.sort_values(by=['run'],ascending=False)
dirList=df.name


colList=['k', 'r', 'm']
phiList=[]

pi=np.pi

# dataPath='/home/abhisek/dataAnalysis/tip RPA/new/20220524/G/AngularDist/20220524_G_run3_8mW/'
for i, dirName in enumerate(dirList):
    
    fileName=dirName+'settingsCounts.csv'
    
    data=pd.read_csv(fileName).values
    
    theta=2*(data[:,0]-15)*np.pi/180.0
    theta=theta.astype('float')
    counts=data[:,2]
    counts=counts.astype('float')
    
    # theta=theta[0:46]
    # counts=counts[0:46]
    
    # fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    # ax.plot(theta, counts)
    
    
    ### Fitting
    from numpy.polynomial import Legendre as L
    x=np.cos(theta)
    y=counts
    # coeffs = np.polynomial.legendre.legfit(x, y, [0,2])
    # fy=np.polynomial.legendre.legval(x, coeffs)
    
    
    # P0=coeffs[0]
    # P2=coeffs[2]
    fy,A,B,phi=fitLegendre.fitLegendre2(theta,y)
    
    norm=np.max(fy)
    # plt.plot(theta,counts, '*'+colList[i])
    leg=utility.getRunNum(dirName)
    plt.figure(0)
    # plt.plot(theta, counts/norm, '.'+colList[i], label=leg)
    plt.plot(theta*180/pi,fy/norm, '--'+colList[i], label=leg,linewidth=3)
    plt.legend()
    plt.xlabel('Angle (degree)')
    plt.ylabel('Counts (arb. units)')
    
    phi=phi%(2*math.pi) * 180/np.pi
    print(leg +' ' +str(phi))
    
    plt.figure(1)
    plt.subplot(1,3,i+1)
    # fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    plt.plot(theta*180/pi,y,'.'+colList[i],alpha=0.35)
    plt.plot(theta*180/pi, fy, '--'+colList[i])
    plt.title(leg)
    
    phiList.append(phi)
    plt.xlabel('Angle (degree)')
    plt.ylabel('Counts (arb. units)')
    
print(np.diff(phiList))
# plt.ylim([1.3e7, 1.3e9])

