# -*- coding: utf-8 -*-
from src.Flights import Flights
import os
import unittest
import sys
import pytest

class TestViajeros(unittest.TestCase):
          
    def TestNumViajeros(self):
        numPas=3
        vuelos=Flights('abc', 2, 'Paris', 'Barcelona')
        assert numPas == vuelos.getNumPass()
        print('correcto')
        pass

if __name__ == '__main__':
    unittest.main()
    
