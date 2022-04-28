class WavesStats:

    #private class attributes
    __url = 'https://api.blockchair.com/ethereum/erc-20/0x1cf4592ebffd730c7dc92c1bdffdfc3b9efcf29a/stats'
    __dbTableName = 'blockchair_wavesDetails'
    __dbTableAttributes = '(transactions_total, transactions_24h, date)'
    __dbDynamicInsertPlaceholders = '%s, %s, %s'


    #public class getter methods
    def getUrl(self):
        return self.__url

    def getDbTableName(self):
        return self.__dbTableName

    def getDbTableAttributes(self):
        return self.__dbTableAttributes

    def getDbDynamicInsertPlaceholders(self):
        return self.__dbDynamicInsertPlaceholders