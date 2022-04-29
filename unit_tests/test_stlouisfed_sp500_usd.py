#import external modules
import unittest

#import internal folder
import sys, os

pathToApiEndpointsDir = os.path.join(os.path.dirname(__file__), '../api_endpoints')
sys.path.append(pathToApiEndpointsDir)


#import internal classes
from stlouisfed_sp500_usd import SP500UsdMarketPrices

class TestSP500UsdMarketPrices(unittest.TestCase): 

    def test_getUrl(self):
        self.assertEqual(SP500UsdMarketPrices().getUrl(),'https://api.stlouisfed.org/fred/series/observations?api_key=1260500ff9e23c45cdf81a960f44bf68&file_type=json&observation_start=2017-01-01&series_id=SP500')

    def test_getDbTableName(self):
        self.assertEqual(SP500UsdMarketPrices().getDbTableName(),'stlouisfed_marketPricesSP500ToUsd')

    def test_getDbTableAttributes(self):
       self.assertEqual(SP500UsdMarketPrices().getDbTableAttributes(),'(sp500MarketPrice_usd, date)')

    def test_getDbDynamicInsertPlaceholders(self):
       self.assertEqual(SP500UsdMarketPrices().getDbDynamicInsertPlaceholders(),'%s, %s')


if __name__ == '__main__':
    unittest.main()