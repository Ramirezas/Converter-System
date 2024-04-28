from converter_factory import ConverterFactory
from history_handler import HistoryHandler

if __name__ == "__main__":
    converter_factory = ConverterFactory()
    history_handler = HistoryHandler('conversion_history.txt')

    while True:
        print("Choose which type of number you want to convert:")
        print("1. Roman")
        print("2. Decimal")
        print("3. Show conversion history")
        choice = input("Enter the number corresponding to your choice: ")

        if choice == '3':
            history_handler.print_history()
            break

        if choice not in ['1', '2']:
            print("Invalid choice. Please enter either '1', '2', or '3'.")
            continue

        converter = converter_factory.get_converter()

        if choice == '1':
            roman_numeral = input("Enter the Roman numeral: ")
            try:
                result = converter.roman_to_decimal(roman_numeral.upper())
                print(f"Conversion result: {result}")
                history_handler.write_history(f"Roman to Decimal: {roman_numeral} -> {result}")
                break
            except ValueError as e:
                print(str(e))
                continue
        else:
            decimal_number = input("Enter the decimal number: ")
            try:
                result = converter.decimal_to_roman(int(decimal_number))
                print(f"Conversion result: {result}")
                history_handler.write_history(f"Decimal to Roman: {decimal_number} -> {result}")
                break
            except ValueError:
                print("Invalid decimal number")
                continue