# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 07:52:19 2020

@author: tbiesiad
"""


def day10(filename):
    arr = []
    with open(filename) as f:
        for line in f:
            arr += [int(line)]
    arr.sort()
    diff1count = 0
    diff3count = 0
    for i in range(0, len(arr)):
        if i==0:
            delta = arr[i]-0
        else:
            delta = arr[i]-arr[i-1]
            
        if delta==1:
            diff1count+=1
        elif delta==3:
            diff3count+=1
    diff3count+=1
    
    print(diff1count)
    print(diff3count)
    print(diff1count*diff3count)
    

def pathsFromStart(arr):
    arrLen = len(arr)
    pathsFromHere = [0]*arrLen
    for i in range(arrLen-1, -1, -1):
        if i==arrLen-1:
            pathsFromHere[i]=1
        else:
            j = i + 1
            numPaths = 0
            while((j<arrLen) and (arr[j]<=arr[i]+3)):
                numPaths += pathsFromHere[j]
                j+=1
            pathsFromHere[i] = numPaths
    return pathsFromHere[0]
    
    
def day10part2(filename):
    arr = []
    with open(filename) as f:
        for line in f:
            arr += [int(line)]
    arr.sort()
    arr = [0]+ arr
    print(arr)
    print(pathsFromStart(arr))
        
    
    
day10part2('inputs/day10input.txt')