import yfinance as yf

stock = yf.Ticker("NVDA")
info = stock.info

name = info["longName"]
price = info["currentPrice"]
change = info["regularMarketChangePercent"]

print("Company:", name)
print("Price: $", price)
print("Change today:", round(change, 2), "%")