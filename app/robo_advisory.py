# this is the "app/robo_advisor.py" file
# This code was written with help from Professor Rossetti's "Robo Advisor" project walkthrough
import requests
import json
import csv
import os
from dotenv import load_dotenv
import time

load_dotenv()
#Taken from a previous project
def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

timestr = time.strftime("%I:%M %p")
datestr = time.strftime("%m/%d/%Y")
symbol=input("Please input a valid stock or crypotcurency symbol: ")
# Found the .isalpha() function from https://stackoverflow.com/questions/18667410/how-can-i-check-if-a-string-only-contains-letters-in-python
if symbol.isalpha()==False:
    print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
    quit()
if len(symbol)>5:
    print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
    quit()
if len(symbol)<1:
    print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
    quit()


api_key=os.environ.get("ALPHAVANTAGE_API_KEY")
request_url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(request_url)
parsed_response = json.loads(response.text)
try:
    tsd=parsed_response["Time Series (Daily)"]
except KeyError:
    print("Please enter a valid stock symbol and try again")
    quit()

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
recent_close2=tsd[dates[1]]["4. close"]
recent100highprices=high_prices[:100]
recent_high=max(recent100highprices)
recent_low=min(low_prices)
#breakpoint()
#print(type(response))
#print(response.status_code)
#print(response.text)

reccomendation=""
reason=""
if float(latest_close)>=recent_low*1.2:
    if float(latest_close)>=float(recent_close2)*1.05:
        reccomendation="Buy"
        reason="You should buy because the latest close is more than 20% higher than the recent low and the most recent close is more than 5% higher than the previous day's close"
    else:
        reccomendation="Hold"
        reason="You should hold the stock or not buy because the latest close is less than 5% higher than the previous day's close"
else:
    reccomendation="Sell"
    reason="You should not buy the stock or sell because the latest close is within 20% of the recent low"



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
print("SELECTED SYMBOL: "+symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: "+timestr+" on "+datestr)
print("-------------------------")
print("LATEST DAY:"+ last_refreshed)
print("LATEST CLOSE:"+ to_usd(float(latest_close)))
print("RECENT HIGH: "+to_usd(float(recent_high)))
print("RECENT LOW: "+to_usd(float(recent_low)))
print("-------------------------")
print("RECOMMENDATION: "+reccomendation)
print("RECOMMENDATION REASON: "+reason)
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")