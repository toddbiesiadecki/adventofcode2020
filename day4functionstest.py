# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:45:08 2020

@author: tbiesiad
"""


import day4functions
import unittest

class TestHelperFunctions(unittest.TestCase):
    def test_isNumeric(self):
        self.assertTrue(day4functions.isNumeric('0123456789'))
        self.assertFalse(day4functions.isNumeric('abcdefg'))
        self.assertTrue(day4functions.isNumeric('2020'))
        
    def test_isHexadecimal(self):
        self.assertTrue(day4functions.isHexadecimal('0123456789abcdef'))
        self.assertFalse(day4functions.isHexadecimal('0123456789abcdefg'))
        self.assertFalse(day4functions.isHexadecimal('0123456789ABCDEF'))
        
    def test_isValidYear(self):
        self.assertTrue(day4functions.isValidYear('2020', 2019, 2021))
        self.assertTrue(day4functions.isValidYear('2020', 2020, 2020))
        self.assertFalse(day4functions.isValidYear('1900', 2000, 2020))
        self.assertFalse(day4functions.isValidYear('0002000', 1999, 2001))
        self.assertTrue(day4functions.isValidYear('0050', 49, 51))
        
class TestFieldValidityChecks(unittest.TestCase):
    def test_byr(self):
        self.assertTrue(day4functions.byrValid('1999'))
        self.assertFalse(day4functions.byrValid('1234'))
        self.assertFalse(day4functions.byrValid('abcd'))
        self.assertFalse(day4functions.byrValid('0002000'))
    def test_iyr(self):
        self.assertTrue(day4functions.iyrValid('2015'))
        self.assertFalse(day4functions.iyrValid('1234'))
        self.assertFalse(day4functions.iyrValid('abcd'))
        self.assertFalse(day4functions.iyrValid('0002015'))
    def test_eyr(self):
        self.assertTrue(day4functions.eyrValid('2025'))
        self.assertFalse(day4functions.eyrValid('1234'))
        self.assertFalse(day4functions.eyrValid('abcd'))
        self.assertFalse(day4functions.eyrValid('0002025'))
    def test_hgt(self):
        self.assertTrue(day4functions.hgtValid('65in'))
        self.assertTrue(day4functions.hgtValid('160cm'))
        self.assertFalse(day4functions.hgtValid('30in'))
        self.assertFalse(day4functions.hgtValid('200in'))
        self.assertFalse(day4functions.hgtValid('30cm'))
        self.assertFalse(day4functions.hgtValid('200cm'))
        self.assertFalse(day4functions.hgtValid('200cx'))    
        self.assertFalse(day4functions.hgtValid('abcd'))
    def test_hcl(self):
        self.assertTrue(day4functions.hclValid('#1a2b3c'))
        self.assertFalse(day4functions.hclValid('%1a2b3c'))
        self.assertFalse(day4functions.hclValid('#1a2b3c4'))
        self.assertFalse(day4functions.hclValid('#1A2B3C'))
    def test_ecl(self):
        self.assertTrue(day4functions.eclValid('amb'))
        self.assertTrue(day4functions.eclValid('blu'))
        self.assertTrue(day4functions.eclValid('brn'))
        self.assertTrue(day4functions.eclValid('gry'))
        self.assertTrue(day4functions.eclValid('grn'))
        self.assertTrue(day4functions.eclValid('hzl'))
        self.assertTrue(day4functions.eclValid('oth'))
        self.assertFalse(day4functions.eclValid('xyz'))
    def test_pid(self):
        self.assertTrue(day4functions.pidValid('012345678'))
        self.assertFalse(day4functions.pidValid('0123456789'))
        self.assertFalse(day4functions.pidValid('01234567a'))
        
unittest.main()