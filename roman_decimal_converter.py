from converter import Converter

class RomanDecimalConverter(Converter):
    def __init__(self):
        super().__init__()
        self.roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.decimal_to_roman_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

    def roman_to_decimal(self, roman_numeral):
        decimal_number = 0
        prev_value = 0
        
        for numeral in reversed(roman_numeral):
            value = self.roman_numerals.get(numeral, None)
            if value is None:
                raise ValueError(f"{numeral} is not a valid Roman numeral")
            if value < prev_value:
                decimal_number -= value
            else:
                decimal_number += value
            prev_value = value
        
        return decimal_number
    
    def decimal_to_roman(self, decimal_number):
        roman_numeral = ''
        
        for value, numeral in sorted(self.decimal_to_roman_map.items(), reverse=True):
            while decimal_number >= value:
                roman_numeral += numeral
                decimal_number -= value
        
        return roman_numeral

    def convert(self, value, from_type, to_type):
        if from_type == 'roman' and to_type == 'decimal':
            return self.roman_to_decimal(value)
        elif from_type == 'decimal' and to_type == 'roman':
            return self.decimal_to_roman(int(value))
        else:
            raise ValueError("Invalid conversion type")