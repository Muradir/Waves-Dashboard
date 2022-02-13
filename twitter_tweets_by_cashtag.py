class TwitterTweetsByCashTag:

    #private class attributes
    __baseUrl = 'https://api.twitter.com/1.1/search/tweets.json'
    __initialRelativeUrl = '?q=%24Waves%24USDN&result_type=mixed&count=100&lang=en'
    __bearerToken = 'AAAAAAAAAAAAAAAAAAAAALvmYwEAAAAAJPSM4F8E1IbwuSJHvThJMlXkJw8%3DbJCYq2JIWaEllT1CiUxdxgsYklmJUmIMwA44ai4Lgu3nQVGtn3'
    __databaseObjectName = 'twitter_tweets_by_cashtag'
    __databaseTableAttributes = ['id', 'created_at', 'author_id', 'text', 'loadId']
    __dynamicValues = '%s, %s, %s, %s, %s'


    #public class get methods
    def getBaseUrl(self):
        return self.__baseUrl

    def getInitialRelativeUrl(self):
        return self.__initialRelativeUrl

    def getHeaders(self):
        return {'Authorization' : 'Bearer ' + self.__bearerToken}

    def getDataArrayName(self):
        return self.__dataArrayName

    def getDatabaseObjectName(self):
        return self.__databaseObjectName

    def getDatabaseTableAttributes(self):
        return self.__databaseTableAttributes

    def getDatabaseProcedureName(self):
        return 'load_core_' + self.__databaseObjectName

    def getDynamicValues(self):
        return self.__dynamicValues