import unittest
from unittest import TestCase
from unittest.mock import patch 


import currency


class TestExchangeRate(TestCase):

    @patch('currency.get_exchange_rate')
    def test_from_currency_to_to_currency_rate(self, mock_rates):
        mock_rate = 1987.899
        example_api_response = {"query": {"from": "USD","to": "GBP","amount": 1},"info": {"timestamp": 1667313964,"rate": mock_rate},"date": "2022-11-01"}
        mock_rates.side_effect = [example_api_response]

        converted =currency.get_exchange_rate(100, 'GBP')
        expected = 198789.9
        self.assertEqual(expected, converted)




if __name__ =='__main__':
    unittest.main()