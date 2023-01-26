from tkinter import *
from tkinter import font

# DATA
portfolio_stocks = ['MSFT','AAPL','AMD']

# FRAMES
frm_container = Frame()
frm_container.grid(row=3,column=0,columnspan=2,sticky="w",pady=(25,0))

frm_mystocks = Frame(master=frm_container)
frm_mystocks.grid(row=0,column=0)

# CONFIGURE rows and columns in frames

# COMMANDS / FUNCTIONS
def updatePortfolio():
    r = 1
    for stock in portfolio_stocks:
        lbl_stock = Label(master=frm_mystocks,text=stock)
        lbl_stock.grid(row=r,column=0,sticky="w",padx=10)
        r+=1

# WIDGETS
bold_font = font.Font(weight='bold')

lbl_myportfolio = Label(master=frm_mystocks,text='My Portfolio',font=bold_font)

# PACKING / GRIDDING
lbl_myportfolio.grid(row=0,column=0,sticky="w",padx=10)

# BINDS
updatePortfolio()

