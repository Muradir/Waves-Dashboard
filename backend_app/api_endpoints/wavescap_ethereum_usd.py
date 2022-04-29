class EthereumUsdMarketPrices:

    #private class attributes
    __url = 'https://wavescap.com/api/chart/asset/474jTeYx2r2Va35794tCScAXWJG9hU2HcgxzMowaZUnu-usd-n-all.json'
    __dbTableName = 'wavescap_marketPricesEthereumToUsd'
    __dbTableAttributes = '(ethereumMarketPrice_usd, date)'
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