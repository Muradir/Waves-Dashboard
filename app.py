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
    #db
    database = Database()
    #get timeStart for all time relative api requests
    timeStart = (datetime.today() - relativedelta(years=1)).date()
    loadTwitterTweetsByCashtag(database=database)
    loadTwitterTweetsByUser(database=database)
    loadMarketTreasuryYieldData(timeStart=timeStart, database=database)
    loadWavesMarketPrices(timeStart=timeStart, database=database)
    loadWavesApyData(database=database)


def getDatabaseObjectName(name, databaseLayer, isProcedure):
    if isProcedure:
        return 'load_core_' + name
    else:
        return databaseLayer + '_' + name


#def loadData(classItem, timeStart, database):
#    classInstance = classItem
#    dataArrayName = classInstance.getDataArrayName()
#    stageTableName = classInstance.getDatabaseTableName('stage')
#    coreTableName = classInstance.getDatabaseTableName('core')
#
#    #get treasury yield data
#    data = ApiRequests.getDataByGetRequest(url=classInstance.getBaseUrl(timeStart=str(timeStart)), headers=classInstance.getHeaders())[dataArrayName]
#
#    #database handling
#    database.executeTruncateStatement(tableName=stageTableName)
#    loadId = database.callLoadIdProcedure(procedureParameters=[stageTableName, datetime.today()])
#    database.executeInsertStatement(tableName=stageTableName, data=data, loadId=loadId, tableAttributes=classInstance.getDatabaseTableAttributes(), dynamicValues=classInstance.getDynamicValues())
#    database.callCoreProcessingProcedure(tableName=coreTableName, procedureName=classInstance.getDatabaseProcedureName())


def loadMarketTreasuryYieldData(timeStart, database):
    marketTreasuryYield = MarketTreasuryYield()
    stageTableName = marketTreasuryYield.getDatabaseTableName('stage')
    coreTableName = marketTreasuryYield.getDatabaseTableName('core')

    #get treasury yield data
    data = ApiRequests.getDataByGetRequest(url=marketTreasuryYield.getUrl(timeStart=str(timeStart)), headers=marketTreasuryYield.getHeaders())['observations']

    #database handling
    database.executeTruncateStatement(tableName=stageTableName)
    loadId = database.callLoadIdProcedure(procedureParameters=[stageTableName, datetime.today()])
    database.executeInsertStatement(tableName=stageTableName, data=data, loadId=loadId, tableAttributes=marketTreasuryYield.getDatabaseTableAttributes(), dynamicValues=marketTreasuryYield.getDynamicValues())
    database.callCoreProcessingProcedure(tableName=coreTableName, procedureName=marketTreasuryYield.getDatabaseProcedureName())


def loadWavesMarketPrices(timeStart, database):
    wavesMarketPrices = WavesMarketPrices()
    stageTableName = wavesMarketPrices.getDatabaseTableName('stage')
    coreTableName = wavesMarketPrices.getDatabaseTableName('core')

    #get waves market price data
    data = ApiRequests.getDataByGetRequest(url=wavesMarketPrices.getUrl(timeStart=str(timeStart)), headers=wavesMarketPrices.getHeaders())['data']
    
    #database handling
    database.executeTruncateStatement(tableName=stageTableName)
    loadId = database.callLoadIdProcedure(procedureParameters=[stageTableName, datetime.today()])
    database.executeInsertStatement(stageTableName, data=data, loadId=loadId, tableAttributes=wavesMarketPrices.getDatabaseTableAttributes(), dynamicValues=wavesMarketPrices.getDynamicValues())
    database.callCoreProcessingProcedure(tableName=coreTableName, procedureName=wavesMarketPrices.getDatabaseProcedureName())

def loadWavesApyData(database):
    wavesApy = WavesApy()
    stageTableName = wavesApy.getDatabaseTableName('stage')
    coreTableName = wavesApy.getDatabaseTableName('core')

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
    stageTableName = twitterTweetsByUser.getDatabaseTableName('stage')
    coreTableName = twitterTweetsByUser.getDatabaseTableName('core')
    
    #get twitter (waves)user data
    twitterUserData = ApiRequests.getDataByGetRequest(url=twitterUsers.getUrl(), headers=twitterUsers.getHeaders())['data']
    twitterUserIds = []

    for user in twitterUserData:
        twitterUserIds.append(user['id'])

    database.executeTruncateStatement(tableName=stageTableName)
    loadId = database.callLoadIdProcedure(procedureParameters=[stageTableName, datetime.today()])

    #get twitter tweets by user
    for userId in twitterUserIds:
        urlPerUserId = twitterTweetsByUser.getUrl(str(userId) + '/tweets?tweet.fields=author_id,created_at&start_time=2021-01-01T00:00:00.000Z&max_results=100')

        response = ApiRequests.getDataByGetRequest(url=urlPerUserId, headers=twitterTweetsByUser.getHeaders())
        data = response['data']
        nextToken = response['meta']['next_token']
    
        while (nextToken != None):
            for d in data:
                d['text'] = emoji.demojize(d['text'])
                
            database.executeInsertStatement(tableName=stageTableName, data=data, loadId=loadId, tableAttributes=twitterTweetsByUser.getDatabaseTableAttributes(), dynamicValues=twitterTweetsByUser.getDynamicValues())
            response = ApiRequests.getDataByGetRequest(url=urlPerUserId + '&pagination_token=' + nextToken, headers=twitterTweetsByUser.getHeaders())
            
            if len(response['meta']) == 5:
                data = response['data']
                nextToken = response['meta']['next_token']
            else:
                nextToken = None

        database.callCoreProcessingProcedure(tableName=coreTableName, procedureName=twitterTweetsByUser.getDatabaseProcedureName())


def loadTwitterTweetsByCashtag(database):
    twitterTweetsByCashtag = TwitterTweetsByCashTag()
    stageTableName = twitterTweetsByCashtag.getDatabaseTableName('stage')
    coreTableName = twitterTweetsByCashtag.getDatabaseTableName('core')

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
    stageTableName = twitterSentimentAnalysis.getDatabaseTableName('stage')
    coreTableName = twitterSentimentAnalysis.getDatabaseTableName('core')

    #get data of tweet sentiment analysis
    database.executeTruncateStatement(stageTableName)
    loadId = database.callLoadIdStoredProcedure([stageTableName, datetime.today()])
    tweets = database.executeSelectQuery(tableName='report_twitter_tweets')
    
    newRecords = []
    for tweet in tweets:
        data = ApiRequests.getDataByPostRequest(url=twitterSentimentAnalysis.getUrl(), body={'text' : tweet[1]})
        scores = data['probability']
        data['tweetId'] = tweet[0]
        data['neg'] = scores['neg']
        data['pos'] = scores['pos']
        data['loadId'] = loadId
        newRecords.append(data)

    database.executeInsertStatement(stageTableName, newRecords, twitterSentimentAnalysis.getDatabaseTableAttributes(), twitterSentimentAnalysis.getDynamicValues())
    database.callCoreProcessingProcedure(tableName=coreTableName, procedureName=twitterSentimentAnalysis.getDatabaseProcedureName())


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