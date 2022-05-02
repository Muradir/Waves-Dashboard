#Author: Lars Brebeck
#Description: This file tests the functionality of public methods in class CryptoStatsDataProcessing

#import external modules
import unittest
import sys, os

#navigation to repository folder on same hirachy level
pathToDataProcessingDir = os.path.join(os.path.dirname(__file__), '../../backend_app/data_processing')
sys.path.append(pathToDataProcessingDir)

#import internal classes
from crypto_details_processing import CryptoStatsDataProcessing


class TestCryptoStatsDataProcessing(unittest.TestCase):
    
    def test_start(self):
        self.assertEquals(CryptoStatsDataProcessing().start(), 'Crypto Stats Data Loaded')

if __name__ == '__main__':
    unittest.main()