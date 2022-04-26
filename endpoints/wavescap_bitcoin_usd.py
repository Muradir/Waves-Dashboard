class BitcoinUsdMarketPrices:

    #private class attributes
    __url = 'https://wavescap.com/api/chart/asset/8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS-usd-n-all.json'
    __headers = None
    __tableName = 'wavescap_marketPricesBitcoinToUsd'
    __tableAttributes = '(bitcoinMarketPrice_usd, date)'
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