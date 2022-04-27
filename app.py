#import internal classes
from api_requests import ApiRequests
from database import Database
from database import Database

#import external modules
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

from endpoints.wavescap_bitcoin_usd import BitcoinUsdMarketPrices



def main():
    database = Database()
    print("Wir schaffen das!")
    getMarketPricesData(database=database)
    #getMarketPrData(database=database)


def getMarketPricesData(database):
    cryptosToUsd = []
    bitcoToUsd = BitcoinUsdMarketPrices()
    cryptosToUsd.append(bitcoToUsd)

    for item in cryptosToUsd:
        getCryptoMarketPricesInUsd(database, item)



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
    

    print(recordsToInsert)

    database.executeInsertStatement(tableName=wavesMarketPrices.getTableName(), data=recordsToInsert, insertStatement=wavesMarketPrices.getInsertStatement())
    database.executeInsertStatement(tableName=wavesMarketPrices.getTableName(), tableAttributes=wavesMarketPrices.getTableAttributes(), data=recordsToInsert, dynamicInsertPlaceholders=wavesMarketPrices.getDynamicInsertPlaceholders())




def getMarketPrData(database):
    
    url_waves_to_bitcoin = "https://wavescap.com/api/chart/pair/WAVES-8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS-all.json"
    response = ApiRequests.getDataByGetRequest(url_waves_to_bitcoin, [])
    marketPrices = response['data']
    recordsToInsert = []
    for item in marketPrices:
        attributes = []
        attributes.append(item['data']['weightedAveragePrice'])
        startTime = item['data']['time'][:10]
        startTime = date.fromisoformat(startTime)
        attributes.append(startTime)
        
        recordsToInsert.append(tuple(attributes))
    database.executeInsertStatement(tableName='wavescap_marketPricesWavesToBitcoin', data=recordsToInsert)



if __name__ == "__main__":
    main()