class WavesBitcoinMarketPrices:

    #private class attributes
    __url = "https://wavescap.com/api/chart/pair/WAVES-8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS-all.json"
    __headers = None
    __tableName = 'wavescap_marketPricesWavesToBitcoin'
    __tableAttributes = '(wavesMarketPrice_bitcoin, date)'
    __dynamicInsertPlaceholders = '%s, %s'

    #public class get methods
    def getUrl(self):
        return self.__url

    def getHeaders(self):
        return self.__headers

    def getTableName(self):
        return self.__tableName

    def getTableAttributes(self):
        return self.__tableAttributes

    def getDynamicInsertPlaceholders(self):
        return self.__dynamicInsertPlaceholders