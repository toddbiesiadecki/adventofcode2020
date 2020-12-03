# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 07:10:02 2020

@author: tbiesiad
"""

def ReadMap(filename):
    map = []
    with open(filename) as f:
        for line in f:
            map = map + [list(line.rstrip())]
    return map

def CountTrees(map, rowInc, colInc):
    rowCount = len(map)
    colCount = len(map[0])
    row = 0
    col = 0
    treeCount = 0
    while(row<rowCount-1):
        row+=rowInc
        col+=colInc
        if(map[row][col % colCount]=='#'):
            treeCount+=1
    return treeCount

map = ReadMap('inputs/day3input.txt')


print(CountTrees(map,1,1)*CountTrees(map,1,3)*CountTrees(map,1,5)*CountTrees(map,1,7)*CountTrees(map,2,1))


