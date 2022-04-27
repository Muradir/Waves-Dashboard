#import internal classes
from api_requests import ApiRequests
from database import Database
from database import Database

#import external modules
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from decimal import Decimal
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


def main():
    database = Database()
    print("Wir schaffen das!")
    getMarketPricesData(database=database)
    getCryptoDetailsData(database=database)


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

    sp500ToUsd = SP500UsdMarketPrices()
    getFundMarketPricesInUsd(database, sp500ToUsd)


def getCryptoDetailsData(database):
    bitcoinStats = BitcoinStats()
    ethereumStats = EthereumStats()
    blockchains = [bitcoinStats, ethereumStats]

    for item in blockchains:
        getBlockchainStats(database=database, blockchain=item)

    wavesStats = WavesStats()
    getCryptoStats(database=database, cryptoCurrency=wavesStats)


def getCryptoStats(database, cryptoCurrency):
    response = ApiRequests.getDataByGetRequest(cryptoCurrency.getUrl(), [])
    cryptoStats = response['data']

    recordsToInsert = []
    attributes = [cryptoStats['transactions'], cryptoStats['transactions_24h'], datetime.today().date()]
    recordsToInsert.append(tuple(attributes))

    print(recordsToInsert)

    database.executeInsertStatement(tableName=cryptoCurrency.getTableName(), tableAttributes=cryptoCurrency.getTableAttributes(), data=recordsToInsert, dynamicInsertPlaceholders=cryptoCurrency.getDynamicInsertPlaceholders())

    print('Data inserted successfully!')



def getBlockchainStats(database, blockchain):
    response = ApiRequests.getDataByGetRequest(blockchain.getUrl(), [])
    cryptoStats = response['data']

    recordsToInsert = []
    attributes = []
    attributes.append(cryptoStats['transactions'])
    attributes.append(cryptoStats['transactions_24h'])
    attributes.append(cryptoStats['average_transaction_fee_usd_24h'])
    attributes.append(cryptoStats['market_price_usd_change_24h_percentage'])
    attributes.append(cryptoStats['market_dominance_percentage'])
    recordsToInsert.append(tuple(attributes))

    print(recordsToInsert)

    database.executeInsertStatement(tableName=blockchain.getTableName(), tableAttributes=blockchain.getTableAttributes(), data=recordsToInsert, dynamicInsertPlaceholders=blockchain.getDynamicInsertPlaceholders())

    print('Data inserted successfully!')




def getFundMarketPricesInUsd(database, indexFund):
    response = ApiRequests.getDataByGetRequest(indexFund.getUrl(), [])
    marketPrices = response['observations']

    recordsToInsert = []
    for item in marketPrices:
        attributes = []
        if(item['value']) != '.':
            attributes.append(Decimal(item['value']))
            attributes.append(date.fromisoformat(item['date']))
            recordsToInsert.append(tuple(attributes))

    print(recordsToInsert)

    database.executeInsertStatement(tableName=indexFund.getTableName(), tableAttributes=indexFund.getTableAttributes(), data=recordsToInsert, dynamicInsertPlaceholders=indexFund.getDynamicInsertPlaceholders())

    print('Data inserted successfully!')


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