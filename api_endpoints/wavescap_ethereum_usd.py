class EthereumUsdMarketPrices:

    #private class attributes
    __url = 'https://wavescap.com/api/chart/asset/474jTeYx2r2Va35794tCScAXWJG9hU2HcgxzMowaZUnu-usd-n-all.json'
    __tableName = 'wavescap_marketPricesEthereumToUsd'
    __tableAttributes = '(ethereumMarketPrice_usd, date)'
    __dynamicInsertPlaceholders = '%s, %s'


    #public class getter methods
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