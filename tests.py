import unittest

class RomanNumeralTest(unittest.TestCase):

	def test_prep_numeral():
		input_num = "IV"
		expected = "IIII"

		result = prep_numeral(input_num)

		self.assertEqual(result, expected)

	def test_sort_numeral():
		input_num = "XXL"
		expected = "LXX"

		result = sort_numeral(input_num)

		self.assertEqual(result, expected)

	def test_compress_numeral():
		input_num = "IIIIIIII"
		expected = "VIII"

		result = compress_numeral(input_num)

		self.assertEqual(result,expected)

	def test_20_50():
		twenty = "XX"
