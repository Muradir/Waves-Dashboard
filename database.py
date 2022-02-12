#import modules
from json import load
from ntpath import join
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date

#import classes
from waves_market_prices import WavesMarketPrices

class Database:

    userName = 'u122k7mhfbxvt0rp'
    password = 'sYLq0OQvnWYw8Lv56bB6'
    hostName = 'bp1o15l1iwoajeyerhf6-mysql.services.clever-cloud.com'
    databaseName = 'bp1o15l1iwoajeyerhf6'

    def getDatabaseConnection():
        try:
            connection = mysql.connector.connect(
                user = Database.userName,
                password = Database.password,
                host = Database.hostName, 
                database = Database.databaseName,
            )

            if connection.is_connected():
                print(connection)
                return connection

        except Error as e:
            print("Error while connecting to MySQL", e)

    def closeDatabaseConnection(cursor, connection):
        if connection.is_connected():
            cursor.close()
            connection.close()

    
    def executeSelectQuery(tableName):
        connection = Database.getDatabaseConnection()
        selectStatement = 'SELECT * FROM ' + tableName + ';'
        cursor = connection.cursor()
        cursor.execute(selectStatement)
        data = cursor.fetchall()
        Database.closeDatabaseConnection
        return data


    def executeTruncateStatement(tableName):
        truncateStatement = 'TRUNCATE TABLE ' + tableName + ';'

        connection = Database.getDatabaseConnection()
        cursor = connection.cursor()
        cursor.execute(truncateStatement)
        Database.closeDatabaseConnection(cursor, connection)


    def callLoadIdProcedure(procedureParameters):
        connection = Database.getDatabaseConnection()
        cursor = connection.cursor()
        cursor.callproc('insert_loadid_control', procedureParameters)
        connection.commit()

        for result in cursor.stored_results():
            loadId = result.fetchall()
        loadId = loadId[0][0]
        
        Database.closeDatabaseConnection(cursor, connection)
        
        return loadId


    def callCoreProcessingProcedure(tableName, procedureName):
        loadId = Database.callLoadIdProcedure([tableName, datetime.today()])

        connection = Database.getDatabaseConnection()
        cursor = connection.cursor()
        cursor.callproc(procedureName, [loadId])
        connection.commit()

        Database.closeDatabaseConnection(cursor, connection)


    def executeInsertStatement(tableName, data, loadId, tableAttributes, dynamicValues):

        #print(dynamicValues)
        connection = Database.getDatabaseConnection()
        cursor = connection.cursor()
        #Database.executeTruncateStatement(tableName, cursor)
        
        newRecords = []
        insertStatement = 'INSERT INTO ' + tableName + ' VALUES (' + dynamicValues + ');'

        if isinstance(data, list):
            print('isList')
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
        
            #cursor.executemany(insertStatement, newRecords)
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
        
        print(newRecords)
        cursor.executemany(insertStatement, newRecords)
        connection.commit()
        Database.closeDatabaseConnection(cursor, connection)

            #if cn.is_connected():
    #        #    print(cn.get_server_info())
    #        #    cs = cn.cursor()
    #        #    #cs.execute()
    #        #    print(cs)
    #        #    cs.execute(operation="select database();")
    #        #    rows = cs.fetchall()
    #        #    print(rows)
    #        #    cs.execute(operation="select * from test;")
    #        #    tableData = cs.fetchall()
    #        #    print(tableData)
    #        #    cs.executemany(insert_statement, new_records)
    #        #    cn.commit()
    #        #    print(cs.rowcount)
