#Author: Lars Brebeck
#Description: This file manages the data movement from api-endpoint to database 

#import external modules
import requests
from datetime import date
from dateutil.relativedelta import relativedelta
from decimal import Decimal
import os, sys

#navigation to repository folder on same hirachy level
pathToApiEndpointsDir = os.path.join(os.path.dirname(__file__), '../api_endpoints')
sys.path.append(pathToApiEndpointsDir)

pathToDataStoresDir = os.path.join(os.path.dirname(__file__), '../data_stores')
sys.path.append(pathToDataStoresDir)

#import internal classes
from database import Database
from stlouisfed_sp500_usd import SP500UsdMarketPrices
from wavescap_bitcoin_usd import BitcoinUsdMarketPrices
from wavescap_ethereum_bitcoin import EthereumBitcoinMarketPrices
from wavescap_ethereum_usd import EthereumUsdMarketPrices
from wavescap_ethereum_waves import EthereumWavesMarketPrices
from wavescap_waves_bitcoin import WavesBitcoinMarketPrices
from wavescap_waves_usd import WavesUsdMarketPrices


class MarketPricesDataProcessing:

    #public class method, initiates the data processing workflow by invoking private class methods
    def start(self):
        cryptosToUsd = [BitcoinUsdMarketPrices(), EthereumUsdMarketPrices(), WavesUsdMarketPrices()]
        for item in cryptosToUsd:
            self.__getCryptoMarketPricesInUsd(item)
        
        cryptosToCrypto = [EthereumBitcoinMarketPrices(), EthereumWavesMarketPrices(), WavesBitcoinMarketPrices()]
        for item in cryptosToCrypto:
            self.__getCryptoMarketPricesInCrypto(cryptoCurrency=item)

        self.__getFundMarketPricesInUsd(SP500UsdMarketPrices())
        return 'Market Prices Data Loaded'


    #private class method, gets data via api request and initiates the database insertion
    def __getFundMarketPricesInUsd(self, indexFund):
        response = requests.get(url = indexFund.getUrl()).json()
        marketPrices = response['observations']

        recordsToInsert = []
        for item in marketPrices:
            if(item['value']) != '.':
                attributes = [Decimal(item['value']), date.fromisoformat(item['date'])]
                recordsToInsert.append(tuple(attributes))
    
        Database().insertDataIntoDatabase(entity=indexFund, recordsToInsert=recordsToInsert)


    #private class method, gets data via api request and initiates the database insertion
    def __getCryptoMarketPricesInUsd(self, cryptoCurrency):
        response = requests.get(url = cryptoCurrency.getUrl()).json()
        marketPrices = response['data']
        startTime = date.fromisoformat(response['start'][:10])
    
        recordsToInsert = []
        for item in marketPrices:
            marketPrice = item[0]
            startTime += relativedelta(days=1)
            recordsToInsert.append(tuple([marketPrice, startTime]))
        
        Database().insertDataIntoDatabase(entity=cryptoCurrency, recordsToInsert=recordsToInsert)

    #private class method, gets data via api request and initiates the database insertion
    def __getCryptoMarketPricesInCrypto(self, cryptoCurrency):
        response = requests.get(url = cryptoCurrency.getUrl()).json()
        marketPrices = response['data']

        recordsToInsert = []
        for item in marketPrices:
            marketPrice = item['data']['weightedAveragePrice']
            startTime = date.fromisoformat(item['data']['time'][:10]) + relativedelta(days=1)
            recordsToInsert.append(tuple([marketPrice, startTime]))

        Database().insertDataIntoDatabase(entity=cryptoCurrency, recordsToInsert=recordsToInsert)