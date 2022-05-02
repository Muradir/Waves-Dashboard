#Author: Isabella Lambirth
#Description: This file tests the functionality of public methods in class EthereumStats

#import external modules
import unittest
import sys, os

#navigation to repository folder on same hirachy level
pathToApiEndpointsDir = os.path.join(os.path.dirname(__file__), '../../backend_app/api_endpoints')
sys.path.append(pathToApiEndpointsDir)

#import internal classes
from blockchair_ethereum_stats import EthereumStats


class TestEthereumStats(unittest.TestCase): 

    def test_getUrl(self):
        self.assertEqual(EthereumStats().getUrl(),'https://api.blockchair.com/ethereum/stats')

    def test_getDbTableName(self):
        self.assertEqual(EthereumStats().getDbTableName(),'blockchair_ethereumDetails')

    def test_getDbTableAttributes(self):
       self.assertEqual(EthereumStats().getDbTableAttributes(),'(transactions_total, transactions_24h, averageTransactionFee_24h_usd, marketPriceChangePercentage_24h_usd, marketDominancePercentage)')

    def test_getDbDynamicInsertPlaceholders(self):
       self.assertEqual(EthereumStats().getDbDynamicInsertPlaceholders(),'%s, %s, %s, %s, %s')


if __name__ == '__main__':
    unittest.main()
