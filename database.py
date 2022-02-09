#import modules
import mysql.connector
from mysql.connector import Error

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
        selectStatement = 'SELECT * FROM ' + tableName
        cursor = connection.cursor()
        cursor.execute(selectStatement)
        records = cursor.fetchmany(3)
        print(records)
        Database.closeDatabaseConnection

    def executeTruncateStatement(tableName):
        connection = Database.getDatabaseConnection()
        truncateStatement = 'TRUNCATE TABLE ' + tableName
        cursor = connection.cursor()
        cursor.execute(truncateStatement)


    #def executeInsertStatement(tableName, data):
    #    #db = cn.database
    #        #insert_statement = """INSERT INTO twitter_users (userId, userName) VALUES (%s, %s)"""
    #        ##new_records = 
##
    #        #if cn.is_connected():
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
