#Author: Lars Brebeck
#Description: This file tests the functionality of public methods in class MarketPricesDataProcessing

#import external modules
import unittest
import sys, os

#navigation to repository folder on same hirachy level
pathToDataProcessingDir = os.path.join(os.path.dirname(__file__), '../../backend_app/data_processing')
sys.path.append(pathToDataProcessingDir)

#import internal classes
from market_prices_processing import MarketPricesDataProcessing


class TestMarketPricesDataProcessing(unittest.TestCase):
    
    def test_start(self):
        self.assertEquals(MarketPricesDataProcessing().start(), 'Market Prices Data Loaded')

if __name__ == '__main__':
    unittest.main()