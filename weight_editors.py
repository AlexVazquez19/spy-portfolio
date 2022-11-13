# explicitly created each button and label

from tkinter import *
from functools import partial
from tkinter import font
from pie_chart import updateChartNumbers, redraw

# DATA
sector_names = ['Information Technology','Health Care','Consumer Discretionary','Communication Services',
'Financials','Industrials','Consumer Staples','Utilities','Materials','Real Estate','Energy']

sector_weights = []
with open('sector_weights.txt','r') as f:
        data = f.read().splitlines()
        sector_weights = []
        for elem in data:
            sector_weights.append(float(elem))

sum_of_sector_weights = sum(sector_weights)

#need to make this better
weight_entry_boxes_tracker = 11 #used to make sure redraw isn't called 11 times on startup

# FRAMES
frm_inputFunds = Frame(bg='#D3D3D3')
frm_inputFunds.pack(fill='x')

frm_editors = Frame() # holds the sector weight editors
frm_editors.pack(side='left', anchor='n') 

# CONFIGURE rows and columns in frames
frm_editors.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11], minsize=25, weight=1)
frm_editors.columnconfigure([0,1,2,3,4], minsize=25, weight=1)

# COMMANDS / FUNCTIONS
def add(index): #adds 1 to sector weight when '+' button is clicked
    value = sector_weights[index]
    sector_weights[index] = round(value + 1, 2)
    rewriteSectorWeights()
    updateChartNumbers()
    list_weight_ents[index].delete(0,END)
    list_weight_ents[index].insert(0,sector_weights[index])
    updateSectorWeights()
    updateAllocations()

def subtract(index): #subtracts 1 from sector weight when '-' button is clicked
    value = sector_weights[index] # prevents user from going below zero
    if value - 1 > 0:
        sector_weights[index] = round(value - 1, 2)
        rewriteSectorWeights()
        updateChartNumbers()
    list_weight_ents[index].delete(0,END)
    list_weight_ents[index].insert(0,sector_weights[index])
    updateSectorWeights()
    updateAllocations()

def updateSectorWeights(): #updates the weights of each sector
    sum_of_sector_weights = 0
    for val in sector_weights:
        sum_of_sector_weights += val
    if sum_of_sector_weights > 100 or sum_of_sector_weights < 100:
        lbl_totalweight_number.config(text=str(round(sum_of_sector_weights,2)),fg='red')
    elif sum_of_sector_weights == 100:
        redraw()
        lbl_totalweight_number.config(text=str(round(sum_of_sector_weights,2)),fg='green')

def callback(sv,index): #called when any of the weight entry boxes are edited
    global weight_entry_boxes_tracker
    weight_entry_boxes_tracker -= 1
    if sv.get() != '' and weight_entry_boxes_tracker < 0:
        number = float(sv.get())
        sector_weights[index] = number
        rewriteSectorWeights()
        updateSectorWeights()
        updateAllocations()

def callback2(sv): #called when ent_funds is edited
    if sv.get() != '' and sv.get() != 'Input funds':
        try:
            number = float(sv.get())
            ent_funds.config(fg='black')
            updateAllocations()
        except ValueError as ve:
            print("Error: You cannot put text in the funds box")
    if sv.get() == '':
        setAllocationsZero()

def updateAllocations(): #updates the allocations of funds
    try:
        for i in range(11):
            allocation_labels[i].config(text='$' + str(round((sector_weights[i]/100)*float(ent_funds.get()),2)),fg='black')
    except ValueError as ve:
        return

def setAllocationsZero(): #sets all allocations of funds to zero when ent_funds is empty
    for i in range(11):
        allocation_labels[i].config(text='$0.00',fg='grey')

def temp_text(e): #removes 'Input funds' when clicking on ent_funds
   ent_funds.delete(0,"end")

def rewriteSectorWeights():
    with open('sector_weights.txt','w') as f:
        for elem in sector_weights:
            f.write(str(elem) + '\n')

# WIDGETS

# WIDGETS - font
bold_font = font.Font(weight='bold')

# WIDGETS - column headers
lbl_header_sector = Label(master=frm_editors,text='Sector',font=bold_font,width=17,anchor='w')
lbl_header_weight = Label(master=frm_editors,text='Weight',font=bold_font,width=6)
lbl_header_allocations = Label(master=frm_editors,text='Allocation',font=bold_font,width=10,anchor='w')

