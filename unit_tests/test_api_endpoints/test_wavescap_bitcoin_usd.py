#import external modules
import unittest

#import internal folder
import sys, os

pathToApiEndpointsDir = os.path.join(os.path.dirname(__file__), '../../backend_app/api_endpoints')
sys.path.append(pathToApiEndpointsDir)


#import internal classes
from wavescap_bitcoin_usd import BitcoinUsdMarketPrices

class TestBitcoinUsdMarketPrices(unittest.TestCase): 

    def test_getUrl(self):
        self.assertEqual(BitcoinUsdMarketPrices().getUrl(),'https://wavescap.com/api/chart/asset/8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS-usd-n-all.json')
        
    def test_getDbTableName(self):
        self.assertEqual(BitcoinUsdMarketPrices().getDbTableName(),'wavescap_marketPricesBitcoinToUsd')

    def test_getDbTableAttributes(self):
       self.assertEqual(BitcoinUsdMarketPrices().getDbTableAttributes(),'(bitcoinMarketPrice_usd, date)')

    def test_getDbDynamicInsertPlaceholders(self):
       self.assertEqual(BitcoinUsdMarketPrices().getDbDynamicInsertPlaceholders(),'%s, %s')


if __name__ == '__main__':
    unittest.main()