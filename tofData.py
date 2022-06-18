# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 23:48:14 2022

@author: abhisek
"""

## This class imports the tof Data and does priliminary analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class tofdata:
    # The class is initialized with the path to the csv file
    def __init__(self, dataPathVal, level_empty_data=True):
        self.dataPath=dataPathVal
        self.readData()
        self.invertSignal(level_empty_data)
        
    def readData(self):
        self.data=pd.read_csv(self.dataPath)
        self.data=self.data.drop(labels=0)
        self.tof=self.data['Time'].values.astype(float)
        self.signal=self.data['Signal'].values.astype(float)
        self.trigger=self.data['Trigger'].values.astype(float)
        
        
        
    def getData(self):
        return self.data.values.astype(float)
    
    def getTOF(self):
        return self.tof
    
    def getSIGNAL(self):
        return self.signal
    
    def getPD(self):
        return self.trigger
    
    # def getCounts(self):
    #     return self.counts
    
    def invertSignal(self, level_empty_data): # level_empty_data: weather you want to level an empty signal
        ## first get the index of the min
        t=self.getTOF()
        sig=self.getSIGNAL()
        minIdx=np.argmax(sig)

        pad=1000
        if minIdx<pad or minIdx>len(t)-pad:
            if level_empty_data:   # if you want to level an empty signal
                self.signal=np.zeros(np.shape(self.getSIGNAL()))
            else:
                offset=np.mean(sig[0:300])
                self.signal=self.getSIGNAL()-offset
                self.signal=-self.getSIGNAL()
        else:
            offset=np.mean(sig[minIdx-pad:minIdx-pad+300])
            self.signal=self.getSIGNAL()-offset
            self.signal=-self.getSIGNAL()
            
            

    def calculateCounts(self, threshold):
        sig=self.getSIGNAL()
        t=self.getTOF()
        maxIdx=np.argmax(sig)
        maxVal=np.max(sig)
        

        plt.plot(t[maxIdx], sig[maxIdx], 'o')
        sigLeft=sig[0:maxIdx] ; tLeft=t[0:maxIdx]
        sigRight=sig[maxIdx+1:len(sig)];  tRight=t[maxIdx+1:len(sig)]
        plt.show()
        
        plt.figure()
        plt.plot(tLeft,sigLeft)
        plt.plot(tRight,sigRight)
        
        
        plt.show()
        


     
    def plotSignal(self):
        plt.figure()
        plt.plot(self.getTOF(), self.getSIGNAL())
        plt.xlabel('TOF (sec)')
        plt.ylabel('Signal (Volts)')
        # plt.show()
    
if __name__ == '__main__':
    plt.close('all')
    dataPath='E:/dataAnalysis/tip RPA/20220519/G/TipHorizontalScan/20220519_G_run1/20220519_G_run1_0.00E+0V_0.00E+0deg.txt'
    # dataPath='zeroData.txt'
    td=tofdata(dataPath, level_empty_data=False)
    t=td.getTOF()
    s=td.getSIGNAL()
    # print(td.getCounts())
    # plt.plot(s)

    

    td.plotSignal()
    td.calculateCounts(0.1)
    # td.plotSignal()
    
    

        
    
    
        
        
