print('accessed CryptoStatsDP')
#import external modules
from datetime import datetime
import requests
import sys, os

testdir = os.path.dirname(__file__)
srcdir = '../api_endpoints'
sys.path.insert(1, os.path.abspath(os.path.join(testdir, srcdir)))
testdir2 = os.path.dirname(__file__)
srcdir2 = '../data_stores'
sys.path.insert(0, os.path.abspath(os.path.join(testdir2, srcdir2)))
print(sys.path)

#import internal classes
from database import Database
from blockchair_bitcoin_stats import BitcoinStats
from blockchair_ethereum_stats import EthereumStats
from blockchair_waves_stats import WavesStats

class CryptoStatsDataProcessing:
    
    #public class method, initiates the data processing workflow by invoking private class methods
    def start(self):
        blockchains = [BitcoinStats(), EthereumStats()]
        for item in blockchains:
            self.__getBlockchainStats(blockchain=item)

        self.__getCryptoStats(cryptoCurrency=WavesStats())
        return 'Crypto Stats Data Loaded'


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