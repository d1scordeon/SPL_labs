import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import plotly.express as px


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class LoadDataCommand(Command):
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def execute(self):
        self.data = pd.read_csv(self.filename, delimiter=';')
        return self.data


class ExtremeValuesCommand(Command):
    def __init__(self, data):
        self.data = data
        self.extreme_values = None

    def execute(self):
        self.extreme_values = self.data.describe()
        return self.extreme_values

    def undo(self):
        self.extreme_values = None


class VisualizationReceiver:
    def __init__(self, data):
        self.data = data

    def basic_visualization(self):
        self.data.plot(kind='bar')
        plt.show()

    def extended_visualization(self):
        if len(self.data.columns) >= 2:
            col1 = self.data.columns[0]
            col2 = self.data.columns[1]
            plt.scatter(self.data[col1], self.data[col2])
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title('Extended Visualization: Scatter Plot')
            plt.show()
        else:
            print("Not enough columns for extended visualization.")

    def save_extended_visualization_html(self, filename):
        if len(self.data.columns) >= 2:
            fig = px.scatter(self.data, x=self.data.columns[0], y=self.data.columns[1],
                             title='Extended Visualization: Scatter Plot')
            fig.write_html(filename)
            print(f"Extended visualization saved as HTML: {filename}")
        else:
            print("Not enough columns for extended visualization.")

    def save_basic_visualization_html(self, filename):
        long_form_data = pd.melt(self.data, id_vars=self.data.columns[0], value_vars=self.data.columns[1:])

        fig = px.bar(long_form_data, x='variable', y='value', title='Basic Visualization: Bar Plot')
        fig.write_html(filename)
        print(f"Basic visualization saved as HTML: {filename}")

    def save_extended_visualization_png(self, filename):
        if len(self.data.columns) >= 2:
            col1 = self.data.columns[0]
            col2 = self.data.columns[1]
            plt.scatter(self.data[col1], self.data[col2])
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title('Extended Visualization: Scatter Plot')
            plt.savefig(filename)  
            plt.show()
            print(f"Extended visualization saved as PNG: {filename}")
        else:
            print("Not enough columns for extended visualization.")

    def save_basic_visualization_png(self, filename):
        long_form_data = pd.melt(self.data, id_vars=self.data.columns[0], value_vars=self.data.columns[1:])

        plt.bar(long_form_data['variable'], long_form_data['value'])
        plt.title('Basic Visualization: Bar Plot')
        plt.savefig(filename)
        plt.show()
        print(f"Basic visualization saved as PNG: {filename}")


class BasicVisualizationCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.basic_visualization()


class ExtendedVisualizationCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.extended_visualization()


class Client:
    def __init__(self):
        self.data = None
        self.receiver = VisualizationReceiver(None)
        self.command_stack = []

    def run_command(self, command):
        command.execute()
        self.command_stack.append(command)

    def undo_last_command(self):
        if self.command_stack:
            undone_command = self.command_stack.pop()
            undone_command.undo()
            print(f"Undoing last command: {undone_command}")


if __name__ == "__main__":
    load_command = LoadDataCommand("weather.csv")
    data = load_command.execute()

    extreme_values_command = ExtremeValuesCommand(data)
    extreme_values = extreme_values_command.execute()
    print("Extreme Values:")
    print(extreme_values)

    visualization_receiver = VisualizationReceiver(data)

    basic_visualization_command = BasicVisualizationCommand(visualization_receiver)
    basic_visualization_command.execute()

    extended_visualization_command = ExtendedVisualizationCommand(visualization_receiver)
    extended_visualization_command.execute()

    visualization_receiver.save_basic_visualization_html("basic_visualization.html")
    visualization_receiver.save_extended_visualization_html("extended_visualization.html")

    visualization_receiver.save_basic_visualization_png("basic_visualization.png")
    visualization_receiver.save_extended_visualization_png("extended_visualization.png")

    client = Client()
    client.run_command(load_command)


