class SP500UsdMarketPrices:

    #private class attributes
    __url = 'https://api.stlouisfed.org/fred/series/observations?api_key=1260500ff9e23c45cdf81a960f44bf68&file_type=json&observation_start=2017-01-01&series_id=SP500'
    __headers = None
    __tableName = 'stlouisfed_marketPricesSP500ToUsd'
    __tableAttributes = '(sp500MarketPrice_usd, date)'
    __dynamicInsertPlaceholders = '%s, %s'

    #public class get methods
    def getUrl(self):
        return self.__url

    def getHeaders(self):
        return self.__headers

    def getTableName(self):
        return self.__tableName

    def getTableAttributes(self):
        return self.__tableAttributes

    def getDynamicInsertPlaceholders(self):
        return self.__dynamicInsertPlaceholders