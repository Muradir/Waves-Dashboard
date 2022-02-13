class WavesApy:

    #private class attributes
    __url = 'https://dev.pywaves.org/neutrino/json'
    __headers = None
    __dataArrayName = 'usdn-apy'
    __databaseObjectName = 'waves_apy'
    __databaseTableAttributes = ['30d', '60d', '7d', 'last', '3d', 'dateOfToday', 'loadId']
    __dynamicValues = '%s, %s, %s, %s, %s, %s, %s'

    #public class get methods
    def getUrl(self):
        return self.__url

    def getHeaders(self):
        return self.__headers

    def getDataArrayName(self):
        return self.__dataArrayName

    def getDatabaseTableName(self, databaseLayer):
        return databaseLayer + '_' + self.__databaseObjectName

    def getDatabaseTableAttributes(self):
        return self.__databaseTableAttributes

    def getDatabaseProcedureName(self):
        return 'load_core_' + self.__databaseObjectName

    def getDynamicValues(self):
        return self.__dynamicValues