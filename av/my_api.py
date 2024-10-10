from flask import Flask

stock_prices = {
    'AAPL': [150.25, 152.10, 148.75, 151.50, 149.80],
    'MSFT': [280.50, 285.25, 282.75, 278.90, 283.60],
    'AMZN': [3250.00, 3280.50, 3220.75, 3260.25, 3240.10],
    'GOOG': [2750.75, 2780.25, 2760.50, 2770.10, 2765.80],
    'TSLA': [750.00, 760.50, 755.25, 745.80, 752.90]
}

app = Flask('app')

@app.route("/")
def index():
  return "Welcome to Flask app"

@app.route("/allprices")
def allprices():
  return stock_prices

@app.route("/price/<stocksymbol>")
def symbolprice(stocksymbol):
  # if stocksymbol not present in stock_prices return stock not present
  if stocksymbol.upper() in stock_prices.keys():
      return {
        "stockprices": stock_prices[stocksymbol.upper()]
      }
  # else return stock prices for the symbol
  return f"Symbol: {stocksymbol.upper()} not found"


app.run(port=5051)

"""
status: ok, not_found
symbol: [], Name of symbols
data: {}  - values as a dictionary

Eg.
{
  "status": "ok",
  "symbol": ["IBM"],
  "data": {}
}
"""