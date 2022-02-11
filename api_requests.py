import requests

class ApiRequests:

    def getData(url, headers):
        return requests.get(url = url, headers = headers).json()
        #data = response.json()
        #return data
