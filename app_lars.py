#import modules
import requests
import mysql.connector
from mysql.connector import Error
from database import Database

#import classes
from twitter_users import TwitterUsers
from api_requests import ApiRequests

#get data from api call

#get twitter user data
userData = ApiRequests.getData(url=TwitterUsers.url, headers=TwitterUsers.headers)

new_records = []

for item in userData:
    list = []
    list.append(int(item['id']))
    list.append(item['username'])
    new_records.append(tuple(list))

Database.executeSelectQuery(TwitterUsers.tableName)
Database.executeTruncateStatement(TwitterUsers.tableName)
