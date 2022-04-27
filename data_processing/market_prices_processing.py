#import internal classes
from data_stores.database import Database
from api_endpoints.stlouisfed_sp500_usd import SP500UsdMarketPrices
from api_endpoints.wavescap_bitcoin_usd import BitcoinUsdMarketPrices
from api_endpoints.wavescap_ethereum_bitcoin import EthereumBitcoinMarketPrices
from api_endpoints.wavescap_ethereum_usd import EthereumUsdMarketPrices
from api_endpoints.wavescap_ethereum_waves import EthereumWavesMarketPrices
from api_endpoints.wavescap_waves_bitcoin import WavesBitcoinMarketPrices
from api_endpoints.wavescap_waves_usd import WavesUsdMarketPrices
#import external modules
import requests
from datetime import date
from dateutil.relativedelta import relativedelta
from decimal import Decimal

class MarketPricesDataProcessing:
    def start(self):
        cryptosToUsd = [BitcoinUsdMarketPrices(), EthereumUsdMarketPrices(), WavesUsdMarketPrices()]
        for item in cryptosToUsd:
            self.__getCryptoMarketPricesInUsd(item)
        
        cryptosToCrypto = [EthereumBitcoinMarketPrices(), EthereumWavesMarketPrices(), WavesBitcoinMarketPrices()]
        for item in cryptosToCrypto:
            self.__getCryptoMarketPricesInCrypto(cryptoCurrency=item)

        self.__getFundMarketPricesInUsd(SP500UsdMarketPrices())


    def __getFundMarketPricesInUsd(self, indexFund):
        response = requests.get(url = indexFund.getUrl()).json()
        marketPrices = response['observations']

        recordsToInsert = []
        for item in marketPrices:
            if(item['value']) != '.':
                attributes = [Decimal(item['value']), date.fromisoformat(item['date'])]
                recordsToInsert.append(tuple(attributes))
    
        Database().insertDataIntoDatabase(entity=indexFund, recordsToInsert=recordsToInsert)


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


    def __getCryptoMarketPricesInCrypto(self, cryptoCurrency):
        response = requests.get(url = cryptoCurrency.getUrl()).json()
        marketPrices = response['data']

        recordsToInsert = []
        for item in marketPrices:
            marketPrice = item['data']['weightedAveragePrice']
            startTime = date.fromisoformat(item['data']['time'][:10]) + relativedelta(days=1)
            recordsToInsert.append(tuple([marketPrice, startTime]))

        Database().insertDataIntoDatabase(entity=cryptoCurrency, recordsToInsert=recordsToInsert)