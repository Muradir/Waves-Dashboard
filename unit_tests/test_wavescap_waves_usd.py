#import external modules
import unittest

#import internal folder
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../api_endpoints'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

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