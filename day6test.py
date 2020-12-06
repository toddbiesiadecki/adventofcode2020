# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 06:59:45 2020

@author: tbiesiad
"""


import day6
import unittest

class TestDay6(unittest.TestCase):
    def testGroupCount(self):
        self.assertEqual(day6.groupCount('abc'),3)
        self.assertEqual(day6.groupCount('a\nb\nc'),3)
        self.assertEqual(day6.groupCount('ab\nac'),3)
        self.assertEqual(day6.groupCount('a\na\na\n'),1)
        self.assertEqual(day6.groupCount('b'), 1)
        self.assertEqual(day6.groupCount('abcdefghijlkmnopqrstuvwxyz'), 26)
        
unittest.main()