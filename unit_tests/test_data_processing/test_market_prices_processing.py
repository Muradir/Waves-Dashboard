#import external modules
import unittest
import sys, os

pathToDataProcessingDir = os.path.join(os.path.dirname(__file__), '../../backend_app/data_processing')
sys.path.append(pathToDataProcessingDir)

#import internal classes
from market_prices_processing import MarketPricesDataProcessing

#testing the functionality of the database
class TestMarketPricesDataProcessing(unittest.TestCase):
    
    def test_start(self):
        self.assertEquals(MarketPricesDataProcessing().start(), 'Market Prices Data Loaded')

if __name__ == '__main__':
    unittest.main()