# Converter Application Report
## Introduction
This report covers the development of a converter application that handles conversions between Roman numerals and decimal numbers. The application also maintains a history of conversions. The primary goals were to implement object-oriented programming (OOP) principles and design patterns to ensure the application is robust, maintainable, and easy to extend.

### What is your application?
The application allows users to convert Roman numerals to decimal numbers and vice versa. It also provides a feature to display the history of conversions.

### How to run the program?
To run the program, ensure you have Python installed on your system. Then, execute the main.py file from the command line.

### How to use the program?
1. Run the program.
2. Choose the type of conversion (Roman to Decimal or Decimal to Roman).
3. Enter the number to be converted.
4. View the conversion result.
5. Optionally, view the history of conversions.

## Body/Analysis

## OOP Pillars Implementation

### Abstraction
Abstraction is implemented in the Converter class, which defines an abstract method convert. This method is overridden by subclasses to provide specific conversion logic.
```
class Converter:
    def init(self):
        pass

    def convert(self, value):
        raise NotImplementedError("Subclass must implement this method")
```

### Encapsulation
Encapsulation is demonstrated in the RomanDecimalConverter class, where the conversion logic and data are encapsulated within methods and private attributes.
```
class RomanDecimalConverter(Converter):
    def init(self):
        super().init()
        self.roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.decimal_to_roman_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
```

### Inheritance
Inheritance is used where RomanDecimalConverter inherits from the Converter class, providing specific implementations for converting between Roman and decimal numbers.
```
class RomanDecimalConverter(Converter):
    def roman_to_decimal(self, roman_numeral):
        # Conversion logic here

    def decimal_to_roman(self, decimal_number):
        # Conversion logic here
```

### Polymorphism
Polymorphism is demonstrated through the Converter interface, where the convert method can be used by any subclass to perform specific conversions.
```
def perform_conversion(converter: Converter, value):
    return converter.convert(value)
```

## Design Patterns

### Singleton Pattern
The Singleton pattern is implemented in the HistoryHandler class to ensure there is only one instance managing the conversion history.
```
class HistoryHandler:
    _instance = None

    def __new__(cls, filename):
        if not cls._instance:
            cls._instance = super(HistoryHandler, cls).__new__(cls)
            cls._instance.init(filename)
        return cls._instance

    def init(self, filename):
        self.filename = filename
        self.history = self.read_history()
```

### Factory Method Pattern
The Factory Method pattern is used in the ConverterFactory class to create instances of RomanDecimalConverter.
```
class ConverterFactory:
    def get_converter(self):
        return RomanDecimalConverter()
```

## Reading from and Writing to Files

The application reads from and writes to a text file to maintain a history of conversions. This is handled by the HistoryHandler class.
```
def read_history(self):
    try:
        with open(self.filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_history(self, conversion):
    with open(self.filename, 'a') as file:
        file.write(conversion + '\n')
```

## Results and Summary

### Results
Successful Implementation: The program effectively implements the specified design patterns and object-oriented programming principles, including encapsulation, abstraction, inheritance, and polymorphism.
Functional Conversion: Users can convert between Roman numerals and decimal numbers seamlessly, ensuring accurate and reliable conversions.
Conversion History: The program maintains a conversion history, allowing users to track their previous conversions and view them whenever needed.
Flexible Design: The use of design patterns such as the Factory Method Pattern ensures flexibility in creating converter instances, while the abstraction provided by the Converter base class allows for the addition of new converter types with minimal changes to existing code.

### Conclusions
The application achieves the goal of converting between Roman numerals and decimal numbers while maintaining a history of conversions. It effectively uses OOP principles and design patterns to ensure maintainability and extensibility. Future improvements could include adding support for more number systems and enhancing the user interface.

### Future Prospects
Extend the application to support more types of conversions (e.g., binary, hexadecimal).
Implement a graphical user interface (GUI) for better user interaction.
Enhance error handling and input validation to make the application more robust.