import requests
import json

URL = "https://www.alphavantage.co/query"


function="TIME_SERIES_DAILY"
# symbol=IBM
# api_key=THISISMYAPI

params = {
  "function" : function,
  "symbol" : "IBM",
  "apikey": "demo"
}

# r = requests.get('https://www.python.org')
r = requests.get(url=URL, params=params)
print(r.status_code)

stock_values = r.json()

print(stock_values)

# save the data to a json file

# open file for writing
# write to the file
# close file

with open("IBM.json", "w") as f:
  json.dump(stock_values, f)