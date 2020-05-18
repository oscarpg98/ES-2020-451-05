from src.Trip import Trip
from src.Flights import Flights
from src.User import User
import unittest


class TestTrip(unittest.TestCase):

    def test_add_destination(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flights('abc', 2, 'Paris', 'Barcelona')
        trip = Trip(user)
        trip.add_flight(flight)
        self.assertEqual(1, trip.get_flights())


if __name__ == '__main__':
    unittest.main()
