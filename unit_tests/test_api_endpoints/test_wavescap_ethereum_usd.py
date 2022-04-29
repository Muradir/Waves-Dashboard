#import external modules
import unittest

#import internal folder
import sys, os

pathToApiEndpointsDir = os.path.join(os.path.dirname(__file__), '../../backend_app/api_endpoints')
sys.path.append(pathToApiEndpointsDir)


#import internal classes
from wavescap_ethereum_usd import EthereumUsdMarketPrices

class TestEthereumBitcoinMarketPrices(unittest.TestCase): 

    def test_getUrl(self):
        self.assertEqual(EthereumUsdMarketPrices().getUrl(),'https://wavescap.com/api/chart/asset/474jTeYx2r2Va35794tCScAXWJG9hU2HcgxzMowaZUnu-usd-n-all.json')
        
    def test_getDbTableName(self):
        self.assertEqual(EthereumUsdMarketPrices().getDbTableName(),'wavescap_marketPricesEthereumToUsd')

    def test_getDbTableAttributes(self):
       self.assertEqual(EthereumUsdMarketPrices().getDbTableAttributes(),'(ethereumMarketPrice_usd, date)')

    def test_getDbDynamicInsertPlaceholders(self):
       self.assertEqual(EthereumUsdMarketPrices().getDbDynamicInsertPlaceholders(),'%s, %s')


if __name__ == '__main__':
    unittest.main()