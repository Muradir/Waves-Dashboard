#import modules
import emoji
from datetime import datetime
from dateutil.relativedelta import relativedelta

#import classes
from twitter_tweets_by_user import TwitterTweetsByUser
from twitter_users import TwitterUsers
from api_requests import ApiRequests
from database import Database
from waves_apy import WavesApy
from waves_market_prices import WavesMarketPrices
from market_treasury_yield import MarketTreasuryYield
from twitter_sentiment_analysis import TwitterSentimentAnalysis
from twitter_tweets_by_cashtag import TwitterTweetsByCashTag


def main():
    #database attribute
    database = Database()

    #get timeStart for all time relative api requests
    timeStart = (datetime.today() - relativedelta(years=1)).date()

    #call data load methods
    loadTwitterSentimentAnalysisData(database=database)
    print('start')
    loadTwitterTweetsByCashtag(database=database)
    print(1)
    loadTwitterTweetsByUser(database=database)
    print(2)
    loadMarketTreasuryYieldData(timeStart=timeStart, database=database)
    print(3)
    loadWavesMarketPrices(timeStart=timeStart, database=database)
    print(4)
    loadWavesApyData(database=database)
    print(5)


def getDatabaseTableName(databaseLayer, databaseObjectName):
    return databaseLayer + '_' + databaseObjectName


def loadMarketTreasuryYieldData(timeStart, database):
    marketTreasuryYield = MarketTreasuryYield()
    stageTableName = getDatabaseTableName('stage', marketTreasuryYield.getDatabaseObjectName())
    coreTableName = getDatabaseTableName('core', marketTreasuryYield.getDatabaseObjectName())

    #get treasury yield data
    data = ApiRequests.getDataByGetRequest(url=marketTreasuryYield.getUrl(timeStart=str(timeStart)), headers=marketTreasuryYield.getHeaders())['observations']

    #database handling
    database.executeTruncateStatement(tableName=stageTableName)
    loadId = database.callLoadIdProcedure(procedureParameters=[stageTableName, datetime.today()])
    database.executeInsertStatement(tableName=stageTableName, data=data, loadId=loadId, tableAttributes=marketTreasuryYield.getDatabaseTableAttributes(), dynamicValues=marketTreasuryYield.getDynamicValues())
    database.callCoreProcessingProcedure(tableName=coreTableName, procedureName=marketTreasuryYield.getDatabaseProcedureName())


def loadWavesMarketPrices(timeStart, database):
    wavesMarketPrices = WavesMarketPrices()
    stageTableName = getDatabaseTableName('stage', wavesMarketPrices.getDatabaseObjectName())
    coreTableName = getDatabaseTableName('core', wavesMarketPrices.getDatabaseObjectName())

    #get waves market price data
    data = ApiRequests.getDataByGetRequest(url=wavesMarketPrices.getUrl(timeStart=str(timeStart)), headers=wavesMarketPrices.getHeaders())['data']
    
    #database handling
    database.executeTruncateStatement(tableName=stageTableName)
    loadId = database.callLoadIdProcedure(procedureParameters=[stageTableName, datetime.today()])
    database.executeInsertStatement(stageTableName, data=data, loadId=loadId, tableAttributes=wavesMarketPrices.getDatabaseTableAttributes(), dynamicValues=wavesMarketPrices.getDynamicValues())
    database.callCoreProcessingProcedure(tableName=coreTableName, procedureName=wavesMarketPrices.getDatabaseProcedureName())


def loadWavesApyData(database):
    wavesApy = WavesApy()
    stageTableName = getDatabaseTableName('stage', wavesApy.getDatabaseObjectName())
    coreTableName = getDatabaseTableName('core', wavesApy.getDatabaseObjectName())

    #get waves market price data
    data = ApiRequests.getDataByGetRequest(url=wavesApy.getUrl(), headers=wavesApy.getHeaders())[wavesApy.getDataArrayName()]

    #database handling
    database.executeTruncateStatement(tableName=stageTableName)
    loadId = database.callLoadIdProcedure(procedureParameters=[stageTableName, datetime.today()])
    database.executeInsertStatement(stageTableName, data=data, loadId=loadId, tableAttributes=wavesApy.getDatabaseTableAttributes(), dynamicValues=wavesApy.getDynamicValues())
    database.callCoreProcessingProcedure(tableName=coreTableName, procedureName=wavesApy.getDatabaseProcedureName())


