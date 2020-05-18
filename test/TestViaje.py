# -*- coding: utf-8 -*-
from src.Flights import Flights
import unittest


class TestViaje(unittest.TestCase):

    def test_num_viajeros(self):
        vuelos = Flights('abc', 2, 'Paris', 'Barcelona')
        self.assertEqual(2, vuelos.get_num_pass())
        pass

    def test_num_destinos(self):
        vuelo = Flights()
        self.assertEqual(None, vuelo.get_destinacion())


if __name__ == '__main__':
    unittest.main()
