class BitcoinStats:

    #private class attributes
    __url = 'https://api.blockchair.com/bitcoin/stats'
    __dbTableName = 'blockchair_bitcoinDetails'
    __dbTableAttributes = '(transactions_total, transactions_24h, averageTransactionFee_24h_usd, marketPriceChangePercentage_24h_usd, marketDominancePercentage, date)'
    __dbDynamicInsertPlaceholders = '%s, %s, %s, %s, %s, %s'


    #public class getter methods
    def getUrl(self):
        return self.__url

    def getDbTableName(self):
        return self.__dbTableName

    def getDbTableAttributes(self):
        return self.__dbTableAttributes

    def getDbDynamicInsertPlaceholders(self):
        return self.__dbDynamicInsertPlaceholders