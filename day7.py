# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 06:59:09 2020

@author: tbiesiad
"""


def parseRule(rule):
    str1 = rule.split(' contain ')
    containing = str1[0][0:len(str1[0])-5]
    dct = {}
    if(str1[1].find('no other bags')==-1):
        contained = str1[1].split(', ')
        for bags in contained:
            firstSpace = bags.find(' ')
            quantity = int(bags[0:firstSpace])
            bags = bags[firstSpace+1:]
            lastSpace = bags.rfind(' ')
            color = bags[0:lastSpace]
            dct[color] = quantity
    return containing, dct
    
def readContainedBy(filename):
    containedBy = {}
    with open(filename) as f:
        for line in f:
            (containing, dct) = parseRule(line)
            for color in dct:
                print(color)
                if color not in containedBy:
                    containedBy[color] = []
                containedBy[color] += [containing]
    return containedBy

def readContains(filename):
    contains = {}
    with open(filename) as f:
        for line in f:
            (containing, dct) = parseRule(line)
            contains[containing] = dct
    return contains
            

        
def traverseGraph(containedBy, color):
    currentNodes = [color]
    nodesContainingInputColor = []
    while(currentNodes):
        nextNodes = []
        for node in currentNodes:
            if node in containedBy.keys():
                nextNodes += containedBy[node]
        
        for node in nextNodes:
            if node not in nodesContainingInputColor:
                nodesContainingInputColor += [node]
        currentNodes = nextNodes
    return(len(nodesContainingInputColor))


def traverseGraph2(contains, color):
    bagsAtThisLevel = [color]
    bagsContained = 0
    while bagsAtThisLevel:
        bagsAtNextLevel = []
        for bag in bagsAtThisLevel:
            thisNodeContains = contains[bag]
            for (color, num) in thisNodeContains.items():
                bagsAtNextLevel += [color]*num
        bagsContained += len(bagsAtNextLevel)
        bagsAtThisLevel = bagsAtNextLevel
    return bagsContained
                
                
            
    
    
contains = readContains('Inputs/day7input.txt')
count = traverseGraph2(contains, 'shiny gold')
print(count)
       

                              