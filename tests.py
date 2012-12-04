import unittest
from roman import *

class RomanNumeralTest(unittest.TestCase):

	def test_prep_numeral(self):
		input_num = "IV"
		expected = ["I", "I", "I", "I"]

		result = prep_numeral(input_num)

		self.assertEqual(result, expected)

		input_num = "XC"
		expected = ["X", "X", "X", "X", "L"]

		result = prep_numeral(input_num)

		self.assertEqual(result, expected)

	def test_sort_numeral(self):
		input_num = "X", "X", "L"
		expected = list("LXX")

		result = sort_numeral(input_num)

		self.assertEqual(result, expected)

	def test_compress_numeral(self):
		input_num = list("IIIIIIII")
		expected = "VIII"

		result = compress_numeral(input_num)

		self.assertEqual(result, expected)

	# def test_20_50(self):
	# 	input_num1 = "XX"
	# 	input_num2 = "L"
	# 	expected = "LXX"

	# 	result = add_numerals(input_num1, input_num2)

	# 	self.assertEqual(result, expected)

	def test_26_200(self):
		input_num1 = "XXVI"
		input_num2 = "CC"
		expected = "CCXXVI"

		result = add_numerals(input_num1, input_num2)

		self.assertEqual(result, expected)
