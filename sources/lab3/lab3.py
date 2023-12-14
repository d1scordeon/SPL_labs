from art import text2art
import termcolor
import colorama
import os

class TextArt:
    def init(self):
        self.text = ""
        self.art = ""
        self.font = ""
        self.color = ""

    def user_input(self):
        self.text = input("Write your text: ")

    def ask_for_preview_approval(self):
        while True:
            response = input("Are you satisfied with the preview? (yes/no): ").strip().lower()
            if response == "yes":
                return True
            if response == "no":
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")        
     
    def text_2_art(self):
        self.art = text2art(self.text, font=self.font)
        if self.color:
            self.art = termcolor.colored(self.art, self.color)
        self.display_preview()

        if not self.ask_for_preview_approval():
            print("Let's modify your choices.")
            self.running_text_to_art()
            
        try:
            terminal_width = os.get_terminal_size().columns
        except OSError:
            terminal_width = 80

        for line in self.art.splitlines():
            print(line.center(terminal_width))

        self.save_to_file("output_art.txt")

    def running_text_to_art(self):
        colorama.init() 
        print("Welcome to Text2Art")

        self.user_input()
        self.font_choose()
        self.color_choose()
        self.text_2_art()
        self.save_to_file("filename.txt")
        
class Settings_TextArt(TextArt):
    def font_choose(self):
        fonts = ["block", "banner", "standard", "lean", "avatar", "small", "big"]
        print("Available fonts:", ', '.join(fonts))
        chosen_font = input("Choose a font from the list or press enter for default: ").strip().lower()
        if chosen_font in fonts:
            self.font = chosen_font
        else:
            print("Unknown font. Using default.")

    def color_choose(self):
        colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white", "grey"]
        print("Available colors:", ', '.join(colors))
        chosen_color = input("Choose a color from the list or press enter for default: ").strip().lower()
        if chosen_color in colors:
            self.color = chosen_color
        else:
            print("Unknown color. Using default.")

    def save_to_file(self, filename):
        save = input("Do you want to save the ASCII art to a file? (yes/no): ")
        if save.lower() == "yes":
            with open("ascii_art.txt", "w") as file:
                file.write(self.art)
                print("Saved to ascii_art.txt!")
                exit()
        if save.lower() == "no":
            print("Ok! Bye!")
            exit()
        if save.lower() != "yes" or "no":
            print("Invalid input")
    
    def display_preview(self):
        try:
            terminal_width = os.get_terminal_size().columns
        except OSError:
            terminal_width = 80

        for line in self.art.splitlines():
            print(line.center(terminal_width))


def main():
    text_art_running = Settings_TextArt()
    text_art_running.running_text_to_art()


if __name__ == "__main__":
    main()

