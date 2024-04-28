import unittest
from converter import Converter
from roman_decimal_converter import RomanDecimalConverter

class TestConverter(unittest.TestCase):
    def test_converter_abstract(self):
        with self.assertRaises(NotImplementedError):
            converter = Converter()
            converter.convert("")

class TestRomanDecimalConverter(unittest.TestCase):
    def test_roman_to_decimal(self):
        converter = RomanDecimalConverter()
        self.assertEqual(converter.roman_to_decimal("I"), 1)
        self.assertEqual(converter.roman_to_decimal("V"), 5)
        self.assertEqual(converter.roman_to_decimal("X"), 10)
        self.assertEqual(converter.roman_to_decimal("L"), 50)
        self.assertEqual(converter.roman_to_decimal("C"), 100)
        self.assertEqual(converter.roman_to_decimal("D"), 500)
        self.assertEqual(converter.roman_to_decimal("M"), 1000)

    def test_decimal_to_roman(self):
        converter = RomanDecimalConverter()
        self.assertEqual(converter.decimal_to_roman(1), "I")
        self.assertEqual(converter.decimal_to_roman(4), "IV")
        self.assertEqual(converter.decimal_to_roman(5), "V")
        self.assertEqual(converter.decimal_to_roman(9), "IX")
        self.assertEqual(converter.decimal_to_roman(10), "X")
        self.assertEqual(converter.decimal_to_roman(40), "XL")
        self.assertEqual(converter.decimal_to_roman(50), "L")
        self.assertEqual(converter.decimal_to_roman(90), "XC")
        self.assertEqual(converter.decimal_to_roman(100), "C")
        self.assertEqual(converter.decimal_to_roman(400), "CD")
        self.assertEqual(converter.decimal_to_roman(500), "D")
        self.assertEqual(converter.decimal_to_roman(900), "CM")
        self.assertEqual(converter.decimal_to_roman(1000), "M")

if __name__ == "__main__":
    unittest.main()