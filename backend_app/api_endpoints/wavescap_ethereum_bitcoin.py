class EthereumBitcoinMarketPrices:

    #private class attributes
    __url = 'https://wavescap.com/api/chart/pair/474jTeYx2r2Va35794tCScAXWJG9hU2HcgxzMowaZUnu-8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS-all.json'
    __dbTableName = 'wavescap_marketPricesEthereumToBitcoin'
    __dbTableAttributes = '(ethereumMarketPrice_bitcoin, date)'
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