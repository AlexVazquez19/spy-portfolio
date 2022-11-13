#TODO fix errors on startup - added try-catch block for exceptions
#TODO add % symbol to weights
#TODO make plus/minus buttons look nicer
#TODO fix pie chart location
#TODO make text entered in boxes update the sector_weights list

from tkinter import *
import os

#WRITING / READING DATA
sector_weights = [27.6,13.5,12.7,10.8,10.4,8.4,6.5,2.8,2.6,2.4,2.3]

with open('sector_weights.txt','w') as f:
    for elem in sector_weights:
        f.write(str(elem) + '\n')

# WINDOW
window = Tk()
window.title("Spy Portfolio Optimizer")
window.geometry('1000x500')

# FRAMES
frm_title = Frame(bg='#4169e1') # holds the title
frm_title.pack(fill='x')

# CONFIGURE - rows and columns in frames
frm_title.rowconfigure([0], weight=1)
frm_title.columnconfigure([0,1], weight=1)

# IMPORT FILES
import weight_editors
import pie_chart

# WIDGETS
lbl_title = Label(master=frm_title,font=('Helvetica',25,'bold'),text='Spy Portfolio',bg='#4169e1',fg='white')

# PACKING / GRIDDING
lbl_title.grid(row=0,column=0,padx=20,pady=20,sticky='e')

# MAINLOOP
window.mainloop()