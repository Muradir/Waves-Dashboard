from twitter import Twitter

class TwitterTweetsByUser:

    url = Twitter.baseUrl + '2/users/'#1038127541607956480/tweets?tweet.fields=author_id,created_at&start_time=2021-01-01T00:00:00.000Z'
    bearerToken = 'AAAAAAAAAAAAAAAAAAAAALvmYwEAAAAAJPSM4F8E1IbwuSJHvThJMlXkJw8%3DbJCYq2JIWaEllT1CiUxdxgsYklmJUmIMwA44ai4Lgu3nQVGtn3'
    headers = {'Authorization' : 'Bearer ' + bearerToken}
    tableName = 'twitter_tweets_by_user'
    tableAttributes = ['id', 'created_at', 'author_id', 'text', 'loadId']
    dynamicValues = '%s, %s, %s, %s, %s'