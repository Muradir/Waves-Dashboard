class WavesBitcoinMarketPrices:

    #private class attributes
    __url = 'https://wavescap.com/api/chart/pair/WAVES-8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS-all.json'
    __dbTableName = 'wavescap_marketPricesWavesToBitcoin'
    __dbTableAttributes = '(wavesMarketPrice_bitcoin, date)'
    __dbDynamicInsertPlaceholders = '%s, %s'


    #public class getter methods
    def getUrl(self):
        return self.__url

    def getDbTableName(self):
        return self.__dbTableName

    def getDbTableAttributes(self):
        return self.__dbTableAttributes

    def getDbDynamicInsertPlaceholders(self):
        return self.__dbDynamicInsertPlaceholders