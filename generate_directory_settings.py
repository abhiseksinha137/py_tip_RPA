# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 12:24:07 2022

@author: abhisek
"""


import glob
import pandas as pd
import numpy as np
import re






def generate(dirPath):
    dirList=glob.glob(dirPath+'*/')

    fileNameList=[]
    runList=[]
    powerList=[]
    polList=[]
    voltageList=[]
    for i, dirName in enumerate(dirList):
        dirList[i]=dirName.replace('\\', '/')
        dirName=dirList[i]
        
        folderName=dirName.split('/')[-2]
        
        m=re.search('(2022)?', folderName).groups()
        if m==(None,):
            continue
        
        run=''
        power=''
        pol=''
        voltage='0'
        try:
            run = re.search('(?<=run)(.[0-9]?)(?=_?)', folderName).groups()[0]
        except:
            pass
        try:
            power = re.search('(?<=_)(.[0-9]?).?[0-9]*?(?=mW)', folderName).groups()[0]
        except:
            pass
        try:
            pol = re.search('(?<=pol_)(.*)', folderName).groups()[0]
        except:
            pass
        try:
            voltage = re.search('(?<=)([0-9]*)(?=V)', folderName).groups()[0]
        except:
            pass
        
        fileNameList.append(folderName)
        runList.append(run)
        powerList.append(power)
        polList.append(pol)
        voltageList.append(voltage)
        print(folderName, run, power, pol, voltage)
        
    writeData={'FileName':fileNameList, 'Run':runList, 'Power':powerList, 'Pol':polList,
            'Voltage':voltageList}
    df=pd.DataFrame(writeData)
    df=df.sort_values(by=['Run', 'Power', 'Voltage'])


    ## Write the data
    df.to_csv(dirPath+'dirSettings_py.csv', index=False)



if __name__ =='__main__':
    dirPath='E:/dataAnalysis/tip RPA/new/20220520/G/TipVerticalScan/'
    generate(dirPath)
