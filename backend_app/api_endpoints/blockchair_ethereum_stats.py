class EthereumStats:

    #private class attributes
    __url = 'https://api.blockchair.com/ethereum/stats'
    __dbTableName = 'blockchair_ethereumDetails'
    __dbTableAttributes = '(transactions_total, transactions_24h, averageTransactionFee_24h_usd, marketPriceChangePercentage_24h_usd, marketDominancePercentage)'
    __dbDynamicInsertPlaceholders = '%s, %s, %s, %s, %s'


    #public class getter methods
    def getUrl(self):
        return self.__url

    def getDbTableName(self):
        return self.__dbTableName

    def getDbTableAttributes(self):
        return self.__dbTableAttributes

    def getDbDynamicInsertPlaceholders(self):
        return self.__dbDynamicInsertPlaceholders