#import external modules
import unittest

#import internal folder
import sys, os

pathToApiEndpointsDir = os.path.join(os.path.dirname(__file__), '../../backend_app/api_endpoints')
sys.path.append(pathToApiEndpointsDir)


#import internal classes
from blockchair_bitcoin_stats import BitcoinStats

class TestBitcoinStats(unittest.TestCase): 

    def test_getUrl(self):
        self.assertEqual(BitcoinStats().getUrl(),'https://api.blockchair.com/bitcoin/stats')

    def test_getDbTableName(self):
        self.assertEqual(BitcoinStats().getDbTableName(),'blockchair_bitcoinDetails')

    def test_getDbTableAttributes(self):
       self.assertEqual(BitcoinStats().getDbTableAttributes(),'(transactions_total, transactions_24h, averageTransactionFee_24h_usd, marketPriceChangePercentage_24h_usd, marketDominancePercentage)')

    def test_getDbDynamicInsertPlaceholders(self):
       self.assertEqual(BitcoinStats().getDbDynamicInsertPlaceholders(),'%s, %s, %s, %s, %s')


if __name__ == '__main__':
    unittest.main()