#this is the root file of our backend service

#import internal classes
from api_requests import ApiRequests
from database import Database
from endpoints.wavescap_waves_usd import WavesUsdMarketPrices
from endpoints.wavescap_bitcoin_usd import BitcoinUsdMarketPrices

#import external modules
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

def main():
    database = Database()
    print("Wir schaffen das!")
    marketPricesUsd = []
    wavesUsdMarketPrices = WavesUsdMarketPrices()
    marketPricesUsd.append(wavesUsdMarketPrices)
    bitcoinUsdMarketPrices = BitcoinUsdMarketPrices()
    marketPricesUsd.append(bitcoinUsdMarketPrices)

    for item in marketPricesUsd:
        getMarketPricesData(database=database, apiEndpoint=item)
    #getMarketPrData(database=database)

def getMarketPricesData(database, apiEndpoint):
    response = ApiRequests.getDataByGetRequest(apiEndpoint.getUrl(), [])
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

    database.executeInsertStatement(tableName=apiEndpoint.getTableName(), tableAttributes=apiEndpoint.getTableAttributes(), data=recordsToInsert, dynamicInsertPlaceholders=apiEndpoint.getDynamicInsertPlaceholders())




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

    #print(recordsToInsert)



if __name__ == "__main__":
    main()