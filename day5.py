# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 07:59:38 2020

@author: tbiesiad
"""


def SeatID(boardingPass):
    row = boardingPass[0:7]
    col = boardingPass[7:]

    rowBin = row.replace('F','0').replace('B', '1')
    colBin = col.replace('L', '0').replace('R', '1')

    rowNum = int(rowBin, 2)
    colNum = int(colBin, 2)

    return rowNum * 8 + colNum

def day5part1(filename):
    maxID = 0
    with open(filename) as f:
        for line in f:
            currentID = SeatID(line)
            if(currentID>maxID):
                maxID = currentID
    print(maxID)
    
def day5part2(filename):
    seatIDs = []
    missingSeat = -1
    with open(filename) as f:
        for line in f:
            seatIDs += [SeatID(line)]
            
    seatIDs.sort()
    for i in range(1,len(seatIDs)):
        if(seatIDs[i]==seatIDs[i-1]+2):
            missingSeat = seatIDs[i]-1
            break
    print(missingSeat)
            

day5part2('inputs/day5input.txt')