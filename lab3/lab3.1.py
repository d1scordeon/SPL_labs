import pyfiglet
import termcolor
import colorama
import os
import shutil
import re

class TextArt:
    def __init__(self):
        self.text = ""
        self.art = ""
        self.font = ""
        self.color = ""
        self.width = 80
        self.height = None

    def user_input(self):
        self.text = input("Write your text: ")

    def text_2_art(self):
        figlet = pyfiglet.Figlet(font=self.font or "slant")
        self.art = figlet.renderText(self.text)
        
        self.resize_art()
        
        if self.color:
            self.art = termcolor.colored(self.art, self.color)
        self.display_preview()

        if not self.ask_for_preview_approval():
            print("Let's modify your choices.")
            self.running_text_to_art()

    def running_text_to_art(self):
        colorama.init() 
        print("Welcome to Text2Art")
        self.user_input()
        self.font_choose()
        self.set_art_size()
        self.replace_symbols()
        self.color_choose()
        self.text_2_art()
        self.display_preview()
        self.save_to_file("art.txt")
        
class Settings_TextArt(TextArt):
    def font_choose(self):
        fonts = ["slant", "3-d", "roman"]
        print("Available fonts:", ', '.join(fonts))
        chosen_font = input("Choose a font from the list or press enter for default: ").strip().lower()
        if chosen_font in fonts:
            self.font = chosen_font
        else:
            print("Unknown font. Using default.")

    def color_choose(self):
        colors = ["red", "green", "blue", "cyan", "white", "black"]
        print("Available colors:", ', '.join(colors))
        chosen_color = input("Choose a color from the list or press enter for default: ").strip().lower()
        if chosen_color in colors:
            self.color = chosen_color
        else:
            print("Unknown color. Using default.")

    def save_to_file(self, filename):
        save = input("Do you want to save the ASCII art to a file? (yes/no): ")
        if save.lower() == "yes":
            with open(filename, "w") as file:
                file.write(self.art)
                print(f"Saved to {filename}!")
            exit()
        if save.lower() == "no":
            print("Ok! Bye!")
            exit()
        else:
            print("Invalid input")
    
    def display_preview(self):
        terminal_width, _ = shutil.get_terminal_size((80, 20))
        for line in self.art.splitlines():
            print(line.center(terminal_width))
            
    def ask_for_preview_approval(self):
        while True:
            response = input("Are you satisfied with the preview? (yes/no): ").strip().lower()
            if response == "yes":
                return True
            if response == "no":
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")   
            
    def set_art_size(self):
        while True:
            try:
                width_input = input("Set the width (default is 80, press enter for default): ")
                if width_input:  # Check if user input something
                    self.width = int(width_input)
                
                height_input = input("Set the height (press enter to skip): ")
                if height_input:  # Check if user input something
                    self.height = int(height_input)

                break  # Exit the loop if inputs are correct
            except ValueError:
                print("Invalid input. Please enter a valid number or press enter for default values.")

    def resize_art(self):
        lines = self.art.split("\n")
        resized_art = []
        for line in lines:
            resized_art.append(line[:self.width])
        self.art = "\n".join(resized_art)
        
    def replace_symbols(self):
        old_symbol = input("Enter the symbol in the ASCII art you want to replace: ")
        new_symbol = input(f"Enter the symbol you want to replace '{old_symbol}' with: ")
        self.art = self.art.replace(old_symbol, new_symbol)

text_art_running = Settings_TextArt()
text_art_running.running_text_to_art()
