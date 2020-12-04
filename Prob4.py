# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:06:01 2020

@author: tbiesiad
"""
requiredFields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

import day4functions

fieldValidityCheck = {
    'byr:':day4functions.byrValid,
    'iyr:':day4functions.iyrValid,
    'eyr:':day4functions.eyrValid,
    'hgt:':day4functions.hgtValid,
    'hcl:':day4functions.hclValid,
    'ecl:':day4functions.eclValid,
    'pid:':day4functions.pidValid,
    'cid:':day4functions.cidValid,}

def readInput(filename):
    with open(filename) as f:
        text = f.read()
        passportList = text.split('\n\n')
    return passportList


def areAllRequiredFieldsPresent(passportEntry):
    entryValid = True
    for field in requiredFields:
        if(passportEntry.find(field)==-1):
            entryValid = False
            break
    return entryValid

def isPassportEntryValid(passportEntry):
    if(areAllRequiredFieldsPresent(passportEntry)==False):
        return False
    passportEntry = passportEntry.replace('\n',' ')
    passportFields = passportEntry.split(' ')
    for field in passportFields:
        splitField = field.split(':')
        name = splitField[0] + ':'
        value = splitField[1]
        if(fieldValidityCheck[name](value)==False):
            return False
    return True
        


passportList = readInput("inputs/day4input.txt")
validCount = 0
for entry in passportList:
    if(isPassportEntryValid(entry)):
        validCount+=1
        
print(validCount)
        
        