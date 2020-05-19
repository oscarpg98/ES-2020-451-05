from src.Trip import Trip
from src.Flights import Flights
from src.User import User
from src.Hotels import Hotels
from src.PaymentData import PaymentData
from src.Cars import Cars
import unittest


class TestTripV3(unittest.TestCase):

    def test_price_add_car(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        car = Cars('1345FHZ', 'Ferrari', 'La Mina', 3, 1499.99)
        trip = Trip(user)
        trip.add_car(car)
        self.assertEqual(4499.97, trip.get_total_price())

    def test_price_delete_car(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        car = Cars('1345FHZ', 'Ferrari', 'La Mina', 3, 1499.99)
        car2 = Cars('5648PSD', 'Xaara Picasso', 'Pedralbes', 3, 19.99)
        trip = Trip(user)
        trip.add_car(car)
        trip.add_car(car2)
        trip.delete_car(car)
        self.assertAlmostEqual(59.97, trip.get_total_price()) #AlmostEqual porque en esta función coge más decimales que no deberían aparecer.

    def test_price_add_hotel(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        hotel = Hotels('xyz', 'Hotel W', 2, 1, 3, 149.99)
        trip = Trip(user)
        trip.add_hotel(hotel)
        self.assertEqual(899.94, trip.get_total_price())

    def test_price_delete_hotel(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        hotel = Hotels('xyz', 'Hotel W', 2, 1, 3, 149.99)
        hotel2 = Hotels('jkl', 'Hostal Menchu', 2, 1, 1, 14.99)
        trip = Trip(user)
        trip.add_hotel(hotel)
        trip.add_hotel(hotel2)
        trip.delete_hotel(hotel)
        self.assertAlmostEqual(29.98, trip.get_total_price())


if __name__ == '__main__':
    unittest.main()