# WIDGETS - sector name labels
lbl_sectorname_info_tech = Label(master=frm_editors,text=sector_names[0],width=17,anchor='w')
lbl_sectorname_health = Label(master=frm_editors,text=sector_names[1],width=17,anchor='w')
lbl_sectorname_consumer_discretionary = Label(master=frm_editors,text=sector_names[2],width=17,anchor='w')
lbl_sectorname_communications = Label(master=frm_editors,text=sector_names[3],width=17,anchor='w')
lbl_sectorname_financials = Label(master=frm_editors,text=sector_names[4],width=17,anchor='w')
lbl_sectorname_industrials = Label(master=frm_editors,text=sector_names[5],width=17,anchor='w')
lbl_sectorname_consumer_staples = Label(master=frm_editors,text=sector_names[6],width=17,anchor='w')
lbl_sectorname_utilities = Label(master=frm_editors,text=sector_names[7],width=17,anchor='w')
lbl_sectorname_materials = Label(master=frm_editors,text=sector_names[8],width=17,anchor='w')
lbl_sectorname_real_estate = Label(master=frm_editors,text=sector_names[9],width=17,anchor='w')
lbl_sectorname_energy = Label(master=frm_editors,text=sector_names[10],width=17,anchor='w')
list_lbl_sectornames = [lbl_sectorname_info_tech,lbl_sectorname_health,lbl_sectorname_consumer_discretionary,lbl_sectorname_communications,
    lbl_sectorname_financials,lbl_sectorname_industrials,lbl_sectorname_consumer_staples,lbl_sectorname_utilities,lbl_sectorname_materials,
    lbl_sectorname_real_estate,lbl_sectorname_energy]

# WIDGETS - subtract buttons
btn_subtract_info_tech = Button(master=frm_editors,text='-',command=partial(subtract,0))
btn_subtract_health = Button(master=frm_editors,text='-',command=partial(subtract,1))
btn_subtract_consumer_discretionary = Button(master=frm_editors,text='-',command=partial(subtract,2))
btn_subtract_communications = Button(master=frm_editors,text='-',command=partial(subtract,3))
btn_subtract_financials = Button(master=frm_editors,text='-',command=partial(subtract,4))
btn_subtract_industrials  = Button(master=frm_editors,text='-',command=partial(subtract,5))
btn_subtract_consumer_staples = Button(master=frm_editors,text='-',command=partial(subtract,6))
btn_subtract_utilities = Button(master=frm_editors,text='-',command=partial(subtract,7))
btn_subtract_materials = Button(master=frm_editors,text='-',command=partial(subtract,8))
btn_subtract_real_estate = Button(master=frm_editors,text='-',command=partial(subtract,9))
btn_subtract_energy  = Button(master=frm_editors,text='-',command=partial(subtract,10))
list_subtract_btns = [btn_subtract_info_tech,btn_subtract_health,btn_subtract_consumer_discretionary,btn_subtract_communications,
    btn_subtract_financials,btn_subtract_industrials,btn_subtract_consumer_staples,btn_subtract_utilities,btn_subtract_materials,
    btn_subtract_real_estate,btn_subtract_energy]

# WIDGETS - add buttons
btn_add_info_tech = Button(master=frm_editors,text='+',command=partial(add,0))
btn_add_health = Button(master=frm_editors,text='+',command=partial(add,1))
btn_add_consumer_discretionary = Button(master=frm_editors,text='+',command=partial(add,2))
btn_add_communications = Button(master=frm_editors,text='+',command=partial(add,3))
btn_add_financials = Button(master=frm_editors,text='+',command=partial(add,4))
btn_add_industrials = Button(master=frm_editors,text='+',command=partial(add,5))
btn_add_consumer_staples = Button(master=frm_editors,text='+',command=partial(add,6))
btn_add_utilities = Button(master=frm_editors,text='+',command=partial(add,7))
btn_add_materials = Button(master=frm_editors,text='+',command=partial(add,8))
btn_add_real_estate = Button(master=frm_editors,text='+',command=partial(add,9))
btn_add_energy = Button(master=frm_editors,text='+',command=partial(add,10))
list_add_btns = [btn_add_info_tech,btn_add_health,btn_add_consumer_discretionary,btn_add_communications,btn_add_financials,
    btn_add_industrials,btn_add_consumer_staples,btn_add_utilities,btn_add_materials,btn_add_real_estate,btn_add_energy]

# WIDGETS - weight entry boxes
sv0 = StringVar()
sv0.trace("w", lambda name, index, mode, sv=sv0,i=0: callback(sv,i))
ent_weight_info_tech = Entry(master=frm_editors,textvariable=sv0,width=6)
sv1 = StringVar()
sv1.trace("w", lambda name, index, mode, sv=sv1,i=1: callback(sv,i))
ent_weight_health = Entry(master=frm_editors,textvariable=sv1,width=6)
sv2 = StringVar()
sv2.trace("w", lambda name, index, mode, sv=sv2,i=2: callback(sv,i))
ent_weight_consumer_discretionary = Entry(master=frm_editors,textvariable=sv2,width=6)
sv3 = StringVar()
sv3.trace("w", lambda name, index, mode, sv=sv3,i=3: callback(sv,i))
ent_weight_communications = Entry(master=frm_editors,textvariable=sv3,width=6)
sv4 = StringVar()
sv4.trace("w", lambda name, index, mode, sv=sv4,i=4: callback(sv,i))
ent_weight_financials = Entry(master=frm_editors,textvariable=sv4,width=6)
sv5 = StringVar()
sv5.trace("w", lambda name, index, mode, sv=sv5,i=5: callback(sv,i))
ent_weight_industrials = Entry(master=frm_editors,textvariable=sv5,width=6)
sv6 = StringVar()
sv6.trace("w", lambda name, index, mode, sv=sv6,i=6: callback(sv,i))
ent_weight_consumer_staples = Entry(master=frm_editors,textvariable=sv6,width=6)
sv7 = StringVar()
sv7.trace("w", lambda name, index, mode, sv=sv7,i=7: callback(sv,i))
ent_weight_utilities = Entry(master=frm_editors,textvariable=sv7,width=6)
sv8 = StringVar()
sv8.trace("w", lambda name, index, mode, sv=sv8,i=8: callback(sv,i))
ent_weight_materials = Entry(master=frm_editors,textvariable=sv8,width=6)
sv9 = StringVar()
sv9.trace("w", lambda name, index, mode, sv=sv9,i=9: callback(sv,i))
ent_weight_real_estate = Entry(master=frm_editors,textvariable=sv9,width=6)
sv10 = StringVar()
sv10.trace("w", lambda name, index, mode, sv=sv10,i=10: callback(sv,i))
ent_weight_energy = Entry(master=frm_editors,textvariable=sv10,width=6)
list_weight_ents = [ent_weight_info_tech,ent_weight_health,ent_weight_consumer_discretionary,ent_weight_communications,
    ent_weight_financials,ent_weight_industrials,ent_weight_consumer_staples,ent_weight_utilities,ent_weight_materials,
    ent_weight_real_estate,ent_weight_energy]

