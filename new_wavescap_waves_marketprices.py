class WavesMarketPrices:

    #private class attributes
    __url = 'https://wavescap.com/api/chart/asset/WAVES-usd-n-all.json'
    __headers = None
    __tableName = 'wavescap_marketPricesWavesToUsd'
    __tableAttributes = '(wavesMarketPrice_usd, date)'
    __dynamicInsertPlaceholders = '%s, %s'
    #__insertStatement = 'INSERT INTO '  + __tableName + ' (wavesMarketPrice_usd, date) VALUES (%s, %s);'

    
    ##__dataArrayName = 'data'
    ##__databaseTableAttributes = ['time', 'open', 'close', 'high', 'low', 'volume', 'quoteVolume', 'weightedAveragePrice', 'maxHeight', 'txsCount', 'timeClose', 'loadId']
    #__dynamicValues = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'

    #public class get methods
    def getUrl(self):
        return self.__url

    def getHeaders(self):
        return self.__headers

    def getInsertStatement(self):
        return self.__insertStatement

    def getTableName(self):
        return self.__tableName

    def getTableAttributes(self):
        return self.__tableAttributes

    def getDynamicInsertPlaceholders(self):
        return self.__dynamicInsertPlaceholders