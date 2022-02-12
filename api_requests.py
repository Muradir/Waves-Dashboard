import requests

class ApiRequests:

    def getDataByGetRequest(url, headers):
        return requests.get(url = url, headers = headers).json()
    
    def getDataByPostRequest(url, body):
        return requests.post(url=url, data=body).json()
