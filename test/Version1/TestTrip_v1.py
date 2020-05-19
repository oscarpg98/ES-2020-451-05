from src.Trip import Trip
from src.Flights import Flights
from src.User import User
from src.PaymentData import PaymentData
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

    def test_flight_list_deleting_dest(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flights('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flights('def', 2, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.delete_flight(flight)
        self.assertEqual('def', trip.get_id(flight2))

    def test_price_deleting_dest(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flights('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flights('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flights('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        trip.delete_flight(flight3)
        self.assertEqual(1999.92, trip.get_total_price())

    def test_payment_done(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flights('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flights('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flights('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        total_price = trip.get_total_price()
        payment = PaymentData('Visa', 'Fariseo', '6456456454', '654', total_price)
        _, msg = payment.do_payment(user)
        self.assertEqual('Payment has been done successfully.', msg)

    def test_reservation(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flights('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flights('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flights('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        total_price = trip.get_total_price()
        payment = PaymentData('Visa', 'Fariseo', '6456456454', '654', total_price)
        payment.do_payment(user)
        done, _ = payment.do_payment(user)
        if done:
            self.assertEqual(True, trip.confirm_flight_reservation(user))


if __name__ == '__main__':
    unittest.main()
