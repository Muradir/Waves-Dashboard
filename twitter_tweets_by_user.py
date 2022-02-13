class TwitterTweetsByUser:

    #private class attributes
    __baseUrl = 'https://api.twitter.com/2/users/'
    __bearerToken = 'AAAAAAAAAAAAAAAAAAAAALvmYwEAAAAAJPSM4F8E1IbwuSJHvThJMlXkJw8%3DbJCYq2JIWaEllT1CiUxdxgsYklmJUmIMwA44ai4Lgu3nQVGtn3'
    __databaseObjectName = 'twitter_tweets_by_user'
    __databaseTableAttributes = ['id', 'created_at', 'author_id', 'text', 'loadId']
    __dynamicValues = '%s, %s, %s, %s, %s'


    #public get methods
    def getUrl(self, relativeUrl):
        return self.__baseUrl + relativeUrl
    
    def getHeaders(self):
        return {'Authorization' : 'Bearer ' + self.__bearerToken}

    def getDataArrayName(self):
        return self.__dataArrayName

    def getDatabaseTableName(self, databaseLayer):
        return databaseLayer + '_' + self.__databaseObjectName

    def getDatabaseTableAttributes(self):
        return self.__databaseTableAttributes

    def getDatabaseProcedureName(self):
        return 'load_core_' + self.__databaseObjectName

    def getDynamicValues(self):
        return self.__dynamicValues


