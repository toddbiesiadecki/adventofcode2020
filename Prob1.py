# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:26:47 2020

@author: tbiesiad
"""



def prob1(numList):
    foundNum = 0
    for i in range(len(numList)):
        for j in range (i, len(numList)):
            for k in range(j, len(numList)):
                if(numList[i]+numList[j]+numList[k]==2020):
                    foundNum = 1
                    break
            if(foundNum==1):
                break
        if(foundNum==1):
            break
    print(numList[i])
    print(numList[j])
    print(numList[k])
    print(numList[i]*numList[j]*numList[k])
    
 
inputList = []
with open ('Inputs/day1input.txt') as f:
    for line in f:
        inputList = inputList + [int(line)]
        
prob1(inputList)
    
    
