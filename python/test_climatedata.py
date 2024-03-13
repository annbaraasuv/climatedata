import unittest
from climatedata import plot_city_temperature

class TestPlotCityTemperature(unittest.TestCase):
    def test_plot_city_temperature(self):
        # Test case 1: city with temperature data
        city = 'New York'
        plot_city_temperature(city)
        # The plot should display the temperature data for New York

        # Test case 2: city without temperature data
        city = 'London'
        plot_city_temperature(city)
        # The plot should not display any data as there is no temperature data for London

        # Test case 3: empty city
        city = ''
        plot_city_temperature(city)
        # The plot should not display any data as the city is empty

if __name__ == '__main__':
    unittest.main()