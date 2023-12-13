from abc import ABC, abstractmethod
import requests
from tabulate import tabulate
import json
from datetime import datetime
import csv


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Concrete Command
class WeatherCommand(Command):
    def __init__(self, api_key, base_url, city):
        self.api_key = api_key
        self.base_url = base_url
        self.city = city

    def execute(self):
        params = {'q': self.city, 'key': self.api_key}
        response = requests.get(self.base_url, params=params)

        # Print debugging information
        print(f"Request URL: {response.url}")
        print(f"Status Code: {response.status_code}")

        try:
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()
            print(f"Response Data: {data}")
            return data
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except json.JSONDecodeError as json_err:
            print(f"Error decoding JSON response: {json_err}")
        except requests.RequestException as req_err:
            print(f"An error occurred during the request: {req_err}")
        return None


# Invoker
class WeatherInvoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        if self.command:
            return self.command.execute()
        else:
            print("No command set.")


class WeatherApp:
    def __init__(self, api_key, base_url):
        self.base_url = base_url
        self.api_key = api_key
        self.history = []
        self.invoker = WeatherInvoker()

    def get_weather(self, city):
        command = WeatherCommand(self.api_key, self.base_url, city)
        self.invoker.set_command(command)
        result = self.invoker.execute_command()

        # Check if the response is successful
        if result is not None and 'error' not in result:
            # Extract relevant information from the response
            current_data = result.get('current', {})
            temperature = current_data.get('temp_c', 'N/A')
            description = current_data.get('condition', {}).get('text', 'N/A')

            weather_info = {'city': city, 'temperature': temperature, 'description': description}
            self.history.append(weather_info)
            return weather_info
        else:
            print(f"Error: Unable to retrieve weather information for {city}.")
            return None

    def display_table(self, data):
        headers = ['City', 'Temperature (°C)', 'Description']
        data_list = [
            [data['city'], data['temperature'], data['description']]
        ]
        print(tabulate(data_list, headers=headers, tablefmt='grid'))

    def save_history(self, filename, file_format):
        if file_format == 'json':
            with open(filename, 'w') as json_file:
                json.dump(self.history, json_file, indent=2)
        elif file_format == 'txt':
            with open(filename, 'w') as txt_file:
                for entry in self.history:
                    txt_file.write(f"{entry['city']}: {entry['temperature']}°C, {entry['description']}\n")
        elif file_format == 'csv':
            with open(filename, 'w', newline='') as csv_file:
                headers = list(self.history[0].keys()) if self.history else []  # Use keys from the first entry
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(self.history)

    def display_history(self):
        if not self.history:
            print("No history available.")
        else:
            print("Weather History:")
            headers = ['City', 'Temperature (°C)', 'Description']
            data_list = [
                [entry['city'], entry['temperature'], entry['description']] for entry in self.history
            ]
            print(tabulate(data_list, headers=headers, tablefmt='grid'))


if __name__ == '__main__':
    api_key = '676bfc001e434e959b4143404231312'
    base_url = 'http://api.weatherapi.com/v1/current.json'
    weather_app = WeatherApp(api_key, base_url)

    while True:
        user_input = input('Enter city name (or type "history" to view history, "save" to save history, or "exit" to quit): ')

        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'history':
            weather_app.display_history()
        elif user_input.lower() == 'save':
            save_format = input('Enter save format (json, txt, or csv): ')
            save_filename = input('Enter save filename: ')
            if not save_filename.endswith('.'):
                save_filename += '.'
            save_filename += save_format
            weather_app.save_history(save_filename, save_format)
            print(f"History saved to {save_filename} in {save_format} format.")
        else:
            weather_data = weather_app.get_weather(user_input)

            if weather_data is not None:
                weather_app.display_table(weather_data)
