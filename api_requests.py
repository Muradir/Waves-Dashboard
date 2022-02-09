import requests

class ApiRequests:

    def getData(url, headers):
        response = requests.get(url = url, headers = headers)
        data = response.json()['data']
        return data
