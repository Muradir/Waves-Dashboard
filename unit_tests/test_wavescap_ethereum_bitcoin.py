#import external modules
import unittest

#import internal folder
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../api_endpoints'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

#import internal classes
from wavescap_ethereum_bitcoin import EthereumBitcoinMarketPrices

class TestEthereumBitcoinMarketPrices(unittest.TestCase): 

    def test_getUrl(self):
        self.assertEqual(EthereumBitcoinMarketPrices().getUrl(),'https://wavescap.com/api/chart/pair/474jTeYx2r2Va35794tCScAXWJG9hU2HcgxzMowaZUnu-8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS-all.json')
        
    def test_getDbTableName(self):
        self.assertEqual(EthereumBitcoinMarketPrices().getDbTableName(),'wavescap_marketPricesEthereumToBitcoin')

    def test_getDbTableAttributes(self):
       self.assertEqual(EthereumBitcoinMarketPrices().getDbTableAttributes(),'(ethereumMarketPrice_bitcoin, date)')

    def test_getDbDynamicInsertPlaceholders(self):
       self.assertEqual(EthereumBitcoinMarketPrices().getDbDynamicInsertPlaceholders(),'%s, %s')


if __name__ == '__main__':
    unittest.main()