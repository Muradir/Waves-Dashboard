#import modules
from pickle import TRUE
import emoji
from datetime import datetime
from market_treasury_yield import MarketTreasuryYield
from twitter_sentiment_analysis import TwitterSentimentAnalysis
from twitter_tweets_by_cashtag import TwitterTweetsByCashTag

#import classes
from twitter_tweets_by_user import TwitterTweetsByUser
from twitter_users import TwitterUsers
from api_requests import ApiRequests
from database import Database
from waves_apy import WavesApy
from waves_market_prices import WavesMarketPrices

from datetime import date, datetime
from dateutil.relativedelta import relativedelta



def main():
    #get timeStart for all time relative api requests
    timeStart = (datetime.today() - relativedelta(years=1)).date()
    loadMarketTreasuryYieldData(timeStart=timeStart)
    loadWavesMarketPrices(timeStart=timeStart)


def getDatabaseObjectName(name, databaseLayer, isProcedure):
    if isProcedure:
        return 'load_core_' + name
    else:
        return databaseLayer + '_' + name


def loadMarketTreasuryYieldData(timeStart):
    #get treasury yield data
    data = ApiRequests.getDataByGetRequest(url=MarketTreasuryYield.baseUrl + str(timeStart), headers=MarketTreasuryYield.headers)['observations']
    #database handling
    Database.executeTruncateStatement(tableName=getDatabaseObjectName(MarketTreasuryYield.name, 'stage', False))
    loadId = Database.callLoadIdProcedure(procedureParameters=[MarketTreasuryYield.name, datetime.today()])
    Database.executeInsertStatement(tableName=getDatabaseObjectName(MarketTreasuryYield.name, 'stage', False), data=data, loadId=loadId, tableAttributes=MarketTreasuryYield.tableAttributes, dynamicValues=MarketTreasuryYield.dynamicValues)
    Database.callCoreProcessingProcedure(tableName=getDatabaseObjectName(MarketTreasuryYield.name, 'core', False), procedureName=getDatabaseObjectName(MarketTreasuryYield.name, 'core', True))


def loadWavesMarketPrices(timeStart):
    #get waves market price data
    data = ApiRequests.getDataByGetRequest(url=WavesMarketPrices.baseUrl + str(timeStart), headers=WavesMarketPrices.headers)['data']
    #database handling
    Database.executeTruncateStatement(tableName=getDatabaseObjectName(WavesMarketPrices.name, 'stage', False))
    loadId = Database.callLoadIdProcedure(procedureParameters=[WavesMarketPrices.name, datetime.today()])
    Database.executeInsertStatement(tableName=getDatabaseObjectName(WavesMarketPrices.name, 'stage', False), data=data, loadId=loadId, tableAttributes=WavesMarketPrices.tableAttributes, dynamicValues=WavesMarketPrices.dynamicValues)
    Database.callCoreProcessingProcedure(tableName=getDatabaseObjectName(MarketTreasuryYield.name, 'core', False), procedureName=getDatabaseObjectName(WavesMarketPrices.name, 'core', True))


if __name__ == "__main__":
    main()

    #get twitter user data
    #data = ApiRequests.getData(url=TwitterUsers.url, headers=TwitterUsers.headers)['data']
    #Database.executeTruncateStatement(TwitterUsers.tableName)
    #Database.executeInsertStatement(TwitterUsers.tableName, data, TwitterUsers.tableAttributes, TwitterUsers.dynamicValues)

    ###get waves apy data
    #data = ApiRequests.getData(url=WavesApy.url, headers=WavesApy.headers)['usdn-apy']
    #Database.executeTruncateStatement(WavesApy.tableName)
    #Database.executeInsertStatement(WavesApy.tableName, data, WavesApy.tableAttributes, WavesApy.dynamicValues)
    #
    ##get twitter tweets by user
    #Database.executeTruncateStatement(tableName=TwitterTweetsByUser.tableName)
    #twitterUserData = ApiRequests.getData(url=TwitterUsers.baseUrl, headers=TwitterUsers.headers)['data']
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
    #
    ##get twitter tweets by cashtag
    #response = ApiRequests.getData(url=TwitterTweetsByCashTag.baseUrl + TwitterTweetsByCashTag.initialRelativeUrl, headers=TwitterTweetsByCashTag.headers)
    #data = response['statuses']
    #nextRelativeUrl = response['search_metadata']['next_results']
    #
    #while (nextRelativeUrl != None):
    #    for d in data:
    #        d['text'] = emoji.demojize(d['text'])
    #        d['author_id'] = d['user']['id']
    #
    #    Database.executeInsertStatement(TwitterTweetsByCashTag.tableName, data, TwitterTweetsByCashTag.tableAttributes, TwitterTweetsByCashTag.dynamicValues)
    #    response = ApiRequests.getData(url=TwitterTweetsByCashTag.baseUrl + nextRelativeUrl, headers=TwitterTweetsByCashTag.headers)
    # 
    #    if len(response['search_metadata']) == 9:
    #        data = response['statuses']
    #        nextRelativeUrl = response['search_metadata']['next_results']
    #    else:
    #        nextRelativeUrl = None

    #get data of tweet sentiment analysis
    #Database.executeTruncateStatement(TwitterSentimentAnalysis.tableName)
    #loadId = Database.callLoadIdStoredProcedure([TwitterSentimentAnalysis.tableName, datetime.today()])
    #tweets = Database.executeSelectQuery(tableName='report_twitter_tweets')
    #
    #newRecords = []
    #for tweet in tweets:
    #    data = ApiRequests.getDataByPostRequest(url=TwitterSentimentAnalysis.url, body={'text' : tweet[1]})
    #    scores = data['probability']
    #    data['tweetId'] = tweet[0]
    #    data['neg'] = scores['neg']
    #    data['pos'] = scores['pos']
    #    data['loadId'] = loadId
    #    newRecords.append(data)
    #    print(len(newRecords))
    #Database.executeInsertStatement(TwitterSentimentAnalysis.tableName, newRecords, TwitterSentimentAnalysis.tableAttributes, TwitterSentimentAnalysis.dynamicValues)