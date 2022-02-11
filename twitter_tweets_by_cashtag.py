class TwitterTweetsByCashTag:

    baseUrl = 'https://api.twitter.com/1.1/search/tweets.json'
    initialRelativeUrl = '?q=%24Waves%24USDN&result_type=recent&count=100&lang=en'
    bearerToken = 'AAAAAAAAAAAAAAAAAAAAALvmYwEAAAAAJPSM4F8E1IbwuSJHvThJMlXkJw8%3DbJCYq2JIWaEllT1CiUxdxgsYklmJUmIMwA44ai4Lgu3nQVGtn3'
    headers = {'Authorization' : 'Bearer ' + bearerToken}
    tableName = 'stage_twitter_tweets_by_cashtag'
    tableAttributes = ['id', 'created_at', 'author_id', 'text', 'loadId']
    dynamicValues = '%s, %s, %s, %s, %s'