from typing import List
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

class StockData(BaseModel):
  symbol: str
  prices: List[float]

stock_prices = {
    'AAPL': [150.25, 152.10, 148.75, 151.50, 149.80],
    'MSFT': [280.50, 285.25, 282.75, 278.90, 283.60],
    'AMZN': [3250.00, 3280.50, 3220.75, 3260.25, 3240.10],
    'GOOG': [2750.75, 2780.25, 2760.50, 2770.10, 2765.80],
    'TSLA': [750.00, 760.50, 755.25, 745.80, 752.90]
}

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index(request: Request):
  return templates.TemplateResponse("stock_form.html", {"request": request})
  # return {"status": "ok", "about": "FastAPI endpoint"}
  
@app.post("/add")
def stock_add(symbol: str = Form(...), name: str=Form(...), currencyd: str=Form(...)):
  return {
    "symbol": symbol,
    "name": name,
    "currency": currencyd
  }

# create a route allprices to show all the stock_prices
@app.get("/price/{stocksymbol}")
def getsymbolprice(stocksymbol):
  return {"status": "ok", "symbol": stocksymbol}

# post request route /add_stock to add a symbol and price
@app.post("/add_stock")
def addsymbol(stockjson: StockData):
  return {"status": "ok", "message": "added"}
