# Converter System
Application Description:
The application is a Roman numeral to decimal converter and vice versa. It allows users to input either Roman numerals or decimal numbers and convert them to the corresponding representation. Additionally, it provides functionality to view conversion history.

How to Run:
To run the program, execute main.py in the terminal.

How to Use:
Upon running the program, users are prompted to choose the type of number they want to convert (Roman or Decimal). They can also view conversion history.

Object-Oriented Programming Pillars:
Encapsulation:
```
class HistoryHandler:
    def __init__(self, filename):
        self.filename = filename
        self.history = self.read_history()

    def read_history(self):
        try:
            with open(self.filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def write_history(self, conversion):
        with open(self.filename, 'a') as file:
            file.write(conversion + '\n')

    def print_history(self):
        if not self.history:
            print("No conversion history available.")
        else:
            for i, conversion in enumerate(self.history, 1):
                print(f"{i}. {conversion.strip()}")
```
The HistoryHandler class encapsulates the conversion history data and file operations within its methods, ensuring controlled access to the data.
Abstraction:
```
from abc import ABC, abstractmethod

class Converter(ABC):
    @abstractmethod
    def convert(self, value):
        pass
```
Abstraction is achieved by providing an abstract base class Converter with a method convert(), hiding the implementation details.
Inheritance:
```
class RomanDecimalConverter(Converter):
    def convert(self, value):
```
The RomanDecimalConverter class inherits from the Converter class, inheriting common behavior and interface from the base class.
Polymorphism:
```
from abc import ABC, abstractmethod

class Converter(ABC):
    @abstractmethod
    def convert(self, value):
        pass

class RomanDecimalConverter(Converter):
    def convert(self, value):
        # Implementation for Roman to Decimal and vice versa
        pass

    # Other methods specific to RomanDecimalConverter

# Usage of polymorphism
def perform_conversion(converter, value):
    result = converter.convert(value)
    print(f"Conversion result: {result}")

# Example usage
if __name__ == "__main__":
    roman_converter = RomanDecimalConverter()

    perform_conversion(roman_converter, "XIV")
```
Polymorphism is demonstrated through method overriding in the RomanDecimalConverter class, providing specific implementations for converting between Roman numerals and decimals.

Design Patterns:
Factory Method Pattern:
```
class ConverterFactory:
    def get_converter(self):
        return RomanDecimalConverter()
```
The ConverterFactory class implements the Factory Method pattern by providing a method get_converter() to create instances of converter classes, allowing for flexibility in creating converters without exposing instantiation logic.
Singleton Pattern:
```
class HistoryHandler:
    _instance = None

    def __new__(cls, filename):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```
While not explicitly implemented, the HistoryHandler class exhibits characteristics of the Singleton pattern. Only one instance of HistoryHandler is typically needed to manage conversion history throughout the application.

Results:
Successful Implementation: The program effectively implements the specified design patterns and object-oriented programming principles, including encapsulation, abstraction, inheritance, and polymorphism.
Functional Conversion: Users can convert between Roman numerals and decimal numbers seamlessly, ensuring accurate and reliable conversions.
Conversion History: The program maintains a conversion history, allowing users to track their previous conversions and view them whenever needed.
Flexible Design: The use of design patterns such as the Factory Method Pattern ensures flexibility in creating converter instances, while the abstraction provided by the Converter base class allows for the addition of new converter types with minimal changes to existing code.

Conclusions:
The program achieves its primary objective of providing a user-friendly interface for numeral conversions, coupled with a robust conversion history feature.
The implementation of object-oriented programming principles and design patterns ensures a well-structured and maintainable codebase.
Going forward, the program can be extended by adding support for additional numeral systems, improving error handling mechanisms, or enhancing the user interface for a more intuitive experience.
Overall, the program lays a solid foundation for further enhancements and improvements in the future.