#import external modules
import unittest

#import internal folder
import sys, os

pathToApiEndpointsDir = os.path.join(os.path.dirname(__file__), '../../backend_app/api_endpoints')
sys.path.append(pathToApiEndpointsDir)


#import internal classes
from wavescap_waves_bitcoin import WavesBitcoinMarketPrices

class TestEthereumBitcoinMarketPrices(unittest.TestCase): 

    def test_getUrl(self):
        self.assertEqual(WavesBitcoinMarketPrices().getUrl(),'https://wavescap.com/api/chart/pair/WAVES-8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS-all.json')
        
    def test_getDbTableName(self):
        self.assertEqual(WavesBitcoinMarketPrices().getDbTableName(),'wavescap_marketPricesWavesToBitcoin')

    def test_getDbTableAttributes(self):
       self.assertEqual(WavesBitcoinMarketPrices().getDbTableAttributes(),'(wavesMarketPrice_bitcoin, date)')

    def test_getDbDynamicInsertPlaceholders(self):
       self.assertEqual(WavesBitcoinMarketPrices().getDbDynamicInsertPlaceholders(),'%s, %s')


if __name__ == '__main__':
    unittest.main()