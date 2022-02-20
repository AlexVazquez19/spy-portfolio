#TODO fix errors on startup
#TODO add % symbol to weights

from tkinter import *
from functools import partial

# create the window
window = Tk()
window.title("Spy Portfolio Optimizer")
window.geometry('1000x600')

# Data
sector_names = ['Information Technology','Health Care','Consumer Discretionary','Communication Services',
'Financials','Industrials','Consumer Staples','Utilities','Materials','Real Estate','Energy']
sector_weights = [27.6,13.5,12.7,10.8,10.4,8.4,6.5,2.8,2.6,2.4,2.3]
sum_of_sector_weights = 0
for val in sector_weights:
    sum_of_sector_weights += val

# frames
frm_title = Frame(bg='#4169e1') # holds the title
frm_title.pack(fill='x')
frm_editorsANDallocations = Frame()
frm_editorsANDallocations.pack()
frm_editors = Frame(master=frm_editorsANDallocations) # holds the sector weight editors
frm_editors.pack(side='left',anchor='nw') 
frm_allocations = Frame(master=frm_editorsANDallocations)
frm_allocations.pack(side='left',anchor='nw')

# commands
def add(index):
    value = sector_weights[index]
    sector_weights[index] = round(value + 1, 2)
    frm_editors_2Dlist[index][2].delete(0,END)
    frm_editors_2Dlist[index][2].insert(0,sector_weights[index])
    updateSectorWeights()
    updateAllocations()

def subtract(index):
    value = sector_weights[index] # prevents user from going below zero
    if value - 1 > 0:
        sector_weights[index] = round(value - 1, 2)
    frm_editors_2Dlist[index][2].delete(0,END)
    frm_editors_2Dlist[index][2].insert(0,sector_weights[index])
    updateSectorWeights()
    updateAllocations()

def updateSectorWeights():
    sum_of_sector_weights = 0
    for val in sector_weights:
        sum_of_sector_weights += val
    if sum_of_sector_weights > 100 or sum_of_sector_weights < 100:
        lbl_totalweight_number.config(text=str(round(sum_of_sector_weights,2)),fg='red')
    elif sum_of_sector_weights == 100:
        lbl_totalweight_number.config(text=str(round(sum_of_sector_weights,2)),fg='green')

def callback(sv,index):
    if sv.get() != '':
        number = float(sv.get())
        sector_weights[index] = number
        updateSectorWeights()
        updateAllocations()

def callback2(sv):
    if sv.get() != '':
        number = float(sv.get())
        ent_funds.config(fg='black')
        updateAllocations()
    if sv.get() == '':
        setAllocationsZero()

def updateAllocations():
    for i in range(11):
        allocation_labels[i].config(text='$' + str(round((sector_weights[i]/100)*float(ent_funds.get()),2)))

def setAllocationsZero():
    for i in range(11):
        allocation_labels[i].config(text='$0.00')

def temp_text(e):
   ent_funds.delete(0,"end")

# configure rows and columns for sector weight editors
frm_title.rowconfigure([0], weight=1)
frm_title.columnconfigure([0,1], weight=1)

frm_editors.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11], minsize=25, weight=1)
frm_editors.columnconfigure([0,1,2,3], minsize=25, weight=1)

# adds the plus, minus, entry, and sector name widgets to frm_editors frame
for i in range(11):
    for j in range(4):
        if j == 0:
            lbl_sectorname = Label(master=frm_editors,text=sector_names[i],width=17,anchor='w')
            lbl_sectorname.grid(row=i,column=j,sticky="w",padx=10)
        if j == 1:
            btn_subtract = Button(master=frm_editors,text='-',command=partial(subtract,i)) #could replace partial with 'lambda:'
            btn_subtract.grid(row=i,column=j,sticky="nsew")
        if j == 2:
            sv = StringVar()
            sv.trace("w", lambda name, index, mode, sv=sv,i=i: callback(sv,i))
            ent_weight = Entry(master=frm_editors,textvariable=sv,width=6)
            ent_weight.grid(row=i,column=j)
            ent_weight.insert(0, sector_weights[i])
        if j == 3:
            btn_add = Button(master=frm_editors,text='+',command=partial(add,i)) #could replace partial with 'lambda:'
            btn_add.grid(row=i,column=j,sticky="nsew")

# adds dollar amount allocations to frm_allocations frame

# widgets
lbl_title = Label(master=frm_title,font=('Helvetica',25,'bold'),text='Spy Portfolio',bg='#4169e1',fg='white')
lbl_totalweight = Label(master=frm_editors,text='Total Weight',width=17,anchor='w')
lbl_totalweight_number = Label(master=frm_editors,text=str(sum_of_sector_weights),fg='green')

sv2 = StringVar()
sv2.trace("w", lambda name, index, mode, sv=sv2: callback2(sv))
ent_funds = Entry(master=frm_title,textvariable=sv2,width=10,fg='grey')
ent_funds.insert(0,'Input funds')

lbl_alloc_info_tech = Label(master=frm_allocations,width=10,anchor='w')
lbl_alloc_health = Label(master=frm_allocations,width=10,anchor='w')
lbl_alloc_consumer_discretionary = Label(master=frm_allocations,width=10,anchor='w')
lbl_alloc_communications = Label(master=frm_allocations,width=10,anchor='w')
lbl_alloc_financials = Label(master=frm_allocations,width=10,anchor='w')
lbl_alloc_industrials = Label(master=frm_allocations,width=10,anchor='w')
lbl_alloc_consumer_staples = Label(master=frm_allocations,width=10,anchor='w')
lbl_alloc_utilities = Label(master=frm_allocations,width=10,anchor='w')
lbl_alloc_materials = Label(master=frm_allocations,width=10,anchor='w')
lbl_alloc_real_estate = Label(master=frm_allocations,width=10,anchor='w')
lbl_alloc_energy = Label(master=frm_allocations,width=10,anchor='w')

allocation_labels = [lbl_alloc_info_tech,lbl_alloc_health,lbl_alloc_consumer_discretionary,
lbl_alloc_communications,lbl_alloc_financials,lbl_alloc_industrials,lbl_alloc_consumer_staples,
lbl_alloc_utilities,lbl_alloc_materials,lbl_alloc_real_estate,lbl_alloc_energy]

# creates a 2D list of the widgets inside the frm_editors frame
frm_editors_2Dlist = [] 
count = 0
for child in frm_editors.winfo_children():
    count += 1
    if count%4 == 0:
        sub_list = [frm_editors.winfo_children()[count-4],frm_editors.winfo_children()[count-3],frm_editors.winfo_children()[count-2],frm_editors.winfo_children()[count-1]]
        frm_editors_2Dlist.append(sub_list)

# packing / gridding
lbl_title.grid(row=0,column=0,padx=20,pady=20,sticky='e')
lbl_totalweight.grid(row=11,column=0,sticky="w",padx=10)
lbl_totalweight_number.grid(row=11,column=2,sticky="w")

for i in range(11):
    allocation_labels[i].grid(row=i,column=0,pady=1.5,padx=18)

ent_funds.grid(row=0,column=1,pady=20,sticky='w')

# binds
ent_funds.bind("<FocusIn>", temp_text)

# mainloop
window.mainloop()