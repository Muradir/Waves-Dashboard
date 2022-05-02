#Author: Lars Brebeck
#Description: This file holds all important information about an api-endpoint and makes them accessible via public getter methods

class EthereumWavesMarketPrices:

    #private class attributes
    __url = 'https://wavescap.com/api/chart/pair/474jTeYx2r2Va35794tCScAXWJG9hU2HcgxzMowaZUnu-WAVES-all.json'
    __dbTableName = 'wavescap_marketPricesEthereumToWaves'
    __dbTableAttributes = '(ethereumMarketPrice_waves, date)'
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