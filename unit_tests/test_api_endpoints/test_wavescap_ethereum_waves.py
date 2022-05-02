#Author: Isabella Lambirth
#Description: This file tests the functionality of public methods in class EthereumWavesMarketPrices


#import external modules
import unittest
import sys, os

#navigation to repository folder on same hirachy level
pathToApiEndpointsDir = os.path.join(os.path.dirname(__file__), '../../backend_app/api_endpoints')
sys.path.append(pathToApiEndpointsDir)

#import internal classes
from wavescap_ethereum_waves import EthereumWavesMarketPrices


class TestEthereumWavesMarketPrices(unittest.TestCase): 

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