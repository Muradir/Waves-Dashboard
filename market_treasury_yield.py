class MarketTreasuryYield:

    #private class attributes
    __baseUrl = 'https://api.stlouisfed.org/fred/series/observations?series_id=DGS10&api_key=1260500ff9e23c45cdf81a960f44bf68&file_type=json&observation_start='
    __dataArrayName = 'observations'
    __headers = None
    __databaseObjectName = 'market_treasury_yield'
    __databaseTableAttributes = ['date', 'value', 'loadId']
    __dynamicValues = '%s, %s, %s'

    #public class get methods
    def getUrl(self, timeStart):
        return self.__baseUrl + timeStart

    def getDataArrayName(self):
        return self.__dataArrayName

    def getHeaders(self):
        return self.__headers

    def getDatabaseTableName(self, databaseLayer):
        return databaseLayer + '_' + self.__databaseObjectName

    def getDatabaseTableAttributes(self):
        return self.__databaseTableAttributes

    def getDatabaseProcedureName(self):
        return 'load_core_' + self.__databaseObjectName

    def getDynamicValues(self):
        return self.__dynamicValues

    