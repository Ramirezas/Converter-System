import unittest
from converter_factory import ConverterFactory
from roman_decimal_converter import RomanDecimalConverter

class TestConverterFactory(unittest.TestCase):
    def test_get_converter(self):
        factory = ConverterFactory()
        converter = factory.get_converter()
        self.assertIsInstance(converter, RomanDecimalConverter)

if __name__ == "__main__":
    unittest.main()