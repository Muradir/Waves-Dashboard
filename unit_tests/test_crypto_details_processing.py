#import external modules
import unittest
import sys, os

#testdir2 = os.path.dirname(__file__)
#srcdir2 = '../data_stores'
#sys.path.insert(0, os.path.abspath(os.path.join(testdir2, srcdir2)))

testdir = os.path.dirname(__file__)
srcdir = '../data_processing'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

print(sys.path)

#import internal classes
from crypto_details_processing import CryptoStatsDataProcessing

#testing the functionality of the database
class TestCryptoStatsDataProcessing(unittest.TestCase):
    
    def test_start(self):
        self.assertEquals(CryptoStatsDataProcessing().start(), 'Crypto Stats Data Loaded')

if __name__ == '__main__':
    unittest.main()