#Lab 1
import math
from re import I

result = []
operations = ['+', '-', '*', '/', '**', 'sqrt', '%']

def add(x: float, operation: str, y: float):
    result.append(f"{x} {operation} {y} = {x + y}")
    return x + y

def sub(x: float, operation: str, y: float):
    result.append(f"{x} {operation} {y} = {x - y}")
    return x - y

def mult(x: float, operation: str, y: float):
    result.append(f"{x} {operation} {y} = {x * y}")
    return x * y

def div(x: float, operation: str, y: float):
    result.append(f"{x} {operation} {y} = {x / y}")
    return x / y

def exp(x: float, operation: str, y: float):
    result.append(f"{x} {operation} {y} = {x ** y}")
    return x ** y

def sqrt(x: float, operation: str):
    result.append(f"{operation}{x} = {math.sqrt(x)}")
    return math.sqrt(x)

def mod(x: float, operation: str, y: float):
    result.append(f"{x} {operation} {y} = {x % y}")
    return x % y

def calculator(x: float, y: float, choice: str):
    if choice not in operations:
        print(f'Invalid operation. Please write one from the list: {operations}')
        return
    if choice == '+':
        print(x, "+", y, "=", add(x, choice, y))
    if choice == '-':
        print(x, "-", y, "=", sub(x, choice, y))
    if choice == '*':
        print(x, "*", y, "=", mult(x, choice, y))
    if choice == '/':
        try:
            print(x, "/", y, "=", div(x, choice, y))
        except ZeroDivisionError:
            print("Division by 0 is not possible!")
    if choice == '**':
        print(x, "**", y, "=", exp(x, choice, y))
    if choice == 'sqrt':
        print("Square root: ", x, "=", sqrt(x, choice))
    if choice == '%':
        print(x, "%", y, "=", mod(x, choice, y))
 
print("Hello! Welcome to Calculator! Choose the option:")

while True:
    try:
        x = float(input("Num 1 ="))
        y = float(input("Num 2 ="))
    except:
        print("Invalid number")
        exit()
    
    print("Choose the operation now!")
    print(" 1.Add(+)\n 2.Substract(-)\n 3.Mutliply(*)\n 4.Divide(/)\n 5.Exponentiation(**)\n 6.Square root(sqrt)\n 7.Modulus(%)")

    choice = input("Your choice:")
    
    calculator(x,y,choice)
    
    next_calculation = input("Let's do next calculation? (yes/no): ")
    
    if next_calculation == "no":
          print(result)
    elif next_calculation == "yes":
          continue
    else:
        print("Invalid Input.")
        continue
    
    delete_history = input("Want to delete history?(yes or no): ")
    
    while delete_history != "yes" and delete_history != "no":
        print("Invalid Input.")
        delete_history = input("Want to delete history?(yes or no): ")
    
    if delete_history == "yes":
        result.clear()
        print("Your history was deleted.")
        print(result)
        break
    else:
        break
     