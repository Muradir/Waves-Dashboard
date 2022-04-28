#import external modules
import unittest

#import internal folder
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../api_endpoints'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

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