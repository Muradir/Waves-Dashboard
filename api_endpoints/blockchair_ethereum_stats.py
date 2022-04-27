class EthereumStats:

    #private class attributes
    __url = 'https://api.blockchair.com/ethereum/stats'
    __headers = None
    __tableName = 'blockchair_ethereumDetails'
    __tableAttributes = '(transactions_total, transactions_24h, averageTransactionFee_24h_usd, marketPriceChangePercentage_24h_usd, marketDominancePercentage)'
    __dynamicInsertPlaceholders = '%s, %s, %s, %s, %s'

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