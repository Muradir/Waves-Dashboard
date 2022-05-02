#Author: Lars Brebeck
#Description: This file holds all important information about an api-endpoint and makes them accessible via public getter methods

class BitcoinUsdMarketPrices:

    #private class attributes
    __url = 'https://wavescap.com/api/chart/asset/8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS-usd-n-all.json'
    __dbTableName = 'wavescap_marketPricesBitcoinToUsd'
    __dbTableAttributes = '(bitcoinMarketPrice_usd, date)'
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