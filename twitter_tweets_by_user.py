from twitter import Twitter

class TwitterTweetsByUser:

    baseUrl = Twitter.baseUrl + '2/users/'
    bearerToken = 'AAAAAAAAAAAAAAAAAAAAALvmYwEAAAAAJPSM4F8E1IbwuSJHvThJMlXkJw8%3DbJCYq2JIWaEllT1CiUxdxgsYklmJUmIMwA44ai4Lgu3nQVGtn3'
    headers = {'Authorization' : 'Bearer ' + bearerToken}
    tableName = 'stage_twitter_tweets_by_user'
    tableAttributes = ['id', 'created_at', 'author_id', 'text', 'loadId']
    dynamicValues = '%s, %s, %s, %s, %s'