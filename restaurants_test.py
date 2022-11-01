import unittest 
from unittest import TestCase
from unittest.mock import patch 

import restaurants

class TestRestaurants(TestCase):
    @patch('restaurants')