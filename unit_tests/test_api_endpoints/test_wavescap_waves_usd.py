#import external modules
import unittest

#import internal folder
import sys, os

pathToApiEndpointsDir = os.path.join(os.path.dirname(__file__), '../../backend_app/api_endpoints')
sys.path.append(pathToApiEndpointsDir)


#import internal classes
from wavescap_waves_usd import WavesUsdMarketPrices

class TestEthereumBitcoinMarketPrices(unittest.TestCase): 

    def test_getUrl(self):
        self.assertEqual(WavesUsdMarketPrices().getUrl(),'https://wavescap.com/api/chart/asset/WAVES-usd-n-all.json')
        
    def test_getDbTableName(self):
        self.assertEqual(WavesUsdMarketPrices().getDbTableName(),'wavescap_marketPricesWavesToUsd')

    def test_getDbTableAttributes(self):
       self.assertEqual(WavesUsdMarketPrices().getDbTableAttributes(),'(wavesMarketPrice_usd, date)')

    def test_getDbDynamicInsertPlaceholders(self):
       self.assertEqual(WavesUsdMarketPrices().getDbDynamicInsertPlaceholders(),'%s, %s')


if __name__ == '__main__':
    unittest.main()