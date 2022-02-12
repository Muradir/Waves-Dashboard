from twitter import Twitter

class TwitterUsers:
    
    url = Twitter.baseUrl + '2/users/by?usernames=wavesprotocol,SignatureChain,neutrino_proto,sasha35625&user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at'
    bearerToken = 'AAAAAAAAAAAAAAAAAAAAALvmYwEAAAAAJPSM4F8E1IbwuSJHvThJMlXkJw8%3DbJCYq2JIWaEllT1CiUxdxgsYklmJUmIMwA44ai4Lgu3nQVGtn3'
    headers = {'Authorization' : 'Bearer ' + bearerToken}