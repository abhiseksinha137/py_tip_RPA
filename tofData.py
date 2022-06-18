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
    def __init__(self, dataPathVal):
        self.dataPath=dataPathVal
        self.readData()
        self.calculateCounts()
        
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
    
    def getCounts(self):
        return self.counts
    
    def calculateCounts(self):
        ## first get the index of the min
        t=self.getTOF()
        sig=self.getSIGNAL()
        minIdx=np.argmax(sig)
        
        pad=1000
        if minIdx<pad or minIdx>len(t)-pad:
            self.counts=0
        else:
            offset=np.mean(sig[minIdx-pad:minIdx-pad+300])
            print(offset)
            self.signal=self.getSIGNAL()-offset
            self.signal=-self.getSIGNAL()
            
            self.counts=np.trapz(self.getSIGNAL(), self.getTOF())/1.6e-19
            
            
        
        
    
    def plotSignal(self):
        plt.figure()
        plt.plot(self.getTOF(), self.getSIGNAL())
        plt.xlabel('TOF (sec)')
        plt.ylabel('Signal (Volts)')
    
if __name__ == '__main__':
    plt.close('all')
    td=tofdata('E:/dataAnalysis/tip RPA/20220519/G/TipHorizontalScan/20220519_G_run1/20220519_G_run1_0.00E+0V_0.00E+0deg.txt')
    t=td.getTOF()
    s=td.getSIGNAL()
    print(td.getCounts())
    plt.plot(s)
    
    # plt.show()
    # td.plotSignal()
    # td.plotSignal()
    
    

        
    
    
        
        