from src.Trip import Trip
from src.Flight import Flight
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
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        self.assertEqual(['Barcelona', 'New York'], trip.get_destinations())

    def test_add_flight_list(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        self.assertEqual(['abc', 'def'], trip.get_flight_ids())

    def test_price_multiple_passengers(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        self.assertEqual(999.96, trip.get_total_price())

    def test_dest_list_deleting_dest(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.delete_flight(flight)
        self.assertEqual(['New York'], trip.get_destinations())

    def test_flight_list_deleting_dest(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.delete_flight(flight)
        self.assertEqual(['def'], trip.get_flight_ids())

    def test_price_deleting_dest(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flight('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        trip.delete_flight(flight3)
        self.assertEqual(1999.92, trip.get_total_price())

    def test_payment_done(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flight('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        total_price = trip.get_total_price()
        payment = PaymentData('Visa', 'Fariseo', '6456456454', '654', total_price)
        answer = trip.do_payment(user, payment)
        self.assertEqual('Payment has been done successfully.', answer)

    def test_flight_reservation(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flight('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        self.assertEqual(True, trip.confirm_flight_reservation(user))


if __name__ == '__main__':
    unittest.main()

'''
@pytest.fixture()
def trip1():
    user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
    flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
    flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
    flight3 = Flight('ghi', 4, 'New York', 'Paris', 299.99)
    trip = Trip(user)
    trip.add_flight(flight)
    trip.add_flight(flight2)
    trip.add_flight(flight3)
    return trip
'''
