from tkinter import *
from tkinter import font


# DATA
portfolio_stocks = ['MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD','MSFT','AAPL','AMD']

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
        lbl_stock = Label(master=scrollable_frame,text=stock)
        lbl_stock.grid(row=r,column=0,sticky="w",padx=10)
        r+=1

# SCROLL WINDOWS
canvas_portfolio = Canvas(frm_mystocks)
vscroll = Scrollbar(frm_mystocks,orient='vertical',command=canvas_portfolio.yview)
scrollable_frame = Frame(canvas_portfolio)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas_portfolio.configure(
        scrollregion=canvas_portfolio.bbox("all")
    )
)

canvas_portfolio.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas_portfolio.configure(yscrollcommand=vscroll.set)


# WIDGETS
bold_font = font.Font(weight='bold')

lbl_myportfolio = Label(master=scrollable_frame,text='My Portfolio',font=bold_font)

# PACKING / GRIDDING
canvas_portfolio.pack(side="left", fill="both", expand=True)
vscroll.pack(side="right", fill="y")
lbl_myportfolio.grid(row=0,column=0,sticky="w",padx=10)

# BINDS
updatePortfolio()

