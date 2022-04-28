#import external modules
import unittest

from api_endpoints.blockchair_bitcoin_stats import BitcoinStats

#import internal classes
#from api_endpoints.blockchair_bitcoin_stats import BitcoinStats

class TestBitcoinStats(unittest.Testcase): 

    def test_getUrl(self):
        BitcoinStats().getUrl()
        self.assertEquals(BitcoinStats().getUrl)

    def test_getDbTableName(self):
        BitcoinStats().getDbTableName
        self.assertEquals(BitcoinStats()._getDbTableName)

    def test_getDbTableAttributes(self):
        BitcoinStats().getDbTableAttributes
        self.assertEquals(BitcoinStats().getDbTableAttributes)

    def test_getDbDynamicInsertPlaceholders(self):
        BitcoinStats().getDbDynamicInsertPlaceholders
        self.assertEquals(BitcoinStats().getDbDynamicInsertPlaceholders)
