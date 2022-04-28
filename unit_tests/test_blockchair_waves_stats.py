#import external modules
import unittest

#import internal folder
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../api_endpoints'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

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