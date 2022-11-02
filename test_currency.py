import unittest
from unittest import TestCase
from unittest.mock import patch 


import currency


class TestExchangeRate(TestCase):


  
    @patch('currency.send_latest_exchange_rate_request')
    def test_from_currency_to_to_currency_rate(self, mock_rates):
        mock_rate = 1987.899
        example_api_response ={"query": {"from": "USD","to": "GBP","amount": 1},"info": {"timestamp": 1667330586,"rate": mock_rate},"date": "2022-11-01","result": mock_rate}
        mock_rates.side_effect = [ example_api_response ]

 
        exchange_rate=currency.send_latest_exchange_rate_request('100','GBP')
        expected = 198789.9
       
        self.assertEqual(exchange_rate,expected)




if __name__ =='__main__':
    unittest.main()