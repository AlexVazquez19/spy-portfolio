from tkinter import *
from tkinter import font

# DATA

# FRAMES
frm_container = Frame()
frm_container.grid(row=3,column=0,columnspan=2,sticky="w",pady=(20,0),padx=10)



# CONFIGURE rows and columns in frames

# COMMANDS

# WIDGETS
bold_font = font.Font(weight='bold')

lbl_enterstock = Label(master=frm_container,text='Enter a Stock Ticker:',font=bold_font)

ent_stockticker = Entry(master=frm_container,width=10)

btn_getdata = Button(master=frm_container,text='Get Data')

# PACKING / GRIDDING
lbl_enterstock.grid(row=0,column=0,sticky="w")
ent_stockticker.grid(row=1,column=0,sticky="w")
btn_getdata.grid(row=2,column=0,sticky="w")

# BINDS

