class TwitterSentimentAnalysis:

    #private class attributes
    __url = 'http://text-processing.com/api/sentiment/'
    __databaseObjectName = 'twitter_sentiment_analysis'
    __databaseTableAttributes = ['tweetId', 'neg', 'pos', 'label', 'loadId']
    __dynamicValues = '%s, %s, %s, %s, %s'


    #public class get methods
    def getUrl(self):
        return self.__url

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