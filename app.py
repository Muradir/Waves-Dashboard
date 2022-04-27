#import internal classes
from api_requests import ApiRequests
from database import Database
from database import Database

#import external modules
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

from endpoints.wavescap_bitcoin_usd import BitcoinUsdMarketPrices
from endpoints.wavescap_ethereum_bitcoin import EthereumBitcoinMarketPrices
from endpoints.wavescap_ethereum_usd import EthereumUsdMarketPrices
from endpoints.wavescap_ethereum_waves import EthereumWavesMarketPrices
from endpoints.wavescap_waves_bitcoin import WavesBitcoinMarketPrices
from endpoints.wavescap_waves_usd import WavesUsdMarketPrices



def main():
    database = Database()
    print("Wir schaffen das!")
    getMarketPricesData(database=database)
    #getMarketPrData(database=database)


def getMarketPricesData(database):
    cryptosToUsd = []
    bitcoinToUsd = BitcoinUsdMarketPrices()
    cryptosToUsd.append(bitcoinToUsd)
    ethereumToUsd = EthereumUsdMarketPrices()
    cryptosToUsd.append(ethereumToUsd)
    wavesToUsd = WavesUsdMarketPrices()
    cryptosToUsd.append(wavesToUsd)

    for item in cryptosToUsd:
        getCryptoMarketPricesInUsd(database, item)

    cryptosToCrypto = []
    ethereumToBitcoin = EthereumBitcoinMarketPrices()
    cryptosToCrypto.append(ethereumToBitcoin)
    ethereumToWaves = EthereumWavesMarketPrices()
    cryptosToCrypto.append(ethereumToWaves)
    wavesToBitcoin = WavesBitcoinMarketPrices()
    cryptosToCrypto.append(wavesToBitcoin)

    for item in cryptosToCrypto:
        getCryptoMarketPricesInCrypto(database=database, cryptoCurrency=item)



def getCryptoMarketPricesInUsd(database, cryptoCurrency):
    
    response = ApiRequests.getDataByGetRequest(cryptoCurrency.getUrl(), [])
    marketPrices = response['data']
    startTime = response['start'][:10]

    startTime = date.fromisoformat(startTime)
 
    recordsToInsert = []
    for item in marketPrices:
        item.pop()
        startTime = startTime + relativedelta(days=1)
        item.append(startTime)
        recordsToInsert.append(tuple(item))
    


    database.executeInsertStatement(tableName=cryptoCurrency.getTableName(), tableAttributes=cryptoCurrency.getTableAttributes(), data=recordsToInsert, dynamicInsertPlaceholders=cryptoCurrency.getDynamicInsertPlaceholders())

    print('Data inserted successfully!')



def getCryptoMarketPricesInCrypto(database, cryptoCurrency):
    
    response = ApiRequests.getDataByGetRequest(cryptoCurrency.getUrl(), [])
    marketPrices = response['data']

    recordsToInsert = []
    for item in marketPrices:
        attributes = []
        attributes.append(item['data']['weightedAveragePrice'])
        startTime = item['data']['time'][:10]
        startTime = date.fromisoformat(startTime)
        attributes.append(startTime)
        
        recordsToInsert.append(tuple(attributes))


    database.executeInsertStatement(tableName=cryptoCurrency.getTableName(), tableAttributes=cryptoCurrency.getTableAttributes(), data=recordsToInsert, dynamicInsertPlaceholders=cryptoCurrency.getDynamicInsertPlaceholders())

    print('Data inserted successfully!')



if __name__ == "__main__":
    main()