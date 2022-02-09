import requests

input = "https://wavescap.com/api/markets.json"

def get_data_from_url(url_endpoint):
    response = requests.get(url_endpoint)
    data = response.json()
    return data

print(get_data_from_url(input))