def loadTwitterTweetsByUser(database):
    twitterUsers = TwitterUsers()
    twitterTweetsByUser = TwitterTweetsByUser()
    stageTableName = getDatabaseTableName('stage', twitterTweetsByUser.getDatabaseObjectName())
    coreTableName = getDatabaseTableName('core', twitterTweetsByUser.getDatabaseObjectName())
    
    #get twitter (waves)user data
    twitterUserData = ApiRequests.getDataByGetRequest(url=twitterUsers.getUrl(), headers=twitterUsers.getHeaders())[twitterUsers.getDataArrayName()]
    twitterUserIds = []

    for user in twitterUserData:
        twitterUserIds.append(user['id'])

    database.executeTruncateStatement(tableName=stageTableName)
    loadId = database.callLoadIdProcedure(procedureParameters=[stageTableName, datetime.today()])

    #get twitter tweets by user
    for userId in twitterUserIds:
        urlPerUserId = twitterTweetsByUser.getUrl(str(userId) + '/tweets?tweet.fields=author_id,created_at&start_time=2021-01-01T00:00:00.000Z&max_results=100')

        response = ApiRequests.getDataByGetRequest(url=urlPerUserId, headers=twitterTweetsByUser.getHeaders())
        data = response[twitterTweetsByUser.getDataArrayName()]
        nextToken = response['meta']['next_token']
    
        while (nextToken != None):
            for d in data:
                d['text'] = emoji.demojize(d['text'])
                
            database.executeInsertStatement(tableName=stageTableName, data=data, loadId=loadId, tableAttributes=twitterTweetsByUser.getDatabaseTableAttributes(), dynamicValues=twitterTweetsByUser.getDynamicValues())
            response = ApiRequests.getDataByGetRequest(url=urlPerUserId + '&pagination_token=' + nextToken, headers=twitterTweetsByUser.getHeaders())
            
            if len(response['meta']) == 5:
                data = response[twitterTweetsByUser.getDataArrayName()]
                nextToken = response['meta']['next_token']
            else:
                nextToken = None

        database.callCoreProcessingProcedure(tableName=coreTableName, procedureName=twitterTweetsByUser.getDatabaseProcedureName())


def loadTwitterTweetsByCashtag(database):
    twitterTweetsByCashtag = TwitterTweetsByCashTag()
    stageTableName = getDatabaseTableName('stage', twitterTweetsByCashtag.getDatabaseObjectName())
    coreTableName = getDatabaseTableName('core', twitterTweetsByCashtag.getDatabaseObjectName())

    #get twitter tweets by cashtag
    response = ApiRequests.getDataByGetRequest(url=twitterTweetsByCashtag.getBaseUrl() + twitterTweetsByCashtag.getInitialRelativeUrl(), headers=twitterTweetsByCashtag.getHeaders())
    data = response['statuses']
    nextRelativeUrl = response['search_metadata']['next_results']
    
    database.executeTruncateStatement(tableName=stageTableName)
    loadId = database.callLoadIdProcedure(procedureParameters=[stageTableName, datetime.today()])

    while (nextRelativeUrl != None):
        for d in data:
            d['text'] = emoji.demojize(d['text'])
            d['author_id'] = d['user']['id']
    
        database.executeInsertStatement(tableName=stageTableName, data=data, loadId=loadId, tableAttributes=twitterTweetsByCashtag.getDatabaseTableAttributes(), dynamicValues=twitterTweetsByCashtag.getDynamicValues())
        response = ApiRequests.getDataByGetRequest(url=twitterTweetsByCashtag.getBaseUrl() + nextRelativeUrl, headers=twitterTweetsByCashtag.getHeaders())
     
        if len(response['search_metadata']) == 9:
            data = response['statuses']
            nextRelativeUrl = response['search_metadata']['next_results']
        else:
            nextRelativeUrl = None

    database.callCoreProcessingProcedure(tableName=coreTableName, procedureName=twitterTweetsByCashtag.getDatabaseProcedureName())


def loadTwitterSentimentAnalysisData(database):
    twitterSentimentAnalysis = TwitterSentimentAnalysis()
    stageTableName = getDatabaseTableName('stage', twitterSentimentAnalysis.getDatabaseObjectName())
    coreTableName = getDatabaseTableName('core', twitterSentimentAnalysis.getDatabaseObjectName())

    #get data of tweet sentiment analysis
    database.executeTruncateStatement(stageTableName)
    loadId = database.callLoadIdProcedure([stageTableName, datetime.today()])
    tweets = database.executeSelectQuery(tableName='vw_report_twitter_tweets')
    
    newRecords = []
    for tweet in tweets:
        data = ApiRequests.getDataByPostRequest(url=twitterSentimentAnalysis.getUrl(), body={'text' : tweet[1]})
        scores = data['probability']
        data['tweetId'] = tweet[0]
        data['neg'] = scores['neg']
        data['pos'] = scores['pos']
        #data['loadId'] = loadId
        newRecords.append(data)

    database.executeInsertStatement(tableName=stageTableName, data=newRecords, loadId=loadId, tableAttributes=twitterSentimentAnalysis.getDatabaseTableAttributes(), dynamicValues=twitterSentimentAnalysis.getDynamicValues())
    database.callCoreProcessingProcedure(tableName=coreTableName, procedureName=twitterSentimentAnalysis.getDatabaseProcedureName())


if __name__ == "__main__":
    main()