import unittest
from unittest.mock import Mock, patch

from sources.lab7.lab7 import WeatherCommand


class TestWeatherCommand(unittest.TestCase):
    def setUp(self):
        self.api_key = '676bfc001e434e959b4143404231312'
        self.base_url = 'http://api.weatherapi.com/v1/current.json'
        self.city = 'Lviv'

    @patch('lab7.app.requests.get')
    def test_execute_successful_request(self, mock_requests_get):
        # Mock the requests.get method to return a successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'current': {'temp_c': 25, 'condition': {'text': 'Sunny'}}}
        mock_requests_get.return_value = mock_response

        weather_command = WeatherCommand(self.api_key, self.base_url, self.city)

        result = weather_command.execute()

        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result['current']['temp_c'], 25)
        self.assertEqual(result['current']['condition']['text'], 'Sunny')

    @patch('lab7.app.requests.get')
    def test_execute_unsuccessful_request(self, mock_requests_get):

        mock_response = Mock()
        mock_response.status_code = 404
        mock_requests_get.return_value = mock_response

        weather_command = WeatherCommand(self.api_key, self.base_url, self.city)

        result = weather_command.execute()

        # Assertions
        self.assertIsNotNone(result)
        mock_requests_get.assert_called_once_with(
            self.base_url, params={'q': self.city, 'key': self.api_key}
        )


if __name__ == '__main__':
    unittest.main()
