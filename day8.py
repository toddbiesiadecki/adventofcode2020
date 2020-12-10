# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 05:09:18 2020

@author: tbiesiad
"""
class instruction:
    def __init__(self):
        self.opcode = ''
        self.operand = -999
        self.index = -999
        self.visited = False
        self.acc = -999
        self.inLoo
        
def parseInstruction(strIn):
    instr = instruction()
    x = strIn.split(' ')
    instr.opcode = x[0]
    instr.operand = int(x[1])
    instr.visited = False
    instr.acc = -999
    instr.index =-999
    return instr

def readProgram(filename):
    program = []
    with open(filename) as f:
        for line in f:
            program += [parseInstruction(line)]
    return program


def hasInfiniteLoop(pgm):
    ip = 0
    acc = 0
    finalAcc = 0
    for i in range(0, len(pgm)):
        pgm[i].visited = False
    
    while(ip<len(pgm)):
        pgm[ip].acc = acc
        if pgm[ip].visited == True:
            finalAcc = pgm[ip].acc
            return (True, -999)
            break
        else:
            pgm[ip].visited = True
        
        # execute instruction
        if pgm[ip].opcode == 'acc':
            acc += pgm[ip].operand
            ip+=1
        elif pgm[ip].opcode=='jmp':
            ip+=pgm[ip].operand
        elif pgm[ip].opcode == 'nop':
            ip+=1
    return (False, acc)


def part2InLinearTime(pgm):
    # attempt at algorithm for part 2 that runs in O(n)
    # algorithm is as follows:
    #   - traverse array once and note whether each instruction belongs to a loop
    #   - traverse array again, find all nop or jmp, indicate whether changing them puts you on an instruction that's part of a loop
    #   - fix broken instruction, traverse loop again and calculate acc
    
    i = range(0, len(pgm))
    onLoopPath = [False]*range(0, len(pgm))
    while i:
        thisLevelIndices = []
        thisLevelValues = []
        idx = i[0]
        foundLoop = False
        while (not foundLoop) and (idx<len(pgm)): # this is wrong
            if pgm[idx].visited==True:
                foundLoop = True
            else:
                pgm[idx].visited = True
                thisLevelIndices += [idx]
                thisLevelValues += i[idx]
                if pgm[idx].opcode=='jmp':
                    idx += pgm[idx].operand
                else:
                    idx+=1
        if(foundLoop):
            for num in thisLevelValues:
                onLoop[num]=True
        for x in range(len(thisLevelIndices), 0, -1):
            del[i[thisLevelIndices[x]]]
        
    
pgm = readProgram('Inputs/day8input.txt')
for i in range(0, len(pgm)):
    # change instruction
    oldOpcode = pgm[i].opcode
    if(pgm[i].opcode=='jmp'):
        pgm[i].opcode = 'nop'
    elif(pgm[i].opcode=='nop'):
        pgm[i].opcode = 'jmp'
    else:
        continue
    (infiniteLoop, finalAcc) = hasInfiniteLoop(pgm)
    pgm[i].opcode = oldOpcode
    if(not infiniteLoop):
        print(finalAcc)
        break
    
        