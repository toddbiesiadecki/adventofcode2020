# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 06:59:39 2020

@author: tbiesiad
"""


def readFile(filename):
    with open(filename) as f:
        groups = f.read().split('\n\n')
    return groups

def groupCount(group):
    letterFound = {}
    for i in range(0, 26):
        letterFound[chr(ord('a')+i)] = False
    
    members = group.split('\n')
    for member in members:
        for char in member:
            letterFound[char]=True
    numFound = 0
    for letter, isFound in letterFound.items():
        if(isFound):
            numFound+=1
    return numFound

def groupCount2(group):
    members = group.split('\n')
    letterFound = {}
    for i in range(0, 26):
        letterFound[chr(ord('a')+i)] = [False for i in range(len(members))]
    
    members = group.split('\n')
    for i in range(len(members)):
        for char in members[i]:
            letterFound[char][i]=True
    numFound = 0
    for letter, isFound in letterFound.items():
        if(all(isFound)):
            numFound+=1
    return numFound

groups = readFile('inputs/day6input.txt')
count = 0
for group in groups:
    count += groupCount2(group)

print(count)