import unittest 
from unittest import TestCase
from unittest.mock import patch 

import restaurants
from yelp_example_data import *

class TestRestaurants(TestCase):

    @patch('restaurants.get_data')
    def test_dollars_to_target(self, mock_api_call):
        mock_api_call.side_effect = [example_raw_data]
        final_list = restaurants.get_restaurants('new york', 'us', 20)
        self.assertEqual(final_list, expected_final_list)

if __name__ == '__main__':
    unittest.main()
