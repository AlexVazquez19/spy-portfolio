from tkinter import *
from tkinter import font

# DATA

# FRAMES
frm_container = Frame()
frm_container.grid(row=3,column=0,columnspan=2,sticky=W,pady=(20,0),padx=10)

frm_displaywindow = Frame(master=frm_container,bg="skyblue3",highlightbackground="black",highlightthickness=1.5,padx=20,pady=20)
frm_displaywindow.grid(row=0,rowspan=8,column=2,sticky="nsew")





# COMMANDS / FUNCTIONS
def getStockTicker():
    stock = ent_stockticker.get()
    lbl_test = Label(master=frm_container,text=stock)
    lbl_test.grid(row=1,column=1,sticky="w")

# CONFIGURE rows and columns in frames

# COMMANDS

# WIDGETS
bold_font = font.Font(weight='bold')

lbl_enterstock = Label(master=frm_container,text='Enter a Stock Ticker:',font=bold_font)
lbl_buffer = Label(master=frm_container,text='       ')
lbltst = Label(master=frm_displaywindow,text="TESTING")


ent_stockticker = Entry(master=frm_container,width=10)
#ent_stockticker.insert(0, "Ex: AAPL")

btn_getdata = Button(master=frm_container,text='Get Data',command=lambda: getStockTicker())
btn_1 = Button(master=frm_container,text='filler todo')
btn_2 = Button(master=frm_container,text='filler todo')
btn_3 = Button(master=frm_container,text='filler todo')
btn_4 = Button(master=frm_container,text='filler todo')
btn_5 = Button(master=frm_container,text='filler todo')

# PACKING / GRIDDING
lbl_enterstock.grid(row=0,column=0,sticky="w")
lbl_buffer.grid(row=0,column=1,sticky="w")
ent_stockticker.grid(row=1,column=0,sticky="w")
btn_getdata.grid(row=2,column=0,sticky="w")
btn_1.grid(row=3,column=0,sticky="w")
btn_2.grid(row=4,column=0,sticky="w")
btn_3.grid(row=5,column=0,sticky="w")
btn_4.grid(row=6,column=0,sticky="w")
btn_5.grid(row=7,column=0,sticky="w")

lbltst.grid(row=0,column=0,sticky='nsew')

# BINDS

