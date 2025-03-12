# Instructions:
#
# Basic Calculator Program
#
# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        
    def addition(self) -> int:
        return  self.a + self.b
    def subtraction(self) -> int:
        return self.a - self.b
    def multiplication(self) -> int:
        return self.a * self.b
    def division(self) -> float:
        return self.a / self.b
print('Basic Calculator Program')
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
calculation = Calculator(first_number, second_number)
print('addition', calculation.addition())
print('subtraction', calculation.subtraction())
print('multiplication', calculation.multiplication())
print('division', calculation.division())
