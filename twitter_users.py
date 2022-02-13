class TwitterUsers:
    
    #private class attribute
    __url = 'https://api.twitter.com/2/users/by?usernames=wavesprotocol,SignatureChain,neutrino_proto,sasha35625&user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at'
    __bearerToken = 'AAAAAAAAAAAAAAAAAAAAALvmYwEAAAAAJPSM4F8E1IbwuSJHvThJMlXkJw8%3DbJCYq2JIWaEllT1CiUxdxgsYklmJUmIMwA44ai4Lgu3nQVGtn3'
    __dataArrayName = 'data'


    #public get methods
    def getUrl(self):
        return self.__url

    def getHeaders(self):
        return {'Authorization' : 'Bearer ' + self.__bearerToken}

    def getDataArrayName(self):
        return self.__dataArrayName
