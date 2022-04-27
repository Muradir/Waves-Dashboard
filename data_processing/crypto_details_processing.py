#import internal classes
from data_stores.database import Database
from api_endpoints.blockchair_bitcoin_stats import BitcoinStats
from api_endpoints.blockchair_ethereum_stats import EthereumStats
from api_endpoints.blockchair_waves_stats import WavesStats
#import external modules
from datetime import datetime
import requests


class CryptoStatsDataProcessing:
    
    #public class method, initiates the data processing workflow by invoking private class methods
    def start(self):
        blockchains = [BitcoinStats(), EthereumStats()]
        for item in blockchains:
            self.__getBlockchainStats(blockchain=item)

        self.__getCryptoStats(cryptoCurrency=WavesStats())


    #private class method, gets data via api request and initiates the database insertion
    def __getCryptoStats(self, cryptoCurrency):
        response = requests.get(url = cryptoCurrency.getUrl()).json()
        cryptoStats = response['data']

        attributes = [cryptoStats['transactions'], cryptoStats['transactions_24h'], datetime.today().date()]
        recordsToInsert = [tuple(attributes)]

        Database().insertDataIntoDatabase(entity=cryptoCurrency, recordsToInsert=recordsToInsert)


    #private class method, gets data via api request and initiates the database insertion
    def __getBlockchainStats(self, blockchain):
        response = requests.get(url = blockchain.getUrl()).json()
        cryptoStats = response['data']

        attributes = [cryptoStats['transactions'], cryptoStats['transactions_24h'], cryptoStats['average_transaction_fee_usd_24h'], cryptoStats['market_price_usd_change_24h_percentage'], cryptoStats['market_dominance_percentage']]
        recordsToInsert = [tuple(attributes)]

        Database().insertDataIntoDatabase(entity=blockchain, recordsToInsert=recordsToInsert)