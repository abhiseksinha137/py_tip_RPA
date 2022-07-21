#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 00:29:14 2022

@author: abhisek
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

def func4(theta,A,B,C,phi):
    x=np.cos(theta-phi)
    return A+B*1/2* (3*x**2-1) + C*(1/8) * (35*x**4 - 30*x**2 +3)

def func2(theta,A,B,phi):
    x=np.cos(theta-phi)
    return A+B*1/2* (3*x**2-1)

def fitLegendre4(theta, y):
    popt, pcov = curve_fit(func4, theta, y)
    fy=func4(theta, popt[0], popt[1], popt[2], popt[3])   
    return fy, popt[0], popt[1], popt[2], popt[3]

def fitLegendre2(theta, y):
    popt, pcov = curve_fit(func2, theta, y)
    fy=func2(theta, popt[0], popt[1], popt[2])   
    return fy, popt[0], popt[1], popt[2]

if __name__=='__main__':
    phi=np.pi/4
    theta=np.linspace(0,2*np.pi,100)
    y=func4(theta,1,1,2,phi)
    
    ## fit
    fy,A,B,C,phi=fitLegendre4(theta, y)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta,y,'*')
    ax.plot(theta, fy, '--')
