import yfinance as yf 
import streamlit as st
import pandas as pd
import os
from PIL import Image
import datetime
#from stocks.tickers import list_of_tickers





image = Image.open('wallstreet_photo.jpg')
st.image(image, use_column_width=True)
st.write("""
# Price and Volume (last 10 Years)
For each symbol listed on the SP500
""")


st.header('Performance This Decade') #Check Performance In This Past Decade

workingDir = os.getcwd()
df = pd.read_csv(f'{workingDir}/sp_500_stocks.csv')
symbols = df['Ticker'].values.tolist()
symbols.sort()
Ticker_Symbol_Input = st.selectbox('Select an American Stock',symbols)

#get data on this ticker
tickerData = yf.Ticker(Ticker_Symbol_Input)
today = datetime.datetime.now()
ten_years_ago = today - datetime.timedelta(days=3650)
tickerDf = tickerData.history(period='1d', start=ten_years_ago.strftime('%Y-%m-%d'), end=today.strftime('%Y-%m-%d'))


# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price This Past Decade
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume This Past Decade
""")
st.line_chart(tickerDf.Volume)





