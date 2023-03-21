from pandas_datareader import data as pdr
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mpl_dates

end_date = pd.to_datetime(date.today())
start_date = pd.to_datetime(date.today() - relativedelta(years=1))

df = pdr.DataReader("AAPL", 'stooq', start_date, end_date)
df.reset_index(inplace=True)


df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].apply(mpl_dates.date2num)
ohlc = df.astype(float)

# Creating Subplots
fig, ax = plt.subplots()
  
candlestick_ohlc(ax, df.values, width=0.6,
                 colorup='green', colordown='red', alpha=0.8)
  
# Setting labels & titles
ax.set_xlabel('Date')
ax.set_ylabel('Price')
fig.suptitle('Daily Candlestick Chart of AAPL')
  
# Formatting Date
date_format = mpl_dates.DateFormatter(r'%d-%m-%Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
  
fig.tight_layout()
  
plt.show()

