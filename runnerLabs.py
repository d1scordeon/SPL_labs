import os
import subprocess

numbersOfLabs = ['1', '2', '3', '4', '6']
listOfLabs = ['1. Lab1', '2. Lab2', '3. Lab3', '4. Lab4', '6. Lab6 (Unit test)']
mainFolder = 'C:\\Users\\parlethed\\PycharmProjects\\SPL_labs'


print(*listOfLabs, sep="\n")
userInput = input("Choose the project: ")


def open_project(user_input):
    if user_input in numbersOfLabs:
        lab_path = os.path.join(mainFolder, f"lab{user_input}", f"lab{user_input}.py")
        subprocess.run([r'C:\Users\parlethed\AppData\Local\Programs\Python\Python311\python.exe', lab_path], check=True)
    else:
        print("Error: Invalid lab number")


open_project(userInput)
