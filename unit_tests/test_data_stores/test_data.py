class TestData:

    #private class attributes
    __dbTableName = 'test_table'
    __dbTableAttributes = '(testId, testString)'
    __dbDynamicInsertPlaceholders = '%s, %s'


    #public class getter methods
    def getDbTableName(self):
        return self.__dbTableName

    def getDbTableAttributes(self):
        return self.__dbTableAttributes

    def getDbDynamicInsertPlaceholders(self):
        return self.__dbDynamicInsertPlaceholders