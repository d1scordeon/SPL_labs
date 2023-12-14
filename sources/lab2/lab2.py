#lab 2
import math

class Calculator:
    def __init__(self): 
        self.x = 0
        self.y = 0
        self.operator = ""

    def user_input(self):
        try: 
            self.x = float(input("Write your first number: "))
            self.y = float(input("Please enter the second number: "))
        except ValueError:
            print("Error: Invalid number input. Please try again.")
            self.user_input()
            return

        self.operator = input("Choose the operator (+, -, *, /): ")
        while not self.validate_operator():
            print("Invalid operator")
            self.operator = input("Choose again (+, -, *, /): ")

    def validate_operator(self):
        return self.operator in ['+', '-', '*', '/']

    def calculation(self):
        if self.operator == '+':
            return self.x + self.y
        if self.operator == '-':
            return self.x - self.y
        if self.operator == '*':
            return self.x * self.y
        if self.operator == '/':
            try:
                return self.x / self.y
            except ZeroDivisionError:
                return "You can't divide by 0!"


class AdvancedCalculator(Calculator):
    def user_input(self):
        try: 
            self.x = float(input("Write your first number: "))
            self.y = float(input("Please enter the second number: "))
        except ValueError:
            print("Error: Invalid number input. Please try again.")
            self.user_input()
            return

        self.operator = input("Choose the operator (+, -, *, /, ^, sqrt, %): ")
        while not self.validate_operator():
            print("Invalid operator")
            self.operator = input("Choose again (+, -, *, /, ^, sqrt, %): ")

    def validate_operator(self):
        return super().validate_operator() or self.operator in ['^', 'sqrt', '%']

    def calculation(self):
        if self.operator in ['^', 'sqrt', '%']:
            if self.operator == '^':
                return self.x ** self.y
            if self.operator == 'sqrt':
                if self.x < 0:
                    return "Cannot compute the square root of a negative number!"
                return math.sqrt(self.x)
            if self.operator == '%':
                return self.x % self.y 
        else:
            return super().calculation()
     
    def running_calculation(self):
        print("Welcome to Advanced Calculator!")
        while True:
            self.user_input()
            result = self.calculation()
            
            if self.operator == 'sqrt':
                print(f"The square root of {self.x} = {result}")
            else:
                print(f"Result of {self.x} {self.operator} {self.y} = {result}")

            answer = input("Would you like to do another calculation? (y/n): ")
            
            while answer.lower() not in ["y", "n"]:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
                answer = input("Would you like to do another calculation? (y/n): ")

            if answer.lower() == "n":
                print("Thank you for using the calculator. Goodbye!")
                break

calc = AdvancedCalculator()
calc.running_calculation()


def run():
    return None