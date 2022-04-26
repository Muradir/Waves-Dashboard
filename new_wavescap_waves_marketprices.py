class WavesMarketPrices:

    #private class attributes
    __url = 'https://wavescap.com/api/chart/asset/WAVES-usd-n-all.json'
    __headers = None
    __tableName = 'wavescap_marketPricesWavesToUsd'
    __tableAttributes = '(wavesMarketPrice_usd, date)'
    __dynamicInsertPlaceholders = '%s, %s'
    __insertStatement = 'INSERT INTO '  + __tableName + ' (wavesMarketPrice_usd, date) VALUES (%s, %s);'

    
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

    def getDataArrayName(self):
        return self.__dataArrayName

    def getDatabaseObjectName(self):
        return self.__databaseObjectName

    def getDatabaseTableAttributes(self):
        return self.__databaseTableAttributes

    def getDatabaseProcedureName(self):
        return 'load_core_' + self.__databaseObjectName

    def getDynamicValues(self):
        return self.__dynamicValues