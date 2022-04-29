print('accessed DB')

#import external modules
import mysql.connector
from mysql.connector import Error

class Database:

    #private class attributes, needed for database authentication
    __userName = 'ugk98we9fog0mjs5'
    __password = 'XaP2f68yAjHBfVwNmrTn'
    __hostName = 'b7xzxkxarjooxxw9wkfi-mysql.services.clever-cloud.com'
    __databaseName = 'b7xzxkxarjooxxw9wkfi'


    #public class method, extracts the whole dataset from a specific table of the database
    def executeSelectQuery(self, tableName):
        selectStatement = 'SELECT * FROM ' + tableName + ';'

        connection = self.__getDatabaseConnection()
        cursor = connection.cursor()
        cursor.execute(selectStatement)
        data = cursor.fetchall()
        self.__closeDatabaseConnection(connection)
        return data


    #public class method, initiates data insertion to a specific table of the database
    def insertDataIntoDatabase(self, entity, recordsToInsert):
        self.__executeInsertStatement(tableName=entity.getDbTableName(), tableAttributes=entity.getDbTableAttributes(), data=recordsToInsert, dynamicInsertPlaceholders=entity.getDbDynamicInsertPlaceholders())

        print('Data of entity ' + entity.getDbTableName() + ' was inserted successfully into Database!')
        return 'Data of entity ' + entity.getDbTableName() + ' was inserted successfully into Database!'


    #private class methods, creates a connection to the database
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


    #private class method, closes an existing connection to the database
    def __closeDatabaseConnection(self, connection):
        if connection.is_connected():
            connection.cursor().close()
            connection.close()
        

    #private class method, inserts data into a specific table of the database
    def __executeInsertStatement(self, tableName, tableAttributes, data, dynamicInsertPlaceholders):
        insertStatement = 'INSERT INTO ' + tableName + tableAttributes + ' VALUES (' + dynamicInsertPlaceholders + ');'

        self.__executeTruncateStatement(tableName=tableName)
        connection = self.__getDatabaseConnection()
        
        connection.cursor().executemany(insertStatement, data)
        connection.commit()
        self.__closeDatabaseConnection(connection)


    #private class method, deletes all data from a specific table, is invoked before every data insertion
    def __executeTruncateStatement(self, tableName):
        truncateStatement = 'TRUNCATE TABLE ' + tableName + ';'

        connection = self.__getDatabaseConnection()
        connection.cursor().execute(truncateStatement)
        self.__closeDatabaseConnection(connection)