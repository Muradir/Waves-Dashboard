class EthereumWavesMarketPrices:

    #private class attributes
    __url = 'https://wavescap.com/api/chart/pair/474jTeYx2r2Va35794tCScAXWJG9hU2HcgxzMowaZUnu-WAVES-all.json'
    __headers = None
    __tableName = 'wavescap_marketPricesEthereumToWaves'
    __tableAttributes = '(ethereumMarketPrice_waves, date)'
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