class RomanDecimalConverter:
    def __init__(self):
        self.roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.decimal_to_roman_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

    def roman_to_decimal(self, roman_numeral):
        decimal_number = 0
        prev_value = 0
        
        for numeral in reversed(roman_numeral):
            value = self.roman_numerals.get(numeral, 0)
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

if __name__ == "__main__":
    converter = RomanDecimalConverter()

    roman_numeral_input = input("Enter a Roman numeral: ")
    decimal_number = converter.roman_to_decimal(roman_numeral_input.upper())
    print(f"{roman_numeral_input} in decimal: {decimal_number}")

    decimal_number_input = int(input("Enter a decimal number: "))
    roman_numeral = converter.decimal_to_roman(decimal_number_input)
    print(f"{decimal_number_input} in Roman numeral: {roman_numeral}")
