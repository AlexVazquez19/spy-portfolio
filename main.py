#TODO fix errors on startup
#TODO add % symbol to weights

from tkinter import *

# WINDOW
window = Tk()
window.title("Spy Portfolio Optimizer")
window.geometry('1000x600')

# FRAMES
frm_title = Frame(bg='#4169e1') # holds the title
frm_title.pack(fill='x')

# CONFIGURE - rows and columns in frames
frm_title.rowconfigure([0], weight=1)
frm_title.columnconfigure([0,1], weight=1)

# IMPORT FILES
import editorsV2

# WIDGETS
lbl_title = Label(master=frm_title,font=('Helvetica',25,'bold'),text='Spy Portfolio',bg='#4169e1',fg='white')

# PACKING / GRIDDING
lbl_title.grid(row=0,column=0,padx=20,pady=20,sticky='e')

# MAINLOOP
window.mainloop()