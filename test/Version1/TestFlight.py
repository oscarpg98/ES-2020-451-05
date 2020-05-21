from src.Flight import Flight
import unittest


class TestFlights(unittest.TestCase):

    def test_expected_passengers(self):
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        self.assertEqual(2, flight.get_passenger_num())


if __name__ == '__main__':
    unittest.main()
