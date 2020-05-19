from src.Trip import Trip
from src.Flights import Flights
from src.User import User
import unittest


class TestTrip(unittest.TestCase):

    def test_empty_destination_list(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        trip = Trip(user)
        self.assertEqual(True, trip.destination_is_empty())

    def test_empty_flight_list(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        trip = Trip(user)
        self.assertEqual(True, trip.flight_list_is_empty())

    def test_price_no_destinations(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        trip = Trip(user)
        self.assertEqual(0.0, trip.get_total_price())

    def test_add_destination_list(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flights('abc', 2, 'Paris', 'Barcelona', 99.99)
        trip = Trip(user)
        trip.add_flight(flight)
        self.assertEqual(1, trip.get_flights_len())

    def test_add_flight_list(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flights('abc', 2, 'Paris', 'Barcelona', 99.99)
        trip = Trip(user)
        trip.add_flight(flight)
        self.assertEqual(1, trip.get_destinations_len())

    def test_price_multiple_passengers(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flights('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flights('def', 2, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        self.assertEqual(999.96, trip.get_total_price())

    def test_dest_list_deleting_dest(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flights('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flights('def', 2, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.delete_flight(flight)
        self.assertEqual(['New York'], trip.get_destinations())


if __name__ == '__main__':
    unittest.main()
