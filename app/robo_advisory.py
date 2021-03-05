# this is the "app/robo_advisor.py" file
import requests
import json
import csv
import os

#Taken from a previous project
def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

request_url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey=demo"

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

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writeheader() # uses fieldnames set above
    writer.writerow({"city": "New York", "name": "Yankees"})
    writer.writerow({"city": "New York", "name": "Mets"})
    writer.writerow({"city": "Boston", "name": "Red Sox"})
    writer.writerow({"city": "New Haven", "name": "Ravens"})

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