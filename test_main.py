import unittest
from unittest.mock import patch
from io import StringIO
from converter_factory import ConverterFactory
from history_handler import HistoryHandler

class TestConverterApp(unittest.TestCase):
    def setUp(self):
        self.converter_factory = ConverterFactory()
        self.history_handler = HistoryHandler('test_conversion_history.txt')

    @patch('builtins.input', side_effect=['1', 'IX', '3'])
    def test_roman_to_decimal_conversion(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.converter_factory.get_converter = lambda: self.converter_factory.get_converter()  # Mocking the converter
            self.history_handler.write_history = lambda x: None  # Mocking write_history method
            exec(open('main.py').read())
            self.assertIn("Conversion result: 9", fake_out.getvalue())

    @patch('builtins.input', side_effect=['2', '9', '3'])
    def test_decimal_to_roman_conversion(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.converter_factory.get_converter = lambda: self.converter_factory.get_converter()  # Mocking the converter
            self.history_handler.write_history = lambda x: None  # Mocking write_history method
            exec(open('main.py').read())
            self.assertIn("Conversion result: IX", fake_out.getvalue())

    @patch('builtins.input', side_effect=['4', '1', '2', '3'])
    def test_invalid_choice(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            exec(open('main.py').read())
            self.assertIn("Invalid choice. Please enter either '1', '2', or '3'.", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
