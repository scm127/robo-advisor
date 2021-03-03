# this is the "app/robo_advisor.py" file
import requests
import json

request_url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey=demo"

response = requests.get(request_url)
last_refreshed= parsed_response["Meta Data"]["3. Last Refreshed"]

parsed_response = json.loads(response.text)
latest_close= parsed_response["Time Series {Daily}"]["2021-03-02"]["4. close"]
breakpoint()
#print(type(response))
#print(response.status_code)
#print(response.text)

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: {last_refreshed}")
print("LATEST CLOSE: {to_usd(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")