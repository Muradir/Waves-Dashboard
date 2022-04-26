

#import external modules
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date

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


    def __closeDatabaseConnection(self, cursor, connection):
        if connection.is_connected():
            cursor.close()
            connection.close()


    def executeSelectQuery(self, tableName):
        connection = self.__getDatabaseConnection()
        selectStatement = 'SELECT * FROM ' + tableName + ';'
        cursor = connection.cursor()
        cursor.execute(selectStatement)
        data = cursor.fetchall()
        self.__closeDatabaseConnection(cursor, connection)
        return data
        

    def executeInsertStatement(self, tableName, tableAttributes, data, dynamicInsertPlaceholders):

        self.__executeTruncateStatement(tableName=tableName)
        connection = self.__getDatabaseConnection()
        cursor = connection.cursor()
        
        insertStatement = 'INSERT INTO ' + tableName + tableAttributes + ' VALUES (' + dynamicInsertPlaceholders + ');'
        #insertStatement = 'INSERT INTO ' + tableName + ' (wavesMarketPrice_bitcoin, date) VALUES (%s, %s);'

        cursor.executemany(insertStatement, data)
        connection.commit()
        self.__closeDatabaseConnection(cursor, connection)


    def __executeTruncateStatement(self, tableName):
        truncateStatement = 'TRUNCATE TABLE ' + tableName + ';'

        connection = self.__getDatabaseConnection()
        cursor = connection.cursor()
        cursor.execute(truncateStatement)
        self.__closeDatabaseConnection(cursor, connection)