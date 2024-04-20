import unittest
from datetime import datetime
from project3 import input_chart_type, input_time_series_function, input_date

class TestInputValidation(unittest.TestCase):

    def test_symbol(self):
        valid_symbols = ['AAPL', 'GOOGL', 'TSLA', 'AMZN', 'MSFT']
        invalid_symbols = ['aapl', '123', 'ABCD123', '']

        for symbol in valid_symbols:
            self.assertTrue(symbol.isupper() and len(symbol) >= 1 and len(symbol) <= 7)

        for symbol in invalid_symbols:
            self.assertFalse(symbol.isupper() and len(symbol) >= 1 and len(symbol) <= 7)

    def test_chart_type(self):
        valid_chart_types = ['1', '2']
        invalid_chart_types = ['0', '3', 'bar', 'line']

        for chart_type in valid_chart_types:
            self.assertTrue(input_chart_type(chart_type) in ['bar', 'line'])

        for chart_type in invalid_chart_types:
            with self.assertRaises(ValueError):
                input_chart_type(chart_type)

    def test_time_series_function(self):
        valid_time_series = ['1', '2', '3', '4']
        invalid_time_series = ['0', '5', 'intraday', 'daily', 'monthly', 'yearly']

        for ts in valid_time_series:
            self.assertTrue(input_time_series_function(ts) in ['TIME_SERIES_INTRADAY', 'TIME_SERIES_DAILY', 'TIME_SERIES_WEEKLY', 'TIME_SERIES_MONTHLY'])

        for ts in invalid_time_series:
            with self.assertRaises(ValueError):
                input_time_series_function(ts)

    def test_date(self):
        valid_dates = ['2024-01-01', '2024-12-31']
        invalid_dates = ['01-01-2024', '2024/01/01', '2024-13-01', '2024-01-32']

        for date_str in valid_dates:
            self.assertIsInstance(datetime.strptime(date_str, '%Y-%m-%d'), datetime)

        for date_str in invalid_dates:
            with self.assertRaises(ValueError):
                input_date(date_str)


if __name__ == '__main__':
    unittest.main()
