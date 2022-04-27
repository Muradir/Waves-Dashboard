#import internal classes
from api_requests import ApiRequests
from crypto_details_processing import CryptoStatsDataProcessing
from database import Database
from database import Database
from endpoints.blockchair_bitcoin_stats import BitcoinStats
from endpoints.blockchair_ethereum_stats import EthereumStats
from endpoints.blockchair_waves_stats import WavesStats
from endpoints.stlouisfed_sp500_usd import SP500UsdMarketPrices

from endpoints.wavescap_bitcoin_usd import BitcoinUsdMarketPrices
from endpoints.wavescap_ethereum_bitcoin import EthereumBitcoinMarketPrices
from endpoints.wavescap_ethereum_usd import EthereumUsdMarketPrices
from endpoints.wavescap_ethereum_waves import EthereumWavesMarketPrices
from endpoints.wavescap_waves_bitcoin import WavesBitcoinMarketPrices
from endpoints.wavescap_waves_usd import WavesUsdMarketPrices

#import external modules
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from decimal import Decimal


def main():
    print("Wir schaffen das!")
    #getMarketPricesData()
    CryptoStatsDataProcessing().start()


def getMarketPricesData():
    cryptosToUsd = [BitcoinUsdMarketPrices(), EthereumUsdMarketPrices(), WavesUsdMarketPrices()]
    for item in cryptosToUsd:
        getCryptoMarketPricesInUsd(item)
    
    cryptosToCrypto = [EthereumBitcoinMarketPrices(), EthereumWavesMarketPrices(), WavesBitcoinMarketPrices()]
    for item in cryptosToCrypto:
        getCryptoMarketPricesInCrypto(cryptoCurrency=item)

    getFundMarketPricesInUsd(SP500UsdMarketPrices())


def getFundMarketPricesInUsd(indexFund):
    response = ApiRequests.getDataByGetRequest(indexFund.getUrl(), [])
    marketPrices = response['observations']

    recordsToInsert = []
    for item in marketPrices:
        if(item['value']) != '.':
            attributes = [Decimal(item['value']), date.fromisoformat(item['date'])]
            recordsToInsert.append(tuple(attributes))
  
    Database().insertDataIntoDatabase(entity=indexFund, recordsToInsert=recordsToInsert)


def getCryptoMarketPricesInUsd(cryptoCurrency):
    
    response = ApiRequests.getDataByGetRequest(cryptoCurrency.getUrl(), [])
    marketPrices = response['data']
    startTime = date.fromisoformat(response['start'][:10])
 
    recordsToInsert = []
    for item in marketPrices:
        marketPrice = item[0]
        startTime += relativedelta(days=1)
        recordsToInsert.append(tuple([marketPrice, startTime]))
    
    Database().insertDataIntoDatabase(entity=cryptoCurrency, recordsToInsert=recordsToInsert)


def getCryptoMarketPricesInCrypto(cryptoCurrency):
    
    response = ApiRequests.getDataByGetRequest(cryptoCurrency.getUrl(), [])
    marketPrices = response['data']

    recordsToInsert = []
    for item in marketPrices:
        marketPrice = item['data']['weightedAveragePrice']
        startTime = date.fromisoformat(item['data']['time'][:10]) + relativedelta(days=1)
        recordsToInsert.append(tuple([marketPrice, startTime]))

    Database().insertDataIntoDatabase(entity=cryptoCurrency, recordsToInsert=recordsToInsert)



if __name__ == "__main__":
    main()