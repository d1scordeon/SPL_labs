import sys
from colorama import Fore, init

init(autoreset=True)


class Command:
    def execute(self):
        pass


class Cube:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def draw(self):
        colors = {
            'red': Fore.RED,
            'green': Fore.GREEN,
            'blue': Fore.BLUE,
            'yellow': Fore.YELLOW,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.WHITE,
            'black': Fore.BLACK
        }

        # Set the selected color or default to white if the color is not found
        cube_color = colors.get(self.color.lower(), Fore.WHITE)

        t = v = h = int(self.size / 2) # top, vertical, horizontal, ініціалізація змінних
        s, p, b, f, n = " ", cube_color + "+", cube_color + "|", cube_color + "/", "\n" # s - space, p - plus, b - bar, f - forward slash, n - new line,
                                                                                        # символьні змінні для відображення куба
        l = p + (cube_color + "-") * (t * 4) + p # l - line, t - top, контур верхньої межі куба
        S = s * (4 * t) # S - space, верхня частина куба
        k = s * h # k - space, вертикальна частина куба
        K = b + S + b # K - bar, вертикальна частина куба
        r = (s * t) + s + l + n # r - result, t - top, l - line, n - new line, перший рядок куба
        while t:
            # t - top, v - vertical, h - horizontal, s - space, f - forward slash, b - bar, n - new line
            r += (s * t) + f + (S + f + s * (h - t) + b) + n
            t -= 1
            # t - top, v - vertical, h - horizontal, s - space, f - forward slash, b - bar, n - new line
        r += l + (k + b) + n + ((K + k + b + n) * (v - 1)) + K + k + p + n
        while v:
            v -= 1
            r += K + (s * v) + f + n
        r += l

        return r


class ASCIIArtRenderer:
    def render(self, command):
        return command.execute()


class DrawCubeCommand(Command):
    def __init__(self, cube):
        self.cube = cube

    def execute(self):
        return self.cube.draw()


class Scene:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def render_scene(self):
        for shape in self.shapes:
            print(shape.draw())


class CommandLineInterface:
    def __init__(self):
        self.scene = Scene()

    def run(self):
        print("Welcome to the 3D ASCII Art Generator!")
        while True:
            command = input("Enter a command (create/cube/size/resize/color/render/save/exit): ").lower()
            if command == "exit":
                sys.exit(0)
            elif command == "create":
                self.create_cube()
            elif command == "render":
                self.scene.render_scene()
            elif command == "cube":
                self.create_cube()
            elif command == "size":
                self.set_size()
            elif command == "resize":
                self.resize_shape()
            elif command == "color":
                self.set_color()
            elif command == "save":
                self.save_to_file()
            else:
                print("Invalid command. Please try again.")

    def create_cube(self):
        size_input = input("Enter the size of the cube: ")
        try:
            size = float(size_input)
        except ValueError:
            print("Invalid input. Please enter a numeric size.")
            return
        color = input("Enter the color of the cube (e.g., red, green, blue, yellow, magenta, cyan, white, black ): ")
        cube = Cube(size, color)
        self.scene.add_shape(cube)
        print("Cube created.")

    def set_size(self):
        size = float(input("Enter the size for the current shape: "))
        if not self.scene.shapes:
            print("No shape to set size. Please create a shape first.")
            return
        current_shape = self.scene.shapes[-1]
        current_shape.size = size

    def resize_shape(self):
        scaling_factor = float(input("Enter the scaling factor for the current shape: "))
        if not self.scene.shapes:
            print("No shape to resize. Please create a shape first.")
            return
        current_shape = self.scene.shapes[-1]
        current_shape.size *= scaling_factor

    def set_color(self):
        if not self.scene.shapes:
            print("No shape to set color. Please create a shape first.")
            return
        color = input("Enter the color for the current shape (e.g., red, green, blue, yellow, magenta, cyan, white, black): ")
        current_shape = self.scene.shapes[-1]
        current_shape.color = color
        print(f"Color set to {color} for the current shape.")

    def save_to_file(self):
        if not self.scene.shapes:
            print("No shapes to save. Please create a shape first.")
            return

        file_name = input("Enter the file name to save the ASCII art (include .txt extension): ")

        try:
            with open(file_name, "w") as file:
                for shape in self.scene.shapes:
                    ascii_art = shape.draw()
                    file.write(ascii_art + "\n\n")
            print(f"ASCII art saved to {file_name}.")
        except Exception as e:
            print(f"Error saving to file: {e}")


def main():
    cli = CommandLineInterface()
    cli.run()


if __name__ == "__main__":
    main()

