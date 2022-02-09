from asyncio.windows_events import NULL


class WavesMarketPrices:

    url = 'https://api.wavesplatform.com/v0/candles/WAVES/DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p?timeStart=2021-01-01&interval=1d'
    #bearerToken = 'AAAAAAAAAAAAAAAAAAAAALvmYwEAAAAAJPSM4F8E1IbwuSJHvThJMlXkJw8%3DbJCYq2JIWaEllT1CiUxdxgsYklmJUmIMwA44ai4Lgu3nQVGtn3'
    headers = None
    tableName = 'waves_market_prices_test'
    tableAttributes = ['time', 'open', 'close', 'high', 'low', 'volume', 'quoteVolume', 'weightedAveragePrice', 'maxHeight', 'txsCount', 'timeClose', 'loadId']
    dynamicValues = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'