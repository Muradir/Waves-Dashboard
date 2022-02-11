#import modules
import emoji
from datetime import datetime
from twitter_tweets_by_cashtag import TwitterTweetsByCashTag

#import classes
from twitter_tweets_by_user import TwitterTweetsByUser
from twitter_users import TwitterUsers
from api_requests import ApiRequests
from database import Database
from waves_apy import WavesApy
from waves_market_prices import WavesMarketPrices

#get data from api call

#get twitter user data
data = ApiRequests.getData(url=TwitterUsers.url, headers=TwitterUsers.headers)['data']
Database.executeTruncateStatement(TwitterUsers.tableName)
Database.executeInsertStatement(TwitterUsers.tableName, data, TwitterUsers.tableAttributes, TwitterUsers.dynamicValues)

##get waves market price data
data = ApiRequests.getData(url=WavesMarketPrices.url, headers=WavesMarketPrices.headers)['data']
Database.executeTruncateStatement(WavesMarketPrices.tableName)
Database.executeInsertStatement(WavesMarketPrices.tableName, data, WavesMarketPrices.tableAttributes, WavesMarketPrices.dynamicValues)

##get waves apy data
data = ApiRequests.getData(url=WavesApy.url, headers=WavesApy.headers)['usdn-apy']
Database.executeTruncateStatement(WavesApy.tableName)
Database.executeInsertStatement(WavesApy.tableName, data, WavesApy.tableAttributes, WavesApy.dynamicValues)

#get twitter tweets by user
Database.executeTruncateStatement(tableName=TwitterTweetsByUser.tableName)
#twitterUserData = ApiRequests.getData(url=TwitterUsers.url, headers=TwitterUsers.headers)['data']
#twitterUserIds = []
#for user in twitterUserData:
#    twitterUserIds.append(user['id'])
#
#for userId in twitterUserIds:
#    baseUrlPerUserId = TwitterTweetsByUser.url + userId + '/tweets?tweet.fields=author_id,created_at&start_time=2021-01-01T00:00:00.000Z&max_results=100'
#    print(baseUrlPerUserId)
#    response = ApiRequests.getData(url=baseUrlPerUserId, headers=TwitterTweetsByUser.headers)
#    data = response['data']
#    nextToken = response['meta']['next_token']
#
#    while (nextToken != None):
#        for d in data:
#            d['text'] = emoji.demojize(d['text'])
#            
#        Database.executeInsertStatement(TwitterTweetsByUser.tableName, data, TwitterTweetsByUser.tableAttributes, TwitterTweetsByUser.dynamicValues)
#        response = ApiRequests.getData(url=baseUrlPerUserId + '&pagination_token=' + nextToken, headers=TwitterTweetsByUser.headers)
#        if len(response['meta']) == 5:
#            data = response['data']
#            nextToken = response['meta']['next_token']
#        else:
#            nextToken = None

#get twitter tweets by cashtag
response = ApiRequests.getData(url=TwitterTweetsByCashTag.baseUrl + TwitterTweetsByCashTag.initialRelativeUrl, headers=TwitterTweetsByCashTag.headers)
data = response['statuses']
nextRelativeUrl = response['search_metadata']['next_results']

while (nextRelativeUrl != None):
    for d in data:
        d['text'] = emoji.demojize(d['text'])
        d['author_id'] = d['user']['id']

    #print(data)

    Database.executeInsertStatement(TwitterTweetsByCashTag.tableName, data, TwitterTweetsByCashTag.tableAttributes, TwitterTweetsByCashTag.dynamicValues)
    response = ApiRequests.getData(url=TwitterTweetsByCashTag.baseUrl + nextRelativeUrl, headers=TwitterTweetsByCashTag.headers)
    print(len(response['search_metadata']))
    if len(response['search_metadata']) == 9:
        data = response['statuses']
        nextRelativeUrl = response['search_metadata']['next_results']
    else:
        nextRelativeUrl = None