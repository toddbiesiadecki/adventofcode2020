# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 07:59:57 2020

@author: tbiesiad
"""


import day5
import unittest

class TestDay5(unittest.TestCase):
    def testSeatId(self):
        self.assertEqual(day5.SeatID('BFFFBBFRRR'),567)
        self.assertEqual(day5.SeatID('FFFBBBFRRR'),119)
        self.assertEqual(day5.SeatID('BBFFBBFRLL'),820)
        

unittest.main()
