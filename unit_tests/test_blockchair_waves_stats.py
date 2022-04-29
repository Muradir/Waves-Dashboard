#import external modules
import unittest

#import internal folder
import sys, os

pathToApiEndpointsDir = os.path.join(os.path.dirname(__file__), '../backend_app/api_endpoints')
sys.path.append(pathToApiEndpointsDir)


#import internal classes
from blockchair_waves_stats import WavesStats

class TestWavesStats(unittest.TestCase): 

    def test_getUrl(self):
        self.assertEqual(WavesStats().getUrl(),'https://api.blockchair.com/ethereum/erc-20/0x1cf4592ebffd730c7dc92c1bdffdfc3b9efcf29a/stats')

    def test_getDbTableName(self):
        self.assertEqual(WavesStats().getDbTableName(),'blockchair_wavesDetails')

    def test_getDbTableAttributes(self):
       self.assertEqual(WavesStats().getDbTableAttributes(),'(transactions_total, transactions_24h, date)')

    def test_getDbDynamicInsertPlaceholders(self):
       self.assertEqual(WavesStats().getDbDynamicInsertPlaceholders(),'%s, %s, %s')


if __name__ == '__main__':
    unittest.main()