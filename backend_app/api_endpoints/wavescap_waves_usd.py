class WavesUsdMarketPrices:

    #private class attributes
    __url = 'https://wavescap.com/api/chart/asset/WAVES-usd-n-all.json'
    __dbTableName = 'wavescap_marketPricesWavesToUsd'
    __dbTableAttributes = '(wavesMarketPrice_usd, date)'
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