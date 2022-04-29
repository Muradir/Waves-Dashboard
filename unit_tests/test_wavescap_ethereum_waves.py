#import external modules
import unittest

#import internal folder
import sys, os

pathToApiEndpointsDir = os.path.join(os.path.dirname(__file__), '../api_endpoints')
sys.path.append(pathToApiEndpointsDir)


#import internal classes
from wavescap_ethereum_waves import EthereumWavesMarketPrices

class TestEthereumBitcoinMarketPrices(unittest.TestCase): 

    def test_getUrl(self):
        self.assertEqual(EthereumWavesMarketPrices().getUrl(),'https://wavescap.com/api/chart/pair/474jTeYx2r2Va35794tCScAXWJG9hU2HcgxzMowaZUnu-WAVES-all.json')
        
    def test_getDbTableName(self):
        self.assertEqual(EthereumWavesMarketPrices().getDbTableName(),'wavescap_marketPricesEthereumToWaves')

    def test_getDbTableAttributes(self):
       self.assertEqual(EthereumWavesMarketPrices().getDbTableAttributes(),'(ethereumMarketPrice_waves, date)')

    def test_getDbDynamicInsertPlaceholders(self):
       self.assertEqual(EthereumWavesMarketPrices().getDbDynamicInsertPlaceholders(),'%s, %s')


if __name__ == '__main__':
    unittest.main()