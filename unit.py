import unittest
from main import *


class UnitTests(unittest.TestCase):

  def testAddition(self):
    self.assertEqual(addition(2, 3), 5)

  def testSubtraction(self):
    self.assertEqual(subtraction(3, 5), -2)

  def testMultiplication(self):
    self.assertEqual(multiplication(4, 2),8)

  def testDivision(self):
    self.assertEqual(division(12, 3), 4)
