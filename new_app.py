#this is the root file of our backend service

#import internal classes
from mysqlx import InsertStatement
from api_requests import ApiRequests
from database import Database
from new_wavescap_waves_marketprices import WavesMarketPrices

#import external modules
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

def main():
    database = Database()
    print("Wir schaffen das!")
    getMarketPricesData(database=database)
    #getMarketPrData(database=database)

def getMarketPricesData(database):
    wavesMarketPrices = WavesMarketPrices()
    #url_waves_to_usd = "https://wavescap.com/api/chart/asset/WAVES-usd-n-all.json"
    response = ApiRequests.getDataByGetRequest(wavesMarketPrices.getUrl(), [])
    marketPrices = response['data']
    startTime = response['start'][:10]
    print(startTime)
    print(type(startTime))
    startTime = date.fromisoformat(startTime)
    print(startTime)
    print(type(startTime))
    print(marketPrices)
    recordsToInsert = []

    for item in marketPrices:
        item.pop()
        startTime = startTime + relativedelta(days=1)
        item.append(startTime)
        recordsToInsert.append(tuple(item))

    
    
    print(recordsToInsert)

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

    #print(recordsToInsert)



if __name__ == "__main__":
    main()