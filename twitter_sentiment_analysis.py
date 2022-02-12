class TwitterSentimentAnalysis:

    url = 'http://text-processing.com/api/sentiment/'
    tableName = 'stage_twitter_sentiment_analysis'
    tableAttributes = ['tweetId', 'neg', 'pos', 'label', 'loadId']
    dynamicValues = '%s, %s, %s, %s, %s'