from asciiAlphabet import Alphabet

class ASCIIArt:
    def __init__(self):
        self.filename = "art.txt"
        self.text = ""
        self.symbols = ""
        self.height = 0
        self.width = 0
        self.alignment = "left"
        self.color = ""

    def generate_art(self):
        art_lines = []
        symbol_index = 0

        for i in range(max(self.height, len(Alphabet["A"]))):
            art_line = ""
            for char in self.text.upper():
                if char in Alphabet:
                    line = Alphabet[char][i % len(Alphabet[char])]
                    new_line = ""
                    for ch in line:
                        if ch == "#":
                            new_line += self.symbols[symbol_index % len(self.symbols)]
                            symbol_index += 1
                        else:
                            new_line += ch
                    art_line += new_line
                else:
                    art_line += " " * self.width

            if self.alignment == "center":
                art_line = art_line.center(
                    max(self.width, len(Alphabet["A"])) * len(self.text)
                )
            elif self.alignment == "right":
                art_line = art_line.rjust(
                    max(self.width, len(Alphabet["A"])) * len(self.text)
                )

            art_lines.append(art_line)
        return "\n".join(art_lines)

    def display_art(self):
        color_code = ''
        if self.color.lower() == 'white':
            color_code = '\u001b[37;1m'
        elif self.color.lower() == 'black':
            color_code = '\u001b[30m'
        elif self.color.lower() == 'gray':
            color_code = '\u001b[90m'

        colored_art = f"{color_code}{self.generate_art()}\u001b[0m"
        print(colored_art)

    def save_art(self):
        with open(self.filename, "w") as file:
            file.write(self.generate_art())

    def preview_art(self):
        print("Preview:")
        self.display_art()

    def user_input(self):
        print("Welcome to ASCII art generator!")
        self.text = input("Enter the text: ")
        self.symbols = input("Enter the symbol: ")

        self.height = int(input("Enter the height: "))
        self.width = int(input("Enter the width: "))

        self.alignment = input("Enter the alignment (left, center, right): ")
        if self.alignment not in ["left", "center", "right"]:
            print("Invalid alignment. Defaulting to left.")
            self.alignment = "left"

        self.color = input("Enter the color(white and black or gray): ")

    def run_art(self):
        self.user_input()
        self.display_art()
        if input("Do you want to save the art? (yes/no): ").lower() == "yes":
            self.save_art()
            print(f"Art saved to {self.filename}")
        self.preview_art()


running_prog = ASCIIArt()
running_prog.run_art()