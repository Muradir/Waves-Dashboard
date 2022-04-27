

#import external modules
import mysql.connector
from mysql.connector import Error

class Database:

    __userName = 'ugk98we9fog0mjs5'
    __password = 'XaP2f68yAjHBfVwNmrTn'
    __hostName = 'b7xzxkxarjooxxw9wkfi-mysql.services.clever-cloud.com'
    __databaseName = 'b7xzxkxarjooxxw9wkfi'

    def __getDatabaseConnection(self):
        try:
            connection = mysql.connector.connect(
                user = self.__userName,
                password = self.__password,
                host = self.__hostName, 
                database = self.__databaseName,
            )
            if connection.is_connected():
                return connection

        except Error as e:
            print("Error while connecting to MySQL", e)


    def __closeDatabaseConnection(self, connection):
        if connection.is_connected():
            connection.cursor().close()
            connection.close()


    def executeSelectQuery(self, tableName):
        selectStatement = 'SELECT * FROM ' + tableName + ';'

        connection = self.__getDatabaseConnection()
        cursor = connection.cursor()
        cursor.execute(selectStatement)
        data = cursor.fetchall()
        self.__closeDatabaseConnection(connection)
        return data

    def insertDataIntoDatabase(self, entity, recordsToInsert):
        self.__executeInsertStatement(tableName=entity.getTableName(), tableAttributes=entity.getTableAttributes(), data=recordsToInsert, dynamicInsertPlaceholders=entity.getDynamicInsertPlaceholders())

        print('Data of entity ' + entity.getTableName() + ' was inserted successfully into Database!')
        

    def __executeInsertStatement(self, tableName, tableAttributes, data, dynamicInsertPlaceholders):
        insertStatement = 'INSERT INTO ' + tableName + tableAttributes + ' VALUES (' + dynamicInsertPlaceholders + ');'

        self.__executeTruncateStatement(tableName=tableName)
        connection = self.__getDatabaseConnection()
        
        connection.cursor().executemany(insertStatement, data)
        connection.commit()
        self.__closeDatabaseConnection(connection)


    def __executeTruncateStatement(self, tableName):
        truncateStatement = 'TRUNCATE TABLE ' + tableName + ';'

        connection = self.__getDatabaseConnection()
        connection.cursor().execute(truncateStatement)
        self.__closeDatabaseConnection(connection)