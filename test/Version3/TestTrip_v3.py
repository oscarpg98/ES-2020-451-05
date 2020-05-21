from src.Trip import Trip
from src.Flight import Flight
from src.User import User
from src.Hotel import Hotel
from src.PaymentData import PaymentData
from src.Car import Car
from src.Rentalcars import Rentalcars
from unittest import mock
import unittest


class TestTripV3(unittest.TestCase):

    def test_price_add_car(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        car = Car('1345FHZ', 'Ferrari', 'La Mina', 3, 1499.99)
        trip = Trip(user)
        trip.add_car(car)
        self.assertEqual(4499.97, trip.get_total_price())

    def test_price_delete_car(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        car = Car('1345FHZ', 'Ferrari', 'La Mina', 3, 1499.99)
        car2 = Car('5648PSD', 'Xaara Picasso', 'Pedralbes', 3, 19.99)
        trip = Trip(user)
        trip.add_car(car)
        trip.add_car(car2)
        trip.delete_car(car)
        self.assertAlmostEqual(59.97, trip.get_total_price()) #AlmostEqual porque en esta función coge más decimales que no deberían aparecer.

    def test_price_add_hotel(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        hotel = Hotel('xyz', 'Hotel W', 2, 1, 3, 149.99)
        trip = Trip(user)
        trip.add_hotel(hotel)
        self.assertEqual(899.94, trip.get_total_price())

    def test_price_delete_hotel(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        hotel = Hotel('xyz', 'Hotel W', 2, 1, 3, 149.99)
        hotel2 = Hotel('jkl', 'Hostal Menchu', 2, 1, 1, 14.99)
        trip = Trip(user)
        trip.add_hotel(hotel)
        trip.add_hotel(hotel2)
        trip.delete_hotel(hotel)
        self.assertAlmostEqual(29.98, trip.get_total_price())

    def test_given_a_car_list_when_its_reserved_then_returns_text_confirmation(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        car = Car('1345FHZ', 'Ferrari', 'La Mina', 3, 1499.99)
        car2 = Car('5648PSD', 'Xaara Picasso', 'Central Park', 3, 19.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_car(car)
        trip.add_car(car2)
        self.assertEqual('Your cars have been reserved successfully.', trip.confirm_car_reservation(user))

    @mock.patch('src.Rentalcars')
    def test_given_a_confirmation_error_when_reserving_cars_report_a_message_error(self, mock_rent):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        car = Car('1345FHZ', 'Ferrari', 'La Mina', 3, 1499.99)
        car2 = Car('5648PSD', 'Xaara Picasso', 'Central Park', 3, 19.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_car(car)
        trip.add_car(car2)
        cars = trip.get_cars()
        mock_rent.return_value.confirm_reserve(user, cars).return_value = False
        self.assertEqual('Your car reservation has been denied.', trip.confirm_car_reservation(user))

    def test_given_a_hotel_list_when_its_reserved_then_returns_text_confirmation(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        hotel = Hotel('xyz', 'Hotel W', 2, 1, 3, 149.99)
        hotel2 = Hotel('jkl', 'Hostal Menchu', 2, 1, 1, 14.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_hotel(hotel)
        trip.add_hotel(hotel2)
        self.assertEqual('Your hotels have been reserved successfully.', trip.confirm_hotel_reservation(user))

    @mock.patch('src.Booking')
    def test_given_a_confirmation_error_when_reserving_hotels_report_a_message_error(self, mock_book):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        hotel = Hotel('xyz', 'Hotel W', 2, 1, 3, 149.99)
        hotel2 = Hotel('jkl', 'Hostal Menchu', 2, 1, 1, 14.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_hotel(hotel)
        trip.add_hotel(hotel2)
        hotels = trip.get_hotels()
        mock_book.return_value.confirm_reserve(user, hotels).return_value = False
        self.assertEqual('Your hotel reservation has been denied.', trip.confirm_hotel_reservation(user))


if __name__ == '__main__':
    unittest.main()
