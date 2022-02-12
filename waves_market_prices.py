
class WavesMarketPrices:

    baseUrl = 'https://api.wavesplatform.com/v0/candles/WAVES/DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p?interval=1d&timeStart='
    headers = None
    name = 'waves_market_prices'
    tableAttributes = ['time', 'open', 'close', 'high', 'low', 'volume', 'quoteVolume', 'weightedAveragePrice', 'maxHeight', 'txsCount', 'timeClose', 'loadId']
    dynamicValues = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'