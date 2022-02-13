
class WavesMarketPrices:

    #private class attributes
    __baseUrl = 'https://api.wavesplatform.com/v0/candles/WAVES/DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p?interval=1d&timeStart='
    __headers = None
    __dataArrayName = 'data'
    __databaseObjectName = 'waves_market_prices'
    __databaseTableAttributes = ['time', 'open', 'close', 'high', 'low', 'volume', 'quoteVolume', 'weightedAveragePrice', 'maxHeight', 'txsCount', 'timeClose', 'loadId']
    __dynamicValues = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'

    #public class get methods
    def getUrl(self, timeStart):
        return self.__baseUrl + timeStart

    def getHeaders(self):
        return self.__headers

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