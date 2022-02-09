#import classes
from twitter_users import TwitterUsers
from api_requests import ApiRequests
from database import Database
from waves_market_prices import WavesMarketPrices

#get data from api call

#get twitter user data
data = ApiRequests.getData(url=TwitterUsers.url, headers=TwitterUsers.headers)
Database.executeInsertStatement(TwitterUsers.tableName, data, TwitterUsers.tableAttributes, TwitterUsers.dynamicValues)
Database.executeSelectQuery(TwitterUsers.tableName)

#get waves market price data
data = ApiRequests.getData(url=WavesMarketPrices.url, headers=WavesMarketPrices.headers)
print(data)
Database.executeInsertStatement(WavesMarketPrices.tableName, data, WavesMarketPrices.tableAttributes, WavesMarketPrices.dynamicValues)