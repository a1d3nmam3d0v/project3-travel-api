import unittest
from unittest import TestCase
from unittest.mock import patch 


import currency


class TestExchangeRate(TestCase):

    @patch('currency.send_latest_exchange_rate_request')
    def test_from_currency_to_to_currency_rate(self, mock_rates):
        example_api_response = {"query": {"from": "USD","to": "GBP","amount": 1},"info": {"timestamp": 1667313964,"rate": 0.86271},"date": "2022-11-01"}
        mock_rates.side_effect = [example_api_response]
        converted = currency.get_exchange_rate('USD', 'GBP')
        expected = ['USD', 'GBP', 0.86271]
        self.assertEqual(expected, converted)




if __name__ =='__main__':
    unittest.main()