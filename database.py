#import modules
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date

#import classes
from waves_market_prices import WavesMarketPrices

class Database:

    __userName = 'u122k7mhfbxvt0rp'
    __password = 'sYLq0OQvnWYw8Lv56bB6'
    __hostName = 'bp1o15l1iwoajeyerhf6-mysql.services.clever-cloud.com'
    __databaseName = 'bp1o15l1iwoajeyerhf6'

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
        connection = Database.__getDatabaseConnection()
        selectStatement = 'SELECT * FROM ' + tableName + ';'
        cursor = connection.cursor()
        cursor.execute(selectStatement)
        data = cursor.fetchall()
        self.__closeDatabaseConnection()
        return data


    def executeTruncateStatement(self, tableName):
        truncateStatement = 'TRUNCATE TABLE ' + tableName + ';'

        connection = self.__getDatabaseConnection()
        cursor = connection.cursor()
        cursor.execute(truncateStatement)
        self.__closeDatabaseConnection(cursor, connection)


    def callLoadIdProcedure(self, procedureParameters):
        connection = self.__getDatabaseConnection()
        cursor = connection.cursor()
        cursor.callproc('insert_loadid_control', procedureParameters)
        connection.commit()

        for result in cursor.stored_results():
            loadId = result.fetchall()
        loadId = loadId[0][0]
        
        self.__closeDatabaseConnection(cursor, connection)
        
        return loadId


    def callCoreProcessingProcedure(self, tableName, procedureName):
        loadId = self.callLoadIdProcedure([tableName, datetime.today()])

        connection = self.__getDatabaseConnection()
        cursor = connection.cursor()
        cursor.callproc(procedureName, [loadId])
        connection.commit()

        self.__closeDatabaseConnection(cursor, connection)


    def executeInsertStatement(self, tableName, data, loadId, tableAttributes, dynamicValues):
        print('begin insert')
        connection = self.__getDatabaseConnection()
        cursor = connection.cursor()
        
        newRecords = []
        insertStatement = 'INSERT INTO ' + tableName + ' VALUES (' + dynamicValues + ');'

        if isinstance(data, list):
            for item in data:
                if tableName == 'stage_waves_market_prices':
                    item = item['data']
                values = []
                for attribute in tableAttributes:
                    if attribute == 'dateOfToday':
                        values.append(date.today())
                    elif attribute == 'loadId':
                        values.append(loadId)
                    else:
                        values.append(item[attribute])
                
                newRecords.append(tuple(values))
        
        else:
            values = []
            for attribute in tableAttributes:
                if attribute == 'dateOfToday':
                    values.append(date.today().isoformat())
                elif attribute == 'loadId':
                    values.append(loadId)
                else:
                    values.append(data[attribute])
            
            newRecords.append(values)
        
        cursor.executemany(insertStatement, newRecords)
        connection.commit()
        self.__closeDatabaseConnection(cursor, connection)
