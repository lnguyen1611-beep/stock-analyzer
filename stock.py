import yfinance as yf
import streamlit as st

st.title("📈 Stock Analyzer")

tickers = st.text_input("Enter stocks (e.g. NVDA, AAPL, TSLA)")

if st.button("Analyze"):
    for symbol in tickers.upper().split(","):
        stock = yf.Ticker(symbol.strip())
        info = stock.info

        st.subheader(info.get("longName", symbol))
        st.write("💰 Price: $", info.get("currentPrice", "N/A"))
        st.write("📊 Change:", round(info.get("regularMarketChangePercent", 0), 2), "%")
        st.line_chart(stock.history(period="1mo")["Close"])
        st.divider()