# WIDGETS - total weight label and number
lbl_totalweight = Label(master=frm_editors,text='Total Weight',font=bold_font,width=17,anchor='w')
lbl_totalweight_number = Label(master=frm_editors,text=str(sum_of_sector_weights),font=bold_font,fg='green')

# WIDGETS - funds entry box
sv2 = StringVar()
sv2.trace("w", lambda name, index, mode, sv=sv2: callback2(sv))
ent_funds = Entry(master=frm_inputFunds,textvariable=sv2,width=10,fg='grey')
ent_funds.insert(0,'Input funds')

# WIDGETS - allocation labels
lbl_alloc_info_tech = Label(master=frm_editors,text='$X.XX',fg='grey',width=10,anchor='w')
lbl_alloc_health = Label(master=frm_editors,text='$X.XX',fg='grey',width=10,anchor='w')
lbl_alloc_consumer_discretionary = Label(master=frm_editors,text='$X.XX',fg='grey',width=10,anchor='w')
lbl_alloc_communications = Label(master=frm_editors,text='$X.XX',fg='grey',width=10,anchor='w')
lbl_alloc_financials = Label(master=frm_editors,text='$X.XX',fg='grey',width=10,anchor='w')
lbl_alloc_industrials = Label(master=frm_editors,text='$X.XX',fg='grey',width=10,anchor='w')
lbl_alloc_consumer_staples = Label(master=frm_editors,text='$X.XX',fg='grey',width=10,anchor='w')
lbl_alloc_utilities = Label(master=frm_editors,text='$X.XX',fg='grey',width=10,anchor='w')
lbl_alloc_materials = Label(master=frm_editors,text='$X.XX',fg='grey',width=10,anchor='w')
lbl_alloc_real_estate = Label(master=frm_editors,text='$X.XX',fg='grey',width=10,anchor='w')
lbl_alloc_energy = Label(master=frm_editors,text='$X.XX',fg='grey',width=10,anchor='w')
allocation_labels = [lbl_alloc_info_tech,lbl_alloc_health,lbl_alloc_consumer_discretionary,
    lbl_alloc_communications,lbl_alloc_financials,lbl_alloc_industrials,lbl_alloc_consumer_staples,
    lbl_alloc_utilities,lbl_alloc_materials,lbl_alloc_real_estate,lbl_alloc_energy]

# PACKING / GRIDDING

# PACKING / GRIDDING - funds entry box
ent_funds.pack(padx=10,pady=10)

# PACKING / GRIDDING - column headers
lbl_header_sector.grid(row=0,column=0,sticky="w",padx=10)
lbl_header_weight.grid(row=0,column=2)
lbl_header_allocations.grid(row=0,column=4,sticky="w",padx=15)

# PACKING / GRIDDING - sector name labels
for i in range(len(list_lbl_sectornames)):
    list_lbl_sectornames[i].grid(row=i+1,column=0,sticky="w",padx=10)

# PACKING / GRIDDING - subtract buttons
for i in range(len(list_subtract_btns)):
    list_subtract_btns[i].grid(row=i+1,column=1,sticky="nsew")

# PACKING / GRIDDING - weight entry boxes
for i in range(len(list_weight_ents)):
    list_weight_ents[i].grid(row=i+1,column=2)
    list_weight_ents[i].insert(0, sector_weights[i])

# PACKING / GRIDDING - add buttons
for i in range(len(list_add_btns)):
    list_add_btns[i].grid(row=i+1,column=3,sticky="nsew")

# PACKING / GRIDDING - total weight label and number
lbl_totalweight.grid(row=12,column=0,sticky="w",padx=10)
lbl_totalweight_number.grid(row=12,column=2,sticky="w")

# PACKING / GRIDDING - money allocation labels
for i in range(11):
    allocation_labels[i].grid(row=i+1,column=4,sticky="w",padx=15)

# BINDS
ent_funds.bind("<FocusIn>", temp_text)