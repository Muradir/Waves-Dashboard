import requests

class ApiRequests:

    def getDataByGetRequest(url, headers):
        return requests.get(url = url, headers = headers).json()
