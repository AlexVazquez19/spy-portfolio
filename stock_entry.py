from tkinter import *
from tkinter import font

from pandas_datareader import data as pdr
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# DATA

# FRAMES
frm_container = Frame()
frm_container.grid(row=3,column=0,columnspan=2,sticky=W,pady=(20,0),padx=10)

frm_displaywindow = Frame(master=frm_container,highlightbackground="black",highlightthickness=1.5)
frm_displaywindow.grid(row=0,column=0)

# SCROLL WINDOW
canvas_portfolio = Canvas(frm_displaywindow,width=1000, height=300)
vscroll = Scrollbar(frm_displaywindow,orient='vertical',command=canvas_portfolio.yview)
scrollable_frame = Frame(canvas_portfolio)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas_portfolio.configure(
        scrollregion=canvas_portfolio.bbox("all")
    )
)

canvas_portfolio.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas_portfolio.configure(yscrollcommand=vscroll.set)

# FRAMES - used for seperating the left menu from the displayed window on the right
frm_leftmenu = Frame(master=scrollable_frame)
frm_leftmenu.grid(row=0,column=0,sticky='n')
frm_chartwindow = Frame(master=scrollable_frame)
frm_chartwindow.grid(row=0,column=1,sticky='n')

# COMMANDS / FUNCTIONS
def getStockTicker():
    stock = ent_stockticker.get()
    end_date = pd.to_datetime(date.today())
    start_date = pd.to_datetime(date.today() - relativedelta(years=1))
    df = pdr.DataReader(stock, 'stooq', start_date, end_date)
    df.reset_index(inplace=True)
    # Update the date column formatting
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].apply(mpl_dates.date2num)
    ohlc = df.astype(float)
    # Creating Subplots
    fig, ax = plt.subplots(figsize=(8,4),dpi=40)
    candlestick_ohlc(ax,df.values,width=0.6,colorup='green',colordown='red',alpha=0.8)
    # Setting labels & titles
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    fig.suptitle('1 Year Candlestick Chart of ' + stock)
    # Formatting Date
    date_format = mpl_dates.DateFormatter(r'%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    fig.tight_layout()
    # Create and pack the canvas
    canvas = FigureCanvasTkAgg(fig, master=frm_chartwindow)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0,column=0)
        

# CONFIGURE rows and columns in frames

# WIDGETS
bold_font = font.Font(weight='bold')

lbl_enterstock = Label(master=frm_leftmenu,text='Enter a Stock Ticker:',font=bold_font)


ent_stockticker = Entry(master=frm_leftmenu,width=10)
#ent_stockticker.insert(0, "Ex: AAPL")

btn_getdata = Button(master=frm_leftmenu,text='Get Data',command=lambda: getStockTicker())


# PACKING / GRIDDING
lbl_enterstock.grid(row=0,column=0,sticky="w")
ent_stockticker.grid(row=1,column=0,sticky="w")
btn_getdata.grid(row=2,column=0,sticky="w")

canvas_portfolio.pack(side="left", fill="both", expand=True)
vscroll.pack(side="right", fill="y")

# BINDS

