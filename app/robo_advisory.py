# this is the "app/robo_advisor.py" file
import requests
import json
import csv
import os
from dotenv import load_dotenv
load_dotenv()
#Taken from a previous project
def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

symbol="TSLA"
api_key=os.environ.get("ALPHAVANTAGE_API_KEY")
request_url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(request_url)
parsed_response = json.loads(response.text)

tsd=parsed_response["Time Series (Daily)"]

dates= list(tsd.keys())

latest_day=dates[0]

last_refreshed= parsed_response["Meta Data"]["3. Last Refreshed"]

latest_close= tsd[latest_day]["4. close"] 
high_prices=[]
low_prices=[]
for date in dates:
    high_price=tsd[date]["2. high"]
    high_prices.append(high_price)
    low_price=tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_high=max(high_prices)
recent_low=min(low_prices)
#breakpoint()
#print(type(response))
#print(response.status_code)
#print(response.text)



import csv

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv") # a relative filepath

csv_headers=["timestamp","open","high","low","close","volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices=tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high":daily_prices["2. high"],
            "low":daily_prices["3. low"],
            "close":daily_prices["4. close"],
            "volume":daily_prices["5. volume"],
        })

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY:"+ last_refreshed)
print("LATEST CLOSE:"+ to_usd(float(latest_close)))
print("RECENT HIGH: "+to_usd(float(recent_high)))
print("RECENT LOW: "+to_usd(float(recent_low)))
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")