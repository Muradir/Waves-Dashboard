#import external modules
import unittest

from api_endpoints.blockchair_bitcoin_stats import BitcoinStats

#import internal classes
#from api_endpoints.blockchair_bitcoin_stats import BitcoinStats

class TestBitcoinStats(unittest.TestCase): 

    def test_getUrl(self):
        BitcoinStats().getUrl
        self.assertTrue(BitcoinStats().getUrl,'https://api.blockchair.com/bitcoin/stats')

    def test_getDbTableName(self):
       BitcoinStats().getDbTableName
       self.assertTrue(BitcoinStats().getDbTableName,'blockchair_bitcoinDetails')

    def test_getDbTableAttributes(self):
       BitcoinStats().getDbTableAttributes
       self.assertTrue(BitcoinStats().getDbTableAttributes,'(transactions_total, transactions_24h, averageTransactionFee_24h_usd, marketPriceChangePercentage_24h_usd, marketDominancePercentage)')

    def test_getDbDynamicInsertPlaceholders(self):
       BitcoinStats().getDbDynamicInsertPlaceholders
       self.assertTrue(BitcoinStats().getDbDynamicInsertPlaceholders,'%s, %s, %s, %s, %s')


if __name__ == '__main__':
    unittest.main()