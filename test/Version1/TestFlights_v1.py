from src.Flights import Flights
import unittest


class TestFlights(unittest.TestCase):

    def test_expected_passengers(self):
        flight = Flights('abc', 2, 'Paris', 'Barcelona', 99.99)
        self.assertEqual(2, flight.get_passenger_num())


if __name__ == '__main__':
    unittest.main()
