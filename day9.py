# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 06:52:09 2020

@author: tbiesiad
"""


def readInput(filename):
    arr = []
    with open(filename) as f:
        for line in f:
            arr += [int(line)]
    return arr

def part1(arr, length):
    for i in range(length, len(arr)):
        validInput = False
        for j in range(i-length, i):
            for k in range(i-length, i):
                if not (j==k):
                    if(arr[j]+arr[k]==arr[i]):
                        validInput = True
        if validInput == False:
            return arr[i]
    return -1


def part2(arr,length):
    invalidNum = part1(arr, length)
    startInd = 0
    endInd = 0
    found = False
    sum = arr[0]
    while found == False:
        if sum < invalidNum:
            endInd += 1
            sum += arr[endInd]
        elif sum > invalidNum:
            sum -= arr[startInd]
            startInd+=1
        else:
            found = True
    
    subArr = arr[startInd:endInd+1]
    return max(subArr)+min(subArr)

print(part2(readInput('inputs/day9input.txt'),25))

    
    
    
                    
            