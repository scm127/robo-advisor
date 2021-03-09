# robo_advisor
This Readme.md is adopted from my Shopping-cart Readme.  It explains how to clone the robo-advisor repository, and allows the user to pull stock data from the internet for any stock and returns the last closing price, the recent high and the recent low price and a reccomendation about whether to buy or sell the stock. 

# Prerequisites:
```sh
Anaconda 3.7+
Python 3.7+
Pip
```

# Installing the Repository
Fork this remote repository under your own control, then "clone" or download your remote copy onto your local computer.

Navigate to the repository from the command line (subsequent commands assume you are running them from the local repository's root directory). If you saved the repository to your desktop use the following code or else you will have to adjust the code to wherever the repository is saved:
```sh
cd ~/Desktop/robo-advisor
```
# Create and activate virtual enviorment
Use Anaconda to create and activate a new virtual environment, perhaps called "my-game-env":

```sh
conda create -n stocks-env python=3.8
conda activate stocks-env
```

From inside the virtual environment, install package dependencies. The requirmemnts.txt file has the Dotenv package which is needed to load enviorment variables as well as the requests package which is nrequest data from the internet:
```sh
pip install -r requirements.txt
```
# Setup local variables
In the root directory of your local repository, create a new file called ".env". The program needs an API key to issue requests to AlphaVantage API. Follow this link and the instructions to get a free API key:  https://www.alphavantage.co/ and create a variable called ALPHAVANTAGE_API_KEY in the .env file with your API key:

```sh
ALPHAVANTAGE_API_KEY="YOUR_API_KEY"
```

# Run the robo-advisor Python Script and follow the instructions to input valid stock symbols (eg. "MSFT") for the desired stocks:
```sh
python shopping_cart.py
```
Note that if a numeric value is input or if the input is not between 1 and 5 letters, the program will stop and ask to please enter a valid stock symbol. If there is no stock symbols that match, the program will ask to enter a valid symbol. 

