class SP500UsdMarketPrices:

    #private class attributes
    __url = 'https://api.stlouisfed.org/fred/series/observations?api_key=1260500ff9e23c45cdf81a960f44bf68&file_type=json&observation_start=2017-01-01&series_id=SP500'
    __dbTableName = 'stlouisfed_marketPricesSP500ToUsd'
    __dbTableAttributes = '(sp500MarketPrice_usd, date)'
    __dbDynamicInsertPlaceholders = '%s, %s'


    #public class getter methods
    def getUrl(self):
        return self.__url

    def getDbTableName(self):
        return self.__dbTableName

    def getDbTableAttributes(self):
        return self.__dbTableAttributes

    def getDbDynamicInsertPlaceholders(self):
        return self.__dbDynamicInsertPlaceholders