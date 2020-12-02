# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:37:19 2020

@author: tbiesiad
"""

def isPasswordValidPart2(line):
    stringList = line.split()
    password = stringList[2]
    letter = stringList[1].split(':')[0]
    index1 = int(stringList[0].split('-')[0])
    index2 = int(stringList[0].split('-')[1])
    return ((password[index1-1]==letter) ^ (password[index2-1]==letter))

def isPasswordValid(line):
    stringList = line.split()
    password = stringList[2]
    letter = stringList[1].split(':')[0]
    minNum = int(stringList[0].split('-')[0])
    maxNum = int(stringList[0].split('-')[1])
    charCount = 0
    for char in password:
        if(letter==char):
            charCount+=1
    return ((charCount>=minNum) and (charCount<=maxNum))


validPasswordCount = 0
with open('inputs/day2input.txt') as f:
    for line in f:
        if isPasswordValidPart2(line):
            validPasswordCount+=1
            
print(validPasswordCount)
        