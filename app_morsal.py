import requests
from datetime import date

#input = "https://wavescap.com/api/markets.json"
#
#def get_data_from_url(url_endpoint):
#    response = requests.get(url_endpoint)
#    data = response.json()
#    return data
#
#print(get_data_from_url(input))


input = "https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month%28NEW_DATE%29%20eq%202%20and%20year%28NEW_DATE%29%20eq%202022 "
#
#def get_data_from_url(url_endpoint):
#    response = requests.get(url_endpoint)
#    data = response.json()
#    return data
#
#print(get_data_from_url(input))

print(date.today())
