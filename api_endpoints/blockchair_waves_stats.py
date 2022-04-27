class WavesStats:

    #private class attributes
    __url = 'https://api.blockchair.com/ethereum/erc-20/0x1cf4592ebffd730c7dc92c1bdffdfc3b9efcf29a/stats'
    __tableName = 'blockchair_wavesDetails'
    __tableAttributes = '(transactions_total, transactions_24h, date)'
    __dynamicInsertPlaceholders = '%s, %s, %s'


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