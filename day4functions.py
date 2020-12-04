# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:31:24 2020

@author: tbiesiad
"""


def isValidYear(value, minYear, maxYear):
    isValid = (len(value)==4)
    isValid = isValid and isNumeric(value)
    isValid = isValid and (int(value)>=minYear) and (int(value)<=maxYear)
    return isValid

def isNumeric(string):
    for char in string:
        if((char < '0') or (char > '9')):
            return False
    return True

def isHexadecimal(string):
    for char in string:
        if((isNumeric(char)==False) and ((char <'a') or char > 'f')):
            return False
    return True
    

def byrValid(value):
    return isValidYear(value, 1920, 2002)

def iyrValid(value):
    return isValidYear(value, 2010, 2020)

def eyrValid(value):
    return isValidYear(value, 2020, 2030)

def hgtValid(value):
    unit = value[len(value)-2:]
    if((unit!='in')and(unit!='cm')):
        return False 
    num = value[0:len(value)-2]

    if(isNumeric(num)==False):
        return False
    
    if(unit=='in'):
        if((int(num)>76) or (int(num)<59)):
            return False
    elif(unit=='cm'):
        if((int(num)>193) or (int(num)<150)):
            return False
              
    return True

def hclValid(value):
    if(value[0]!='#'):
        return False
    num = value[1:]
    if(len(num)!=6):
        return False
    if isHexadecimal(num)==False:
        return False
    return True

def eclValid(value):
    validValues = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    isValid = False
    for x in validValues:
        if(value==x):
            isValid = True
            break
    return isValid

def pidValid(value):
    isValid = len(value)==9
    for char in value:
        if (char<'0') or (char > '9'):
            isValid = False
            break
    return isValid

def cidValid(value):
    return True