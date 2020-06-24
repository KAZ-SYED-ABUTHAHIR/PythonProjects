# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:25:58 2020

@author: KAZ

This program demonstrated the overhead in using x**2 instead of simple x*x.
"""
import os
import timeit
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

NUM_REPEATS = 256

tPower = timeit.Timer('x**2',setup = 'x=1.23543')
tMult  = timeit.Timer('x*x',setup = 'x=1.23543')

lPower = tPower.repeat(NUM_REPEATS,number=1000000)
lMult  = tMult.repeat(NUM_REPEATS,number=1000000)
lTimesFaster = [lPower[i]/lMult[i] for i in range(len(lMult))]

os.mkdir('Metrics')
 
with PdfPages('Metrics/SquaringWithPower.pdf') as pdf:
    fig,(gMultPower,gTimesFaster) = plt.subplots(2,1,figsize=(7,5))
    
    gMultPower.plot(lPower,'bo-',linewidth=1)
    gMultPower.plot(lMult,'go-',linewidth=1)
    gMultPower.set(xlabel='Count',ylabel='Time Taken by x*x(sec) ',
              title='x*x')
    gMultPower.grid()
    
    gTimesFaster.plot(lTimesFaster,'b-',linewidth=1)
    gTimesFaster.set(xlabel='Count',ylabel='Ratio between times of execution',
              ylim=(0,20),title='x*x is faster than x**2 !')
    gTimesFaster.grid()
    plt.tight_layout()
    
    fig.savefig('Metrics/Squaring Times.png')
    pdf.savefig()  


print("Calulating squares by direct multiplication is",mean(lTimesFaster),
      "times faster on the average than raising to the power 2 using the"
      "operator **")