#import external modules
import unittest
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../api_endpoints'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

#import internal classes
from blockchair_bitcoin_stats import BitcoinStats

class TestBitcoinStats(unittest.TestCase): 

    def test_getUrl(self):
        BitcoinStats().getUrl()
        self.assertEquals(BitcoinStats().getUrl(), 'https://api.blockchair.com/bitcoin/stats')

    #def test_getDbTableName(self):
    #    BitcoinStats().getDbTableName
    #    self.assertEquals(BitcoinStats()._getDbTableName)
#
    #def test_getDbTableAttributes(self):
    #    BitcoinStats().getDbTableAttributes
    #    self.assertEquals(BitcoinStats().getDbTableAttributes)
#
    #def test_getDbDynamicInsertPlaceholders(self):
    #    BitcoinStats().getDbDynamicInsertPlaceholders
    #    self.assertEquals(BitcoinStats().getDbDynamicInsertPlaceholders)

if __name__ == '__main__':
    unittest.main()
