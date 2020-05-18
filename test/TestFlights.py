from src.Flights import Flights
import unittest


class TestFlights(unittest.TestCase):

    def test_expected_passengers(self):
        flight = Flights('abc', 2, 'Paris', 'Barcelona')
        self.assertEqual(2, flight.get_passenger_num())

    def test_empty_destination(self):
        flight = Flights('def', 1, 'Paris', '')
        self.assertEqual(True, flight.destination_is_empty())


if __name__ == '__main__':
    unittest.main()
