#Author: Lars Brebeck
#Description: This file holds information about the table "test_table" inside the database, that is created for testing the database functionality